from antlr4 import *
from PseudoVisitor import PseudoVisitor
from PseudoLexer import PseudoLexer
from PseudoParser import PseudoParser
from SyntaxErrorListener import SyntaxErrorListener
from Listener import Listener
from Memory import Memory
from Functions import Functions
from PseudoExceptions import (
    throw_unsupported_operator_exception,
    throw_undefined_name_exception,
    throw_wrong_type_exception,
    throw_non_defined_function_exception,
    throw_non_redeclaration_in_function_def,throw_var_redeclaration_exception,
    throw_unknown_operator_exception,
    throw_no_parent_scope_exception,
    throw_conversion_exception
)
import re
import random


class PseudoInterpreter(PseudoVisitor):
    def __init__(self, memory: Memory, functions: Functions):
        self.memory = memory
        self.functions = functions
        self.inFunctionCall = False
    
    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.expr())
        print(value)

    def get_nummeric_value(self, var: str):
        return float(var) if "." in var else int(var)

    def visitExpr(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return self.visit(ctx.expr(0))

        if ctx.ID():
            var_id = ctx.ID().getText()
            if self.memory.check_var(var_id) is False:
                throw_undefined_name_exception(ctx.start.line, ctx.start.column, var_id)
            else:
                return self.memory.get_var(var_id)["value"]

        elif ctx.STRING():
            value = ctx.STRING().getText()[1:-1]
            return bytes(value, "utf-8").decode("unicode_escape")

        elif ctx.BOOL():
            value = ctx.BOOL().getText()
            return value == "true"

        elif ctx.NUMBER() or ctx.DOUBLE():
            return self.get_nummeric_value(ctx.getText())
        
        elif ctx.op and ctx.op.type == PseudoParser.PARENT:
            if self.memory.parent:
                current_mem = self.memory
                self.memory = self.memory.parent
                val = self.visit(ctx.expr(0))
                self.memory = current_mem
                return val
            else:
                throw_no_parent_scope_exception(ctx.start.line, ctx.start.column)

        elif ctx.op and ctx.op.type == PseudoParser.TYPE:
            parse_type = ctx.TYPE().getText()
            if ctx.expr(0):
                value = self.visit(ctx.expr(0))
                try:
                    if parse_type == "int":
                        return int(value)
                    elif parse_type == "float":
                        return float(value)
                    elif parse_type == "string":
                        return str(value)
                    elif parse_type == "boolean":
                        return bool(value)
                except Exception as e:
                    throw_conversion_exception(
                        ctx.start.line, ctx.start.column, parse_type, type(value).__name__
                    )

        elif ctx.op and ctx.op.type == PseudoParser.PLUS:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))

            match (left_value, right_value):
                case (str(), str()):
                    return left_value + right_value
                case (int() | float(), int() | float()):
                    return left_value + right_value
                case _:
                    throw_unsupported_operator_exception(
                        ctx.start.line,
                        ctx.start.column,
                        ctx.op.text,
                        type(left_value).__name__,
                        type(right_value).__name__,
                    )

        elif ctx.op and ctx.op.type == PseudoParser.MINUS:
            left_value = self.visit(ctx.expr(0))
            if not (ctx.expr(1) is None):
                right_value = self.visit(ctx.expr(1))

                if not (isinstance(left_value, str) or isinstance(right_value, str)):
                    return left_value - right_value
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
                return -left_value

        elif ctx.op and ctx.op.type == PseudoParser.MULT:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if not (isinstance(left_value, str) and isinstance(right_value, str)):
                return left_value * right_value
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__,
                )

        elif ctx.op and ctx.op.type == PseudoParser.DIV:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))

            if not (isinstance(left_value, str) or isinstance(right_value, str)):
                if abs(right_value) < 1e-9:
                    raise Exception("Cannot divide by zero")
                return left_value / right_value
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__,
                )

        elif ctx.op and ctx.op.type == PseudoParser.INTDIV:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))

            if not (isinstance(left_value, str) or isinstance(right_value, str)):
                if abs(right_value) < 1e-9:
                    raise Exception("Cannot divide by zero")
                return left_value // right_value
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__,
                )

        elif ctx.op and ctx.op.type == PseudoParser.AND:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, bool) and isinstance(right_value, bool):
                return left_value and right_value
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value.__name__, type(right_value).__name__),
                )

        elif ctx.op and ctx.op.type == PseudoParser.OR:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, bool) and isinstance(right_value, bool):
                return left_value or right_value
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value.__name__, type(right_value).__name__),
                )

        elif ctx.op and ctx.op.type == PseudoParser.NOT:
            value = self.visit(ctx.expr(0))
            if isinstance(value, bool):
                return not value
            else:
                raise Exception(
                    f"Error in line: {ctx.start.line}, column: {ctx.start.column}: this value is not boolean."
                )

        elif ctx.op and ctx.op.type == PseudoParser.GREATER:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, (int, float)) and isinstance(
                right_value, (int, float)
            ):
                return left_value > right_value
            elif isinstance(left_value, str) and isinstance(right_value, str):
                return left_value > right_value
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__,
                )

        elif ctx.op and ctx.op.type == PseudoParser.SMALLER:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, (int, float)) and isinstance(
                right_value, (int, float)
            ):
                return left_value < right_value
            elif isinstance(left_value, str) and isinstance(right_value, str):
                return left_value < right_value
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__,
                )

        elif ctx.op and ctx.op.type == PseudoParser.EQUAL:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, (int, float)) and isinstance(
                right_value, (int, float)
            ):
                return left_value == right_value
            elif isinstance(left_value, str) and isinstance(right_value, str):
                return left_value == right_value
            else:
                throw_unsupported_operator_exception(
                    ctx.start.line,
                    ctx.start.column,
                    ctx.op.text,
                    type(left_value).__name__,
                    type(right_value).__name__,
                )

        elif ctx.op and ctx.op.type == PseudoParser.DIFFERENT:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            return left_value != right_value

        else:
            return self.visitChildren(ctx)

    def visitVarDeclStatement(self, ctx):
        var_id = ctx.ID().getText()
        var_type = ctx.TYPE().getText()
        decl_line = ctx.start.line
        if self.inFunctionCall:
            if var_id in self.memory.variables.keys():
                decl_line = self.memory.variables[var_id]["decl_line"]
                throw_var_redeclaration_exception(ctx.start.line, ctx.start.column, var_id, decl_line)
            else:
                self.memory.set_var(var_id, None, decl_line, var_type)
        if ctx.op:
            value = self.visit(ctx.expr())
            try:
                if var_type == "string":
                    if not re.fullmatch(r'(?:\\.|(?!(["\'])).)*', str(value)):
                        raise ValueError

                elif var_type == "int":
                    if not re.fullmatch(r"-?\d+\.?\d*", str(value)):
                        raise ValueError
                    value = int(value)

                elif var_type == "float":
                    if not re.fullmatch(r"-?\d+\.?\d*", str(value)):
                        raise ValueError
                    value = float(value)

                elif var_type == "boolean":
                    if not value.lower() in ["true", "false"]:
                        raise ValueError
                    value = value.lower() == "true"

                else:
                    throw_wrong_type_exception(
                        ctx.start.line, ctx.start.column, var_type
                    )
            except Exception as e:
                throw_wrong_type_exception(ctx.start.line, ctx.start.column, var_type)
            if self.memory.check_var(var_id):
                self.memory.set_value(var_id, value)

    def visitAssignmentStatement(self, ctx):
        var_id = ctx.ID().getText()
        var_type = self.memory.get_var(var_id)["type"]
        if ctx.op and ctx.op.type == PseudoParser.INCREMENT:
            val = self.memory.get_var(var_id)["value"]
            if isinstance(val, int):
                self.memory.set_value(var_id, val + 1)
            elif isinstance(val, float):
                self.memory.set_value(var_id, val + 1.0)
            else:
                throw_wrong_type_exception(
                    ctx.start.line, ctx.start.column, type(val).__name__
                )
        elif ctx.op and ctx.op.type == PseudoParser.DECREMENT:
            val = self.memory.get_var(var_id)["value"]
            if isinstance(val, int):
                self.memory.set_value(var_id, val - 1)
            elif isinstance(val, float):
                self.memory.set_value(var_id, val - 1.0)
            else:
                throw_unknown_operator_exception(
                    ctx.start.line, ctx.start.column, ctx.op.text
                )
        else:
            value = self.visit(ctx.expr())
            if self.memory.check_var(var_id) is False:
                throw_undefined_name_exception(ctx.start.line, ctx.start.column, var_id)

            try:
                if var_type == "string":
                    if not re.fullmatch(r'(?:\\.|(?!(["\'])).)*', str(value)):
                        raise ValueError
                elif var_type == "int":
                    if not bool(re.fullmatch(r"-?\d+\.?\d*", str(value))):
                        raise ValueError
                    value = int(value)

                elif var_type == "float":
                    if not re.fullmatch(r"-?\d+\.?\d*", str(value)):
                        raise ValueError
                    value = float(value)

                elif var_type == "boolean":
                    if not value.lower() in ["true", "false"]:
                        raise ValueError
                    value = value.lower() == "true"

                else:
                    throw_wrong_type_exception(
                        ctx.start.line, ctx.start.column, var_type
                    )

            except Exception:
                throw_wrong_type_exception(ctx.start.line, ctx.start.column, var_type)

            self.memory.set_value(var_id, value)

    def call_function(self, name, args, ctx):
        func = self.functions.functions[name]

        type_map = {
            "int": int,
            "float": float,
            "string": str,
            "boolean": bool,
            "void": type(None),
        }

        if len(args) != len(func["params"]):
            raise Exception("Wrong parameters number!")

        for param, arg in zip(func["params"], args):

            var_name = param
            var_type = func["params"][var_name]
            if not isinstance(arg, type_map[var_type]):
                raise Exception("Wrong parameter type!")

            decl_line = ctx.start.line
            if var_name in self.memory.variables.keys():
                decl_line = func["decl_line"]
                throw_non_redeclaration_in_function_def(
                    ctx.start.line, ctx.start.column, var_name, decl_line
                )
            else:
                self.memory.set_var(var_name, arg, decl_line, var_type)

        for stmt in func["body"].statement():
            self.visit(stmt)

    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.val)
        raise ReturnException(value)

    def visitFunctionDef(self, ctx):
        return None

    def visitIfStatement(self, ctx: PseudoParser.IfStatementContext):
        if self.visit(ctx.expr(0)):
            for stmt in ctx.body(0).statement():
                self.visit(stmt)
            return

        num_elseif = len(ctx.expr()) - 1
        for i in range(num_elseif):
            if self.visit(ctx.expr(i + 1)):
                for stmt in ctx.body(i + 1).statement():
                    self.visit(stmt)
                return

        if ctx.body(num_elseif + 1) is not None:
            for stmt in ctx.body(num_elseif + 1).statement():
                self.visit(stmt)

    def visitWhileStatement(self, ctx: PseudoParser.WhileStatementContext):
        if self.inFunctionCall:
            new_scope = Memory(name=f"while_function_scope_line_{ctx.start.line}_{random.randint(0, 1000)}")
            self.memory.add_child(new_scope)
            self.memory = new_scope
        else:
            self.memory = self.memory.get_child(f"while_scope_line_{ctx.start.line}")
        condition = self.visit(ctx.expr())
        if not isinstance(condition, bool):
            throw_wrong_type_exception(ctx.start.line, ctx.start.column, "boolean")
        while condition:
            for stmt in ctx.body().statement():
                self.visit(stmt)
            condition = self.visit(ctx.expr())
        self.memory = self.memory.parent

    def visitForStatement(self, ctx: PseudoParser.ForStatementContext):
        if self.inFunctionCall:
            new_scope = Memory(name=f"for_function_scope_line_{ctx.start.line}_{random.randint(0, 1000)}")
            self.memory.add_child(new_scope)
            self.memory = new_scope
            if ctx.varDeclStatement():
                self.visitVarDeclStatement(ctx.varDeclStatement())
        else:
            self.memory = self.memory.get_child(f"for_scope_line_{ctx.start.line}")
            if ctx.varDeclStatement():
                self.visitAssignmentStatement(ctx.varDeclStatement())

        condition = self.visit(ctx.expr())
        while condition:
            if not isinstance(condition, bool):
                throw_wrong_type_exception(ctx.start.line, ctx.start.column, "boolean")
            if ctx.body():
                for statement in ctx.body().statement():
                    self.visit(statement)
            if ctx.assignmentStatement():
                self.visit(ctx.assignmentStatement())
            condition = self.visit(ctx.expr())
        self.memory = self.memory.parent

    def visitFunctionCallStatement(self, ctx: PseudoParser.FunctionCallStatementContext):
        self.inFunctionCall = True
        fun_name = ctx.ID().getText()

        if not self.functions.get_fun(fun_name):
            throw_non_defined_function_exception(
                ctx.start.line, ctx.start.column, fun_name
            )
        self.functions.call_fun(fun_name)

        func = self.functions.get_fun(fun_name)

        new_scope = Memory(name=f"function_scope_line_{fun_name}_call_{func["num_called"]}")
        self.memory.add_child(new_scope)
        self.memory = new_scope

        name = fun_name
        if name not in self.functions.functions.keys():
            throw_non_defined_function_exception(
                ctx.start.line, ctx.start.column, ctx.name.text
            )
        args = []
        if ctx.argumentList():
            for expr_ctx in ctx.argumentList().expr():
                args.append(self.visit(expr_ctx))
        try:
            self.call_function(name, args, ctx)
            self.memory = self.memory.parent
            self.inFunctionCall = False
        except ReturnException as ret:
            self.memory = self.memory.parent
            self.inFunctionCall = False
            return ret.value


class ReturnException(Exception):
    def __init__(self, value):
        self.value = value


def run_interpreter(inputStream=None):
    try:
        inputStream = (
            inputStream if inputStream else FileStream("program.pseudo", encoding="utf-8")
        )
        lexer = PseudoLexer(inputStream)
        stream = CommonTokenStream(lexer)
        parser = PseudoParser(stream)

        parser.removeErrorListeners()
        parser.addErrorListener(SyntaxErrorListener())

        tree = parser.program()

        memory = Memory()
        functions = Functions()
        interpreter = PseudoInterpreter(memory, functions)
        listener = Listener(memory, interpreter, functions)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        interpreter.visit(tree)

    except Exception as e:
        print(e)
        return


run_interpreter()

# TODO
# Zarządzanie pamięcią, stos - Maciek
# Zrobienie testów - Maciek
# Zrobić porządek w gramatyce - Maciek
# Zaawansowana diagnostyka błędów
# Rzutowanie typów - Robert
# Napisanie dokumentacji - Kacper
# Dorobić operatory: ">=" "<="

# dodatkowe TODO, fajne rzeczy nietrudne do zrobienia:
# dopracowanie języka: obsługa skróconych operatorów '+=', '-+' '*=' ...
# dodanie moliwości pisania pętli while bez nawiasów okrągłych "while 1==1: ..."
# Importy (zeby dało się zrobić: "import anotherProgram.pseudo"
# Biblioteka standardowa języka, z podstawowymi funkcjami typu: sqrt, time
# REPL (Read-Eval-Print Loop) - bardzo ciekawa rzecz ale nie wiem jak trudna - Interaktywny tryb działania interpretera – użytkownik wpisuje linijki kodu i otrzymuje natychmiastowy wynik.

# trudne (ale fajne), dodatkowe TODO:
# Listy / tablice: z operacjami indeksowania, długości, dodawania/uzupełniania.
