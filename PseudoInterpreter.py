from antlr4 import *
from PseudoVisitor import PseudoVisitor
from PseudoLexer import PseudoLexer
from PseudoParser import PseudoParser
from SyntaxErrorListener import SyntaxErrorListener
from Listener import Listener
from Memory import Memory
from PseudoExceptions import throw_unknown_operator_exception, throw_undefined_name_exception, throw_wrong_type_exception, throw_non_defined_function_exception
import re
import copy

class PseudoInterpreter(PseudoVisitor):
    def __init__(self, memory: Memory):
        self.memory = memory
    
    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        
    def get_nummeric_value(self, var: str):
        return float(var) if '.' in var else int(var)
    
    def visitExpr(self, ctx):
        print("Visiting expression:", ctx.op.type if ctx.op else "None")
        
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expr(0))
        
        if ctx.ID():
            var_id = ctx.ID().getText()
            if var_id not in self.memory.variables.keys():
                print(self.memory.variables.keys())
                throw_undefined_name_exception(ctx.start.line, ctx.start.column, var_id)
            else:
                return self.memory.variables[var_id]["value"]

        elif ctx.STRING():
            value = ctx.STRING().getText()[1:-1]  # Usuwanie cudzysłowów
            return bytes(value, "utf-8").decode("unicode_escape")
        
        elif ctx.BOOL():
            value = ctx.BOOL().getText()
            return value == 'true'
        
        elif ctx.NUMBER() or ctx.DOUBLE():
            return self.get_nummeric_value(ctx.getText())
        
        elif ctx.op and ctx.op.type == PseudoParser.PLUS:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))

            match (left_value, right_value):
                case (str(), str()):
                    return left_value + right_value
                case (int() | float(), int() | float()):
                    return left_value + right_value
                case _:
                    throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value).__name__, type(right_value).__name__)
        elif ctx.op and ctx.op.type == PseudoParser.MINUS:  
            left_value = self.visit(ctx.expr(0))
            print("Left value:", left_value)
            print("Right value:", ctx.expr(1))
            if not(ctx.expr(1) is None):
                right_value = self.visit(ctx.expr(1))

                if not (isinstance(left_value, str) or isinstance(right_value, str)):
                    return left_value - right_value
                else:
                    throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value).__name__, type(right_value).__name__)

            else:
                print("Unary minus")
                if isinstance(left_value, int, float):
                    throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value).__name__, "int/float")
                return -left_value
            
        elif ctx.op and ctx.op.type == PseudoParser.MULT:  
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))

            if not (isinstance(left_value, str) and isinstance(right_value, str)):
                return left_value * right_value
            else:
                throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value).__name__, type(right_value).__name__)
        
        elif ctx.op and ctx.op.type == PseudoParser.DIV:  
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))

            if not (isinstance(left_value, str) or isinstance(right_value, str)):
                if abs(right_value) < 1e-9: raise Exception("Cannot divide by zero")
                return left_value / right_value
            else:
                throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value).__name__, type(right_value).__name__)

        elif ctx.op and ctx.op.type == PseudoParser.INTDIV:  
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            
            if not (isinstance(left_value, str) or isinstance(right_value, str)):
                if abs(right_value) < 1e-9: raise Exception("Cannot divide by zero")
                return left_value // right_value
            else:
                throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value).__name__, type(right_value).__name__)


        elif ctx.op and ctx.op.type == PseudoParser.AND:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, bool) and isinstance(right_value, bool):
                return left_value and right_value
            else:
                throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value.__name__, type(right_value).__name__))
                
        elif ctx.op and ctx.op.type == PseudoParser.OR:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, bool) and isinstance(right_value, bool):
                return left_value or right_value
            else:
                throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value.__name__, type(right_value).__name__))
                                        
        elif ctx.op and ctx.op.type == PseudoParser.NOT:
            value = self.visit(ctx.expr(0))
            if isinstance(value, bool):
                return not value
            else:
                raise Exception(f"Error in line: {ctx.start.line}, column: {ctx.start.column}: this value is not boolean.")

        elif ctx.op and ctx.op.type == PseudoParser.GREATER:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, (int, float)) and isinstance(right_value, (int,float)):
                return left_value > right_value
            elif isinstance(left_value, str) and isinstance(right_value, str):
                return left_value > right_value
            else:
                throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value).__name__, type(right_value).__name__)


        elif ctx.op and ctx.op.type == PseudoParser.SMALLER:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, (int, float)) and isinstance(right_value, (int, float)):
                return left_value < right_value
            elif isinstance(left_value, str) and isinstance(right_value, str):
                return left_value < right_value
            else:
                throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value).__name__, type(right_value).__name__)

        elif ctx.op and ctx.op.type == PseudoParser.EQUAL:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, (int, float)) and isinstance(right_value, (int, float)):
                return left_value == right_value
            elif isinstance(left_value, str) and isinstance(right_value, str):
                return left_value == right_value
            else:
                throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value).__name__, type(right_value).__name__)

        elif ctx.op and ctx.op.type == PseudoParser.DIFFERENT:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            return left_value != right_value
                                                 
        else:
            return self.visitChildren(ctx)
        
    def visitAssignmentStatement(self, ctx):
        var_id = ctx.ID().getText()
        var_type = self.memory.variables[var_id]["type"]
        value = str(self.visit(ctx.expr()))
        
        if var_id not in self.memory.variables.keys():
            throw_undefined_name_exception(ctx.start.line, ctx.start.column, var_id)
        
        try:
            if var_type == 'string':
                if not re.fullmatch(r'(?:\\.|(?!(["\'])).)*', value):
                    raise ValueError

            elif var_type == 'int':
                if not re.fullmatch(r'-?\d+', value):
                    raise ValueError
                value = int(value)

            elif var_type == 'float':
                if not re.fullmatch(r'-?\d+\.\d+', value):
                    raise ValueError
                value = float(value)

            elif var_type == 'boolean':
                if not value.lower() in ["true", "false"]:
                    raise ValueError
                value = value.lower() == "true"

            else:
                throw_wrong_type_exception(ctx.start.line, ctx.start.column, var_type)
        
        except Exception:
            throw_wrong_type_exception(ctx.start.line, ctx.start.column, var_type)
        
        self.memory.variables[var_id]["value"] = value

    def call_function(self, name, args, ctx):
        func = self.memory.functions[name]
        local_memory = copy.deepcopy(self.memory)

        type_map = {
            "int": int,
            "float": float,
            "string": str,
            "boolean": bool,
            "void": type(None)
            }

        if len(args) != len(func["params"]):
            raise Exception("Wrong parameters number!")

        for param, arg in zip(func["params"], args):
            if not isinstance(arg, type_map[param[1]]):
                raise Exception("Wrong parameter type!")
            
            var_type = param[1]
            var_name = param[0]
            decl_line = ctx.start.line

            local_memory.variables[var_name] = {"value": arg,
                                             "type": var_type,
                                             "decl_line": decl_line
                                             }

        try:
            interpreter = PseudoInterpreter(local_memory)
            listener = Listener(local_memory, interpreter)
            walker = ParseTreeWalker()
            tree = func["body"]

            walker.walk(listener, tree)
            interpreter.visit(tree)
            
        except ReturnException as ret:
            return ret.value
        except Exception as e:
            print(e)

    def visitFunctionCallStatement(self, ctx):
        name = ctx.ID().getText()
        if name not in self.memory.functions.keys():
            throw_non_defined_function_exception(ctx.start.line, ctx.start.column, ctx.name.text)
        
        args = []

        if ctx.argumentList():
            for expr_ctx in ctx.argumentList().expr():
                args.append(self.visit(expr_ctx))

        return self.call_function(name, args, ctx)
    
    def visitReturnStatement(self, ctx):
            value = self.visit(ctx.val)
            raise ReturnException(value)
    
    def visitFunctionDef(self, ctx):
        return None
    
    def visitIfStatement(self, ctx: PseudoParser.IfStatementContext):
        condition = self.visit(ctx.expr())
        if not isinstance(condition, bool):
            throw_wrong_type_exception(ctx.start.line, ctx.start.column, "boolean")
        if_body = ctx.body(0)
        else_body = ctx.body(1)  # Returns None if no else part exists
        if condition:
            for stmt in if_body.statement():
                self.visit(stmt)
        elif else_body is not None:
            for stmt in else_body.statement():
                self.visit(stmt)

    def visitWhileStatement(self, ctx: PseudoParser.WhileStatementContext):
        condition = self.visit(ctx.expr())
        if not isinstance(condition, bool):
            throw_wrong_type_exception(ctx.start.line, ctx.start.column, "boolean")
        while condition:
            for stmt in ctx.body().statement():
                self.visit(stmt)
            condition = self.visit(ctx.expr())
            
    def visitForStatement(self, ctx: PseudoParser.ForStatementContext):
        condition = self.visit(ctx.expr())
        if not isinstance(condition, bool):
            throw_wrong_type_exception(ctx.start.line, ctx.start.column, "boolean")
        while condition:
            for stmt in ctx.body().statement():
                self.visit(stmt)
            if ctx.assignmentStatement():
                self.visit(ctx.assignmentStatement())
            condition = self.visit(ctx.expr())

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

def run_interpreter(fileStream=None):
    try:
        inputStream = fileStream if fileStream else FileStream('program.pseudo', encoding='utf-8')
        lexer = PseudoLexer(inputStream)
        stream = CommonTokenStream(lexer)
        parser = PseudoParser(stream)
        
        parser.removeErrorListeners()
        parser.addErrorListener(SyntaxErrorListener())

        tree = parser.program()

        memory = Memory()

        interpreter = PseudoInterpreter(memory)
        listener = Listener(memory, interpreter)
        walker = ParseTreeWalker()
    
        walker.walk(listener, tree)
        interpreter.visit(tree)
    
    except Exception as e:
        print(e)
        return

run_interpreter()

# To code in Pseudo++, one must have file called "program.pseudo", and write its code in it.

# TODO
# ujemne liczby
# else if
# poprawnie działające funkcje xd