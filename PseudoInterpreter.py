from antlr4 import *
from SyntaxErrorListener import SyntaxErrorListener
from PseudoVisitor import PseudoVisitor
from PseudoParser import PseudoParser
from PseudoLexer import PseudoLexer
from StackFrame import StackFrame
from Functions import Functions
from Variables import Variables
from Listener import Listener
from Stack import Stack
import sys
from PseudoExceptions import (
    throw_unsupported_operator_exception,
    throw_undefined_name_exception,
    throw_wrong_type_exception,
    throw_non_defined_function_exception,
    throw_redeclaration_in_function_def_exception,
    throw_unknown_operator_exception,
    throw_conversion_exception,
    throw_var_redeclaration_exception,
    throw_no_parent_scope_exception
)


class PseudoInterpreter(PseudoVisitor):
    def __init__(self, initialStackFrame: StackFrame, functions: Functions = None, globalVariables = None):
        self.inFunctionCall = False
        self.stack: Stack[StackFrame] = Stack()
        self.stack.push(initialStackFrame)
        self.functions = functions
        self.globalVariables: Variables = globalVariables
        self.currentFrame: StackFrame = initialStackFrame

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

        if isinstance(currentVariablesStoringObject, Variables) and currentVariablesStoringObject.check_var(
            var_id
        ):  throw_var_redeclaration_exception(
                ctx.start.line, ctx.start.column, var_id, decl_line
            )
        elif isinstance(currentVariablesStoringObject, StackFrame) and self.currentFrame.localVariables.check_var(var_id):
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
                    else:
                        raise ValueError("Expected int")

                elif var_type == "float":
                    if value_type == "float":
                        pass
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
                throw_undefined_name_exception(ctx.start.line, ctx.start.column, var_id)

        elif ctx.op and ctx.op.type == PseudoParser.PARENT:
            if self.currentFrame.isRoot:
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
                        value
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
                        type(right_value).__name__,
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
                        type(right_value).__name__,
                    )

            else:
                if isinstance(left_value, str):
                    throw_unsupported_operator_exception(
                        ctx.start.line,
                        ctx.start.column,
                        ctx.op.text,
                        type(left_value).__name__,
                        "int/float",
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
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']

            if not (isinstance(left_value, str) or isinstance(right_value, str)):
                if abs(right_value) < 1e-9:
                    raise Exception("Cannot divide by zero")
               
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
                    type(right_value).__name__,
                )

        elif ctx.op and ctx.op.type == PseudoParser.INTDIV:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']

            if not (isinstance(left_value, str) or isinstance(right_value, str)):
                if abs(right_value) < 1e-9:
                    raise Exception("Cannot divide by zero")
                value = left_value // right_value
                return {"type": 'int', "value": value}
            
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__,
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
                    type(left_value.__name__, type(right_value).__name__),
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
                    type(left_value.__name__, type(right_value).__name__),
                )

        elif ctx.op and ctx.op.type == PseudoParser.NOT:
            value = self.visit(ctx.expr(0))['value']
            if isinstance(value, bool):
                value = not value
                return {"type": 'boolean', "value": value}
            else:
                raise Exception(
                    f"Error in line: {ctx.start.line}, column: {ctx.start.column}: this value is not boolean."
                )

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
                    type(right_value).__name__,
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
                    type(right_value).__name__,
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
                    type(right_value).__name__,
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
                    type(right_value).__name__,
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
                    type(right_value).__name__,
                )

        elif ctx.op and ctx.op.type == PseudoParser.DIFFERENT:
            left_value = self.visit(ctx.expr(0))['value']
            right_value = self.visit(ctx.expr(1))['value']
            value = left_value != right_value
            return {"type": 'boolean', "value": value}

        else:
            return self.visitChildren(ctx)

    def visitAssignmentStatement(self, ctx):
        if ctx.parent:
            if self.currentFrame.isRoot:
                throw_no_parent_scope_exception(ctx.start.line, ctx.start.column)
            
            returnFrame = self.currentFrame
            self.currentFrame = self.currentFrame.returnAddress
            self.visit(ctx.assignmentStatement())
            self.currentFrame = returnFrame
        else:
            var_id = ctx.ID().getText()
            currentVariablesStoringObject = (
                self.currentFrame
                if self.currentFrame.check_var(var_id)
                else self.globalVariables
            )

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
                value = self.visit(ctx.expr())
                if currentVariablesStoringObject.check_var(var_id) is False:
                    throw_undefined_name_exception(ctx.start.line, ctx.start.column, var_id)

                try:
                    value_type = value["type"]

                    if var_type == "string":
                        if value_type != "string":
                            raise ValueError("Expected string")

                    elif var_type == "int":
                        if value_type == "int":
                            pass
                        else:
                            raise ValueError("Expected int")

                    elif var_type == "float":
                        if value_type == "float":
                            pass
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
            newStackFrame = self.currentFrame.copy()
            newStackFrame.returnAddress = returnAddress
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
                newStackFrame = self.currentFrame.copy()
                newStackFrame.returnAddress = returnAddress
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
            newStackFrame = self.currentFrame.copy()
            newStackFrame.returnAddress = returnAddress
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
        newStackFrame = self.currentFrame.copy()
        newStackFrame.returnAddress = self.currentFrame
        self.stack.push(newStackFrame)
        self.currentFrame = self.stack.peek()

        condition = self.visit(ctx.expr())['value']
        if not isinstance(condition, bool):
            throw_wrong_type_exception(ctx.start.line, ctx.start.column, "boolean")

        while condition:
            newStackFrame = self.currentFrame.copy()
            newStackFrame.returnAddress = self.currentFrame
            self.stack.push(newStackFrame)
            self.currentFrame = self.stack.peek()
            
            listener = Listener(self.currentFrame, self, functions=self.functions)
            walker = ParseTreeWalker()
            walker.walk(listener, ctx.body())

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
        newStackFrame = self.currentFrame.copy()
        newStackFrame.returnAddress = self.currentFrame
        self.stack.push(newStackFrame)
        self.currentFrame = self.stack.peek()

        if ctx.entryStmt:
            self.visit(ctx.initStatement())

        condition = self.visit(ctx.expr())['value'] if ctx.expr() else True

        listener = Listener(self.currentFrame, self, functions=self.functions)
        walker = ParseTreeWalker()

        while condition:
            newStackFrame = self.currentFrame.copy()
            newStackFrame.returnAddress = self.currentFrame
            self.stack.push(newStackFrame)
            self.currentFrame = self.stack.peek()

            if not isinstance(condition, bool):
                throw_wrong_type_exception(ctx.start.line, ctx.start.column, "boolean")
            if ctx.body():
                walker.walk(listener, ctx.body())
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
                args.append(self.visit(expr_ctx))

        try:
            newStackFrame = self.currentFrame.copy()
            newStackFrame.returnAddress = self.currentFrame
            newStackFrame.isRoot = True
            self.stack.push(newStackFrame)
            self.currentFrame = newStackFrame
            self.call_function(name, args, ctx)

            if self.functions.get_fun(name)["return_type"] != "void":
                raise Exception("Error: Function doesnt return value, but it should.")

        except ReturnException as ret:
            if self.functions.get_fun(name)["return_type"] == "void":
                raise Exception("Error: Void functions cannot return values.")

            return_type = self.functions.get_fun(name)["return_type"]
            if not isinstance(ret.value['value'], types_map[return_type]):
                raise Exception(
                    "Error: Returned value doesnt match with declared in function."
                )
            return ret.value
        except Exception as e:
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
            raise Exception("Error: Wrong parameters number!")

        for param, arg in zip(func["params"], args):

            var_name = param
            var_type = func["params"][var_name]
            if arg['type'] == types_map[var_type]:
                raise Exception("Error: Wrong parameter type!")

            decl_line = ctx.start.line
            if self.currentFrame.localVariables.check_var(var_name):
                decl_line = func["decl_line"]
                throw_redeclaration_in_function_def_exception(
                    ctx.start.line, ctx.start.column, var_name, decl_line
                )
            else:
                self.currentFrame.localVariables.set_var(
                    var_name, arg['value'], decl_line, var_type
                )

        listener = Listener(self.currentFrame, self, functions=self.functions)
        walker = ParseTreeWalker()
        tree = func["body"]
        walker.walk(listener, tree)
        self.visit(tree)

    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.val)
        raise ReturnException(value)

    def visitFunctionDef(self, ctx):
        return None

    def visitContinueStatement(self, ctx):
        raise ContinueException("No message")

    def visitBreakStatement(self, ctx):
        raise BreakException("No message")

    def visitCodeBlock(self, ctx):
        newStackFrame = self.currentFrame.copy()
        newStackFrame.returnAddress = self.currentFrame
        self.stack.push(newStackFrame)
        self.currentFrame = self.stack.peek()
        
        listener = Listener(self.currentFrame, self, functions=self.functions)
        walker = ParseTreeWalker()
        tree = ctx.body()
        walker.walk(listener, tree)
        self.visit(tree)

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
        lexer = PseudoLexer(inputStream)
        stream = CommonTokenStream(lexer)
        parser = PseudoParser(stream)

        parser.removeErrorListeners()
        parser.addErrorListener(SyntaxErrorListener())

        tree = parser.program()

        initialStackFrame = StackFrame(
            globalVariables=Variables(),
            isRoot=True
        )

        functions = Functions()
        globalVariables = Variables()

        interpreter = PseudoInterpreter(
            initialStackFrame=initialStackFrame, functions=functions, globalVariables=globalVariables
        )
        listener = Listener(initialStackFrame, interpreter, functions=functions)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

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
