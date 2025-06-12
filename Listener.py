from PseudoListener import PseudoListener
from PseudoVisitor import PseudoVisitor
from StackFrame import StackFrame
from Functions import Functions
from PseudoExceptions import (
    throw_redeclaration_in_function_def_exception,
    throw_redeclaration_in_function_def_exception,
    throw_function_redeclaration_exception,
    throw_fun_def_in_loop_exception,
    throw_fun_def_in_if_else_block_exception,
    throw_fun_def_in_block_exception
)


class Listener(PseudoListener):
    def __init__(self, stackFrame: StackFrame, visitor: PseudoVisitor, functions: Functions=None):
        self.currentFrame = stackFrame
        self.visitor = visitor
        self.functions = functions
        self.inFunctionDef = False
        self.inCodeBlock = False
        self.inLoop = False
        self.inIfElseBlock = False

    def enterFunctionDef(self, ctx):
        if self.inFunctionDef:
            return
        if self.inCodeBlock:
            throw_fun_def_in_block_exception(ctx.start.line, ctx.start.column)
        if self.inIfElseBlock:
            throw_fun_def_in_if_else_block_exception(ctx.start.line, ctx.start.column)
        if self.inLoop:
            throw_fun_def_in_loop_exception(ctx.start.line, ctx.start.column)
        self.inFunctionDef = True
        name = ctx.name.text
        return_type = ctx.type_.text
        body = ctx.block

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
                    throw_redeclaration_in_function_def_exception(
                        ctx.start.line, column, param_name, ctx.start.line
                    )
                else:
                    params[param_name] = param_type

        self.functions.set_fun(
            name, return_type, params, body, ctx.start.line
        )

    def exitFunctionDef(self, ctx):
        self.inFunctionDef = False

    def enterCodeBlock(self, ctx):
        self.inCodeBlock = True

    def exitCodeBlock(self, ctx):
        self.inCodeBlock = False

    def enterIfStatement(self, ctx):
        self.inIfElseBlock = True
    
    def exitIfStatement(self, ctx):
        self.inIfElseBlock = False

    def enterForStatement(self, ctx):
        self.inLoop = True

    def exitForStatement(self, ctx):
        self.inLoop = False

    def enterWhileStatement(self, ctx):
        self.inLoop = True

    def exitWhileStatement(self, ctx):
        self.inLoop = False
