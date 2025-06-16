from antlr4 import *
from SyntaxErrorListener import SyntaxErrorListener
from PseudoVisitor import PseudoVisitor
from PseudoParser import PseudoParser
from PseudoLexer import PseudoLexer
from StackFrame import StackFrame
from Functions import Functions
from Variables import Variables
from Stack import Stack
import config
import sys
from PseudoExceptions import *

class PseudoInterpreter(PseudoVisitor):
    def __init__(self):
        self.inFunctionCall = False
        self.stack: Stack[StackFrame] = Stack()
        self.functions = Functions()
        self.globalVariables: Variables = Variables()
        self.currentFrame: StackFrame = StackFrame(isRoot=True)
        self.stack.push(self.currentFrame)

    def visitVarDeclStatement(self, ctx: PseudoParser.VarDeclStatementContext):
        value_dict = None
        if ctx.op:
            value_dict = self.visit(ctx.expr())
        var_id = ctx.ID().getText()
        var_type = ctx.TYPE().getText()
        decl_line = ctx.start.line
        is_global = ctx.global_ != None
        currentVariablesStoringObject = (
            self.globalVariables
            if is_global
            else self.currentFrame
        )

        if isinstance(currentVariablesStoringObject, Variables) and currentVariablesStoringObject.check_var(var_id):
            decl_line = currentVariablesStoringObject.get_var(var_id)['decl_line']
            throw_var_redeclaration_exception(
                ctx.start.line, ctx.start.column, var_id, decl_line
            )
        elif isinstance(currentVariablesStoringObject, StackFrame) and self.currentFrame.localVariables.check_var(var_id):
            decl_line = self.currentFrame.localVariables.get_var(var_id)['decl_line']
            throw_var_redeclaration_exception(ctx.start.line, ctx.start.column, var_id, decl_line)

        currentVariablesStoringObject.set_var(var_id, None, decl_line, var_type)

        if ctx.op:
            try:
                value_type = value_dict["type"]

                if var_type == "string":
                    if value_type != "string":
                        raise ValueError("Expected string")

                elif var_type == "int":
                    if value_type == "int":
                        pass
                    elif value_type == "float":
                        value_dict['value'] = int(value_dict['value'])
                    else:
                        raise ValueError("Expected int")

                elif var_type == "float":
                    if value_type == "float":
                        pass
                    elif value_type == "int":
                        value_dict['value'] = float(value_dict['value'])
                    else:
                        raise ValueError("Expected float")

                elif var_type == "boolean":
                    if value_type != "boolean":
                        raise ValueError("Expected boolean")

                else:
                    throw_wrong_type_exception(
                        ctx.start.line, ctx.start.column, var_type
                    )
            except Exception as e:
                throw_wrong_type_exception(ctx.start.line, ctx.start.column, var_type)

            currentVariablesStoringObject.set_value(var_id, value_dict['value'])

    def get_nummeric_value(self, var: str):
        return float(var) if "." in var else int(var)

    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.expr())['value']
        print(value)

    def visitExpr(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return self.visit(ctx.expr(0))

        if ctx.ID():
            var_id = ctx.ID().getText()
            if self.currentFrame.check_var(var_id):
                var_dict = self.currentFrame.get_var(var_id)
                return {"type": var_dict['type'], "value": var_dict['value']}
            elif self.globalVariables.check_var(var_id):
                var_dict = self.globalVariables.get_var(var_id)
                return {"type": var_dict['type'], "value": var_dict['value']}
            else:
                known_names = self.currentFrame.get_all_identifiers()
                throw_undefined_name_exception(ctx.start.line, ctx.start.column, var_id, known_names)

        elif ctx.op and ctx.op.type == PseudoParser.PARENT:
            if self.currentFrame.returnAddress is None:
                throw_no_parent_scope_exception(ctx.start.line, ctx.start.column)
            
            returnFrame = self.currentFrame
            self.currentFrame = self.currentFrame.returnAddress
            var_dict = self.visit(ctx.expr(0))
            self.currentFrame = returnFrame
            return {"type": var_dict['type'], "value": var_dict['value']}

        elif ctx.STRING():
            value = ctx.STRING().getText()[1:-1]
            decoded = bytes(value, "utf-8").decode("unicode_escape")
            return {"type": "string", "value": decoded}

        elif ctx.BOOL():
            value = ctx.BOOL().getText() == "True"
            return {"type": "boolean", "value": value}

        elif ctx.NUMBER():
            value = int(ctx.NUMBER().getText())
            return {"type": "int", "value": value}

        elif ctx.DOUBLE():
            value = float(ctx.DOUBLE().getText())
            return {"type": "float", "value": value}
        
        elif ctx.op and ctx.op.type == PseudoParser.TYPE:
            parse_type = ctx.TYPE().getText()
            if ctx.expr(0):
                value = self.visit(ctx.expr(0))["value"]
                try:
                    if parse_type == "int":
                        return {"type": "int", "value": int(value)}
                    elif parse_type == "float":
                        return {"type": "float", "value": float(value)}
                    elif parse_type == "string":
                        return {"type": "string", "value": str(value)}
                    elif parse_type == "boolean":
                        return {"type": "boolean", "value": bool(value)}
                except Exception as e:
                    throw_conversion_exception(
                        ctx.start.line,
                        ctx.start.column,
                        parse_type,
                        value,
                    )

        elif ctx.op and ctx.op.type == PseudoParser.PLUS:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']

            match (left_value, right_value):
                case (str(), str()):
                    value = left_value + right_value
                    return {"type": "string", "value": value}
                case (int(), int()):
                    value =  left_value + right_value
                    return {"type": "int", "value": value}
                case (int() | float(), int() | float()):
                    value =  left_value + right_value
                    return {"type": "float", "value": value}
                case _:
                    throw_unsupported_operator_exception(
                        ctx.start.line,
                        ctx.start.column,
                        ctx.op.text,
                        type(left_value).__name__,
                        type(right_value).__name__
                    )

        elif ctx.op and ctx.op.type == PseudoParser.MINUS:
            left_value = self.visit(ctx.expr(0))['value']
            if not (ctx.expr(1) is None):
                right_value = self.visit(ctx.expr(1))['value']

                if not (isinstance(left_value, str) or isinstance(right_value, str)):
                    value =  left_value - right_value

                    type = None
                    if isinstance(value, str):
                        type = 'string'
                    elif isinstance(value, int):
                        type = 'int'
                    elif isinstance(value, float):
                        type = 'float'

                    return {"type": type, "value": value}

                else:
                    throw_unsupported_operator_exception(
                        ctx.start.line,
                        ctx.start.column,
                        ctx.op.text,
                        type(left_value).__name__,
                        type(right_value).__name__
                    )

            else:
                if isinstance(left_value, str):
                    throw_unsupported_operator_exception(
                        ctx.start.line,
                        ctx.start.column,
                        ctx.op.text,
                        type(left_value).__name__,
                        "int/float"
                    )
                
                type = None
                if isinstance(left_value, int):
                    type = 'int'
                elif isinstance(left_value, float):
                    type = 'float'

                return {"type": type, "value": -left_value}

        elif ctx.op and ctx.op.type == PseudoParser.MULT:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']
            if not (isinstance(left_value, str) and isinstance(right_value, str)):
                value = left_value * right_value
                type = None
                if isinstance(value, int):
                    type = 'int'
                else:
                    type = 'float'

                return {"type": type, "value": value}

            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__,
                )

        elif ctx.op and ctx.op.type == PseudoParser.DIV:
            left_expr_ctx = ctx.expr(0)
            left_value = self.visit(left_expr_ctx)['value']
            
            right_expr_ctx = ctx.expr(1)
            right_value = self.visit(right_expr_ctx)['value']
            
            if not (isinstance(left_value, str) or isinstance(right_value, str)):
                if abs(right_value) < 1e-9:
                    right_column = right_expr_ctx.start.column
                    throw_dividing_by_zero_exception(ctx.start.line, right_column)
               
                value = left_value / right_value
                type = None
                if isinstance(value, int):
                    type = 'int'
                else:
                    type = 'float'
                
                return {"type": type, "value": value}
            
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__
                )

        elif ctx.op and ctx.op.type == PseudoParser.INTDIV:
            left_expr_ctx = ctx.expr(0)
            left_value = self.visit(left_expr_ctx)['value']
            
            right_expr_ctx = ctx.expr(1)
            right_value = self.visit(right_expr_ctx)['value']

            if not (isinstance(left_value, str) or isinstance(right_value, str)):
                if abs(right_value) < 1e-9:
                    right_column = right_expr_ctx.start.column
                    throw_dividing_by_zero_exception(ctx.start.line, right_column)
                value = left_value // right_value
                return {"type": 'int', "value": value}
            
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__
                )

        elif ctx.op and ctx.op.type == PseudoParser.AND:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']
            if isinstance(left_value, bool) and isinstance(right_value, bool):
                value = left_value and right_value
                return {"type": 'boolean', "value": value}
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value.__name__, type(right_value).__name__)
                )

        elif ctx.op and ctx.op.type == PseudoParser.OR:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']
            if isinstance(left_value, bool) and isinstance(right_value, bool):
                value = left_value or right_value
                return {"type": 'boolean', "value": value}
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value.__name__, type(right_value).__name__)
                )

        elif ctx.op and ctx.op.type == PseudoParser.NOT:
            value = self.visit(ctx.expr(0))['value']
            col = ctx.expr(0).start.column
            if isinstance(value, bool):
                value = not value
                return {"type": 'boolean', "value": value}
            else:
                throw_bool_op_with_another_type_exception(ctx.start.line, col)

        elif ctx.op and ctx.op.type == PseudoParser.GREATER:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']
            if isinstance(left_value, (int, float)) and isinstance(
                right_value, (int, float)
            ):
                value = left_value > right_value
                return {"type": 'boolean', "value": value}
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__
                )

        elif ctx.op and ctx.op.type == PseudoParser.GREATEREQUAL:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']
            if isinstance(left_value, (int, float)) and isinstance(
                right_value, (int, float)
            ):
                value = left_value >= right_value
                return {"type": 'boolean', "value": value}
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__
                )

        elif ctx.op and ctx.op.type == PseudoParser.SMALLER:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']
            if isinstance(left_value, (int, float)) and isinstance(
                right_value, (int, float)
            ):
                value = left_value < right_value
                return {"type": 'boolean', "value": value}
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__
                )

        elif ctx.op and ctx.op.type == PseudoParser.SMALLEREQUAL:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']
            if isinstance(left_value, (int, float)) and isinstance(
                right_value, (int, float)
            ):
                value = left_value <= right_value
                return {"type": 'boolean', "value": value}
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__
                )

        elif ctx.op and ctx.op.type == PseudoParser.EQUAL:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']
            if isinstance(left_value, (int, float)) and isinstance(
                right_value, (int, float)
            ):
                value = left_value == right_value
                return {"type": 'boolean', "value": value}
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__
                )

        elif ctx.op and ctx.op.type == PseudoParser.DIFFERENT:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']
            value = left_value != right_value
            return {"type": 'boolean', "value": value}

        else:
            return self.visitChildren(ctx)

    def visitAssignmentStatement(self, ctx, jump=None):
        if ctx.parent:
            if self.currentFrame.returnAddress is None:
                throw_no_parent_scope_exception(ctx.start.line, ctx.start.column)

            jump = self.currentFrame if jump is None else jump

            returnFrame = self.currentFrame
            self.currentFrame = self.currentFrame.returnAddress
            self.visitAssignmentStatement(ctx.assignmentStatement(), jump=jump)
            self.currentFrame = returnFrame
        else:
            var_id = ctx.ID().getText()
            currentVariablesStoringObject = (
                self.currentFrame
                if self.currentFrame.check_var(var_id)
                else self.globalVariables
            )

            if not currentVariablesStoringObject.check_var(var_id):
                known_names = self.currentFrame.get_all_identifiers()
                throw_undefined_name_exception(ctx.start.line, ctx.start.column, var_id, known_names)

            var_type = currentVariablesStoringObject.get_var(var_id)["type"]

            if ctx.op and ctx.op.type == PseudoParser.INCREMENT:
                val = currentVariablesStoringObject.get_var(var_id)["value"]
                if isinstance(val, int):
                    currentVariablesStoringObject.set_value(var_id, val + 1)
                elif isinstance(val, float):
                    currentVariablesStoringObject.set_value(var_id, val + 1.0)
                else:
                    throw_wrong_type_exception(
                        ctx.start.line, ctx.start.column, type(val).__name__
                    )
            elif ctx.op and ctx.op.type == PseudoParser.DECREMENT:
                val = currentVariablesStoringObject.get_var(var_id)["value"]
                if isinstance(val, int):
                    currentVariablesStoringObject.set_value(var_id, val - 1)
                elif isinstance(val, float):
                    currentVariablesStoringObject.set_value(var_id, val - 1.0)
                else:
                    throw_unknown_operator_exception(
                        ctx.start.line, ctx.start.column, ctx.op.text
                    )
            else:
                value = None
                if jump:
                    returnAddress = self.currentFrame
                    self.currentFrame = jump
                    value = self.visit(ctx.expr())
                    self.currentFrame = returnAddress
                else:
                    value = self.visit(ctx.expr())

                if currentVariablesStoringObject.check_var(var_id) is False:
                    known_names = self.currentFrame.get_all_identifiers().union(self.globalVariables.get_all_names())
                    throw_undefined_name_exception(ctx.start.line, ctx.start.column, var_id, known_names)

                try:
                    value_type = value["type"]

                    if var_type == "string":
                        if value_type != "string":
                            raise ValueError("Expected string")

                    elif var_type == "int":
                        if value_type == "int":
                            pass
                        elif value_type == "float":
                            value['value'] = int(value['value'])
                        else:
                            raise ValueError("Expected int")

                    elif var_type == "float":
                        if value_type == "float":
                            pass
                        elif value_type == "int":
                            value['value'] = float(value['value'])
                        else:
                            raise ValueError("Expected float")

                    elif var_type == "boolean":
                        if value_type != "boolean":
                            raise ValueError("Expected boolean")

                    else:
                        throw_wrong_type_exception(
                            ctx.start.line, ctx.start.column, var_type
                        )

                except Exception:
                    throw_wrong_type_exception(ctx.start.line, ctx.start.column, var_type)

                currentVariablesStoringObject.set_value(var_id, value['value'])

    def visitIfStatement(self, ctx: PseudoParser.IfStatementContext):

        returnAddress = self.currentFrame
        if self.visit(ctx.expr(0))['value']:
            newStackFrame = StackFrame(returnAddress=returnAddress)
            self.stack.push(newStackFrame)
            self.currentFrame = self.stack.peek()

            try:
                for stmt in ctx.body(0).statement():
                    self.visit(stmt)
            except Exception:
                raise
            finally:
                self.stack.pop()
                self.currentFrame = self.stack.peek()
            return

        num_elseif = len(ctx.expr()) - 1
        for i in range(num_elseif):

            if self.visit(ctx.expr(i + 1))['value']:
                newStackFrame = StackFrame(returnAddress=returnAddress)
                self.stack.push(newStackFrame)
                self.currentFrame = self.stack.peek()

                try:
                    for stmt in ctx.body(i + 1).statement():
                        self.visit(stmt)
                except Exception:
                    raise
                finally:
                    self.stack.pop()
                    self.currentFrame = self.stack.peek()
                return

        if ctx.body(num_elseif + 1) is not None:
            newStackFrame = StackFrame(returnAddress=self.currentFrame)
            self.stack.push(newStackFrame)
            self.currentFrame = self.stack.peek()

            try:
                for stmt in ctx.body(num_elseif + 1).statement():
                    self.visit(stmt)
            except Exception:
                raise
            finally:
                self.stack.pop()
                self.currentFrame = self.stack.peek()

    def visitWhileStatement(self, ctx: PseudoParser.WhileStatementContext):
        newStackFrame = StackFrame(returnAddress=self.currentFrame)
        self.stack.push(newStackFrame)
        self.currentFrame = self.stack.peek()

        condition = self.visit(ctx.expr())['value']
        if not isinstance(condition, bool):
            throw_wrong_type_exception(ctx.start.line, ctx.start.column, "boolean")

        while condition:
            newStackFrame = StackFrame(returnAddress=self.currentFrame)
            self.stack.push(newStackFrame)
            self.currentFrame = self.stack.peek()
            
            try:
                self.visit(ctx.body())
            except ContinueException:
                continue
            except BreakException:
                break

            condition = self.visit(ctx.expr())['value']

            self.stack.pop()
            self.currentFrame = self.stack.peek()
        
        self.stack.pop()
        self.currentFrame = self.stack.peek()

    def visitForStatement(self, ctx: PseudoParser.ForStatementContext):
        newStackFrame = StackFrame(returnAddress=self.currentFrame)
        self.stack.push(newStackFrame)
        self.currentFrame = self.stack.peek()

        if ctx.entryStmt:
            self.visit(ctx.initStatement())

        condition = self.visit(ctx.expr())['value'] if ctx.expr() else True

        while condition:
            newStackFrame = StackFrame(returnAddress=self.currentFrame)
            self.stack.push(newStackFrame)
            self.currentFrame = self.stack.peek()

            if not isinstance(condition, bool):
                throw_wrong_type_exception(ctx.start.line, ctx.start.column, "boolean")
            if ctx.body():
                try:
                    self.visit(ctx.body())
                except ContinueException:
                    continue
                except BreakException:
                    break
                finally:
                    if ctx.assignmentStatement():
                        self.visit(ctx.assignmentStatement())

            condition = self.visit(ctx.expr())['value'] if ctx.expr() else True
            
            self.stack.pop()
            self.currentFrame = self.stack.peek()

        self.stack.pop()
        self.currentFrame = self.stack.peek()

    def visitFunctionCallStatement(
        self, ctx: PseudoParser.FunctionCallStatementContext
    ):
        name = ctx.ID().getText()

        types_map = {
            "int": int,
            "float": float,
            "string": str,
            "boolean": bool,
            "void": type(None),
        }

        if not self.functions.check_fun(name):
            throw_non_defined_function_exception(ctx.start.line, ctx.start.column, name)

        args = []
        if ctx.argumentList():
            for expr_ctx in ctx.argumentList().expr():
                value = self.visit(expr_ctx)
                column = expr_ctx.start.column
                args.append((value, column))

        try:
            newStackFrame = StackFrame(returnAddress=self.currentFrame)
            newStackFrame.isRoot = True
            self.stack.push(newStackFrame)
            self.currentFrame = newStackFrame
            self.call_function(name, args, ctx)

            if self.functions.get_fun(name)["return_type"] != "void":
                line = self.functions.get_fun(name)['decl_line']
                col = self.functions.get_fun(name)['return_type_col']
                throw_function_doesnt_return_exception(line, col)

        except ReturnException as ret:
            if self.functions.get_fun(name)["return_type"] == "void":
                line = self.functions.get_fun(name)['decl_line']
                col = self.functions.get_fun(name)['return_type_col']
                throw_void_function_returns_exception(line, col)

            return_type = self.functions.get_fun(name)["return_type"]
            if not isinstance(ret.value['value'], types_map[return_type]):
                line = self.functions.get_fun(name)['decl_line']
                col = self.functions.get_fun(name)['return_type_col']
                throw_function_returns_types_dont_match_exception(line, col)
            return ret.value
        
        except Exception:
            raise
        finally:
            self.stack.pop()
            self.currentFrame = self.currentFrame.returnAddress

    def call_function(self, name, args, ctx):
        func = self.functions.get_fun(name)

        types_map = {
            "int": int,
            "float": float,
            "string": str,
            "boolean": bool,
            "void": type(None),
        }

        if len(args) != len(func["params"]):
            throw_wrong_parameters_number_exception(ctx.start.line, ctx.start.column, name, len(args), len(func["params"]))

        for param, arg in zip(func["params"], args):
            
            par_name = param
            var_type = func["params"][par_name]['type']
            if arg[0]['type'] != var_type:
                error_line = ctx.start.line
                error_col = arg[1]
                func_def_line = func['decl_line']
                param_col_in_def = func["params"][par_name]['decl_column']
                param_type = arg[0]['type']

                throw_wrong_parameter_typw_exception(error_line, error_col, func_def_line, param_col_in_def, var_type, param_type)

            decl_line = func["decl_line"]
            if self.currentFrame.localVariables.check_var(par_name):
                decl_column = self.currentFrame.localVariables.get_var(par_name)['decl_column']
                throw_redeclaration_in_function_def_exception(
                    ctx.start.line, ctx.start.column, par_name, decl_column
                )
            else:
                self.currentFrame.localVariables.set_var(
                    par_name, arg[0]['value'], decl_line, var_type
                )

        tree = func["body"]
        self.visit(tree)

    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.val)
        raise ReturnException(value)

    def visitFunctionDef(self, ctx):
        if not self.currentFrame.isRoot:
            throw_fun_def_in_block_exception(ctx.start.line, ctx.start.column)
        
        name = ctx.name.text
        return_type = ctx.type_.text
        body = ctx.block
        type_column = ctx.TYPE().getSymbol().column

        if self.functions.check_fun(name):
            decl_line = self.functions.get_fun(name)["decl_line"]
            throw_function_redeclaration_exception(ctx.start.line, ctx.start.column, name, decl_line)

        params = {}
        if ctx.paramList():
            for param_ctx in ctx.paramList().param():
                param_type = param_ctx.TYPE().getText()
                param_name = param_ctx.ID().getText()
                if param_name in params.keys():
                    column = param_ctx.ID().getSymbol().column
                    decl_column = params[param_name]['decl_column']
                    throw_redeclaration_in_function_def_exception(
                        ctx.start.line, column, param_name, decl_column
                    )
                else:
                    decl_column = param_ctx.ID().getSymbol().column
                    params[param_name] = {'type': param_type,
                                          'decl_column': decl_column}

        self.functions.set_fun(
            name, return_type, params, body, ctx.start.line, type_column
        )

    def visitContinueStatement(self, ctx):
        raise ContinueException("No message")

    def visitBreakStatement(self, ctx):
        raise BreakException("No message")

    def visitCodeBlock(self, ctx):
        newStackFrame = StackFrame(returnAddress=self.currentFrame)
        self.stack.push(newStackFrame)
        self.currentFrame = self.stack.peek()
        
        self.visit(ctx.body())

        self.stack.pop()
        self.currentFrame = self.stack.peek()

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value


class ContinueException(Exception):
    def __init__(self, value):
        self.value = value


class BreakException(Exception):
    def __init__(self, value):
        self.value = value


class ContinueException(Exception):
    def __init__(self, value):
        self.value = value


class BreakException(Exception):
    def __init__(self, value):
        self.value = value


def run_interpreter(inputStream=None, filename = "program.pseudo"):
    try:
        inputStream = (
            inputStream
            if inputStream
            else FileStream(filename, encoding="utf-8")
        )
        config.source_file_name = filename

        lexer = PseudoLexer(inputStream)
        stream = CommonTokenStream(lexer)
        parser = PseudoParser(stream)

        parser.removeErrorListeners()
        parser.addErrorListener(SyntaxErrorListener())

        tree = parser.program()

        interpreter = PseudoInterpreter()

        interpreter.visit(tree)

    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    if len(sys.argv) != 2:
            print("Usage: python3 pseudoInterpreter.py <filename>")
            sys.exit(1)
    filename = sys.argv[1]
    run_interpreter(filename=filename)
