from antlr4 import *
from PseudoVisitor import PseudoVisitor
from PseudoLexer import PseudoLexer
from PseudoParser import PseudoParser
from SyntaxErrorListener import SyntaxErrorListener
from Listener import Listener
from Memory import Memory
from PseudoExceptions import throw_unknown_operator_exception, throw_undefined_name_exception, throw_wrong_type_exception
import re

class PseudoInterpreter(PseudoVisitor):
    def __init__(self, memory: Memory):
        self.memory = memory
    
    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        
    def get_nummeric_value(self, var: str):
        return float(var) if '.' in var else int(var)
    
    def visitExpr(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expr(0))
        
        if ctx.ID():
            var_id = ctx.ID().getText()
            if var_id not in self.memory.variables.keys():
                throw_undefined_name_exception(ctx.start.line, ctx.start.column, var_id)
            else:
                return self.memory.variables[var_id][0]

        elif ctx.STRING():
            value = ctx.STRING().getText()[1:-1]  # Usuwanie cudzysłowów
            return bytes(value, "utf-8").decode("unicode_escape")
        
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
            right_value = self.visit(ctx.expr(1))

            if not (isinstance(left_value, str) or isinstance(right_value, str)):
                return left_value - right_value
            else:
                throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value).__name__, type(right_value).__name__)
        
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
                throw_unknown_operator_exception(ctx.start.line, ctx.start.column, ctx.op.text, type(left_value.__name__, type(right_value).__name__))

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
        
    def visitAssignmentStatement(self, ctx:PseudoParser.AssignmentStatementContext):
        var_id = ctx.ID().getText()
        var_type = self.memory.variables[var_id][1]
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
            print(value)
            throw_wrong_type_exception(ctx.start.line, ctx.start.column, var_type)
        
        self.memory.variables[var_id][0] = value

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
        if ctx.varDeclStatement():
            self.visit(ctx.varDeclStatement())
        condition = self.visit(ctx.expr())
        if not isinstance(condition, bool):
            throw_wrong_type_exception(ctx.start.line, ctx.start.column, "boolean")
        while condition:
            for stmt in ctx.body().statement():
                self.visit(stmt)
            if ctx.assignmentStatement():
                self.visit(ctx.assignmentStatement())
            condition = self.visit(ctx.expr())

def run_interpreter(input_text):
    lexer = PseudoLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = PseudoParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(SyntaxErrorListener())

    tree = parser.program()

    memory = Memory() # class used for managing variables (it contains dict for variables)

    interpreter = PseudoInterpreter(memory)
    listener = Listener(memory, interpreter)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    interpreter.visit(tree)

# Run interpreter
try:
    with open("program.pseudo", "r", encoding="utf-8") as f:
        code = f.read()
        run_interpreter(code)
except Exception as e:
    print(e)