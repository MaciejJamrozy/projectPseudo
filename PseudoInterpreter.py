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
import re
from PseudoExceptions import (
    throw_unsupported_operator_exception,
    throw_undefined_name_exception,
    throw_wrong_type_exception,
    throw_non_defined_function_exception,
    throw_non_redeclaration_in_function_def,
    throw_unknown_operator_exception,
    throw_conversion_exception,
    throw_var_redeclaration_exception,
)


class PseudoInterpreter(PseudoVisitor):
    def __init__(self, initialStackFrame: StackFrame, functions: Functions = None):
        self.inFunctionCall = False
        self.stack: Stack[StackFrame] = Stack()
        self.stack.push(initialStackFrame)
        self.functions = functions
        self.currentFrame: StackFrame = initialStackFrame

    def visitVarDeclStatement(self, ctx: PseudoParser.VarDeclStatementContext):
        var_id = ctx.ID().getText()
        var_type = ctx.TYPE().getText()
        decl_line = ctx.start.line
        is_global = ctx.global_ != None
        currentVariablesStoringObject = (
            self.currentFrame.globalVariables
            if is_global
            else self.currentFrame.localVariables
        )

        if self.currentFrame.localVariables.check_var(var_id) or self.currentFrame.globalVariables.check_var(var_id):
            throw_var_redeclaration_exception(
                ctx.start.line, ctx.start.column, var_id, decl_line
            )

        currentVariablesStoringObject.set_var(var_id, None, decl_line, var_type)

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
                    if not str(value) in ["True", "False"]:
                        raise ValueError
                    value = str(value) == "True"

                else:
                    throw_wrong_type_exception(
                        ctx.start.line, ctx.start.column, var_type
                    )
            except Exception as e:
                throw_wrong_type_exception(ctx.start.line, ctx.start.column, var_type)

            currentVariablesStoringObject.set_value(var_id, value)

    def get_nummeric_value(self, var: str):
        return float(var) if "." in var else int(var)

    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.expr())
        print(value)

    def visitExpr(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return self.visit(ctx.expr(0))

        if ctx.ID():
            var_id = ctx.ID().getText()
            if self.currentFrame.localVariables.check_var(var_id):
                return self.currentFrame.localVariables.get_var(var_id)["value"]
            elif self.currentFrame.globalVariables.check_var(var_id):
                return self.currentFrame.globalVariables.get_var(var_id)["value"]
            else:
                throw_undefined_name_exception(ctx.start.line, ctx.start.column, var_id)

        elif ctx.STRING():
            value = ctx.STRING().getText()[1:-1]
            return bytes(value, "utf-8").decode("unicode_escape")

        elif ctx.BOOL():
            value = ctx.BOOL().getText()
            return value == "True"

        elif ctx.NUMBER() or ctx.DOUBLE():
            return self.get_nummeric_value(ctx.getText())

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
                        ctx.start.line,
                        ctx.start.column,
                        parse_type,
                        type(value).__name__,
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

        elif ctx.op and ctx.op.type == PseudoParser.GREATEREQUAL:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, (int, float)) and isinstance(
                right_value, (int, float)
            ):
                return left_value >= right_value
            elif isinstance(left_value, str) and isinstance(right_value, str):
                return left_value >= right_value
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

        elif ctx.op and ctx.op.type == PseudoParser.SMALLEREQUAL:
            left_value = self.visit(ctx.expr(0))
            right_value = self.visit(ctx.expr(1))
            if isinstance(left_value, (int, float)) and isinstance(
                right_value, (int, float)
            ):
                return left_value <= right_value
            elif isinstance(left_value, str) and isinstance(right_value, str):
                return left_value <= right_value
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

    def visitAssignmentStatement(self, ctx):
        var_id = ctx.ID().getText()
        is_global = ctx.global_ != None
        currentVariablesStoringObject = (
            self.currentFrame.globalVariables
            if is_global
            else self.currentFrame.localVariables
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
                    if not str(value) in ["True", "False"]:
                        raise ValueError
                    value = str(value) == "True"

                else:
                    throw_wrong_type_exception(
                        ctx.start.line, ctx.start.column, var_type
                    )

            except Exception:
                throw_wrong_type_exception(ctx.start.line, ctx.start.column, var_type)

            currentVariablesStoringObject.set_value(var_id, value)

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
        condition = self.visit(ctx.expr())
        if not isinstance(condition, bool):
            throw_wrong_type_exception(ctx.start.line, ctx.start.column, "boolean")

        listener = Listener(self.currentFrame, self, functions=self.functions)
        walker = ParseTreeWalker()

        while condition:
            walker.walk(listener, ctx.body())

            try:
                self.visit(ctx.body())
            except ContinueException:
                continue
            except BreakException:
                break

            condition = self.visit(ctx.expr())

    def visitForStatement(self, ctx: PseudoParser.ForStatementContext):
        if ctx.varDeclStatement():
            self.visit(ctx.varDeclStatement())

        condition = self.visit(ctx.expr()) if ctx.expr() else True

        listener = Listener(self.currentFrame, self, functions=self.functions)
        walker = ParseTreeWalker()

        while condition:
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

            condition = self.visit(ctx.expr()) if ctx.expr() else True

        if ctx.varDeclStatement():
            self.currentFrame.localVariables.del_var(
                ctx.varDeclStatement().ID().getText()
            )

    def visitFunctionCallStatement(
        self, ctx: PseudoParser.FunctionCallStatementContext
    ):
        name = ctx.ID().getText()

        if not self.functions.check_fun(name):
            throw_non_defined_function_exception(ctx.start.line, ctx.start.column, name)

        args = []
        if ctx.argumentList():
            for expr_ctx in ctx.argumentList().expr():
                args.append(self.visit(expr_ctx))
        try:
            newStackFrame = self.currentFrame.geniusCopy()
            newStackFrame.returnAddress = self.currentFrame
            self.stack.push(newStackFrame)
            self.currentFrame = self.stack.peek()
            self.call_function(name, args, ctx)
        except ReturnException as ret:
            if self.functions.get_fun(name)['return_type'] == 'void':
                raise Exception('Error: Void functions cannot return values.')
            return ret.value
        except Exception as e:
            raise
        finally:
            self.stack.pop()
            self.currentFrame = self.stack.peek()

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
            if not isinstance(arg, types_map[var_type]):
                raise Exception("Error: Wrong parameter type!")

            decl_line = ctx.start.line
            if self.currentFrame.localVariables.check_var(var_name):
                decl_line = func["decl_line"]
                throw_non_redeclaration_in_function_def(
                    ctx.start.line, ctx.start.column, var_name, decl_line
                )
            else:
                self.currentFrame.localVariables.set_var(
                    var_name, arg, decl_line, var_type
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


def run_interpreter(inputStream=None):
    try:
        inputStream = (
            inputStream
            if inputStream
            else FileStream("program.pseudo", encoding="utf-8")
        )
        lexer = PseudoLexer(inputStream)
        stream = CommonTokenStream(lexer)
        parser = PseudoParser(stream)

        parser.removeErrorListeners()
        parser.addErrorListener(SyntaxErrorListener())

        tree = parser.program()

        initialStackFrame = StackFrame(
            globalVariables=Variables(),
        )

        functions = Functions()

        interpreter = PseudoInterpreter(
            initialStackFrame=initialStackFrame, functions=functions
        )
        listener = Listener(initialStackFrame, interpreter, functions=functions)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        interpreter.visit(tree)

    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    run_interpreter()

# TODO
# Zrobić porządek w gramatyce - Maciek
# Zaawansowana diagnostyka błędów
# Rzutowanie typów - Robert
# Napisanie dokumentacji - Kacper

# dodatkowe TODO, fajne rzeczy nietrudne do zrobienia:
# dopracowanie języka: obsługa skróconych operatorów '+=', '-+' '*=' ...
# dodanie moliwości pisania pętli while bez nawiasów okrągłych "while 1==1: ..."
# Importy (zeby dało się zrobić: "import anotherProgram.pseudo"
# Biblioteka standardowa języka, z podstawowymi funkcjami typu: sqrt, time
# REPL (Read-Eval-Print Loop) - bardzo ciekawa rzecz ale nie wiem jak trudna - Interaktywny tryb działania interpretera – użytkownik wpisuje linijki kodu i otrzymuje natychmiastowy wynik.

# trudne (ale fajne), dodatkowe TODO:
# Listy / tablice: z operacjami indeksowania, długości, dodawania/uzupełniania.
