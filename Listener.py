from PseudoListener import PseudoListener
from PseudoVisitor import PseudoVisitor
from PseudoParser import PseudoParser
from StackFrame import StackFrame
from Functions import Functions
import re
from PseudoExceptions import (
    throw_redeclaration_in_function_def_exception,
    throw_redeclaration_in_function_def_exception,
    throw_function_redeclaration_exception
)


class Listener(PseudoListener):
    def __init__(self, stackFrame: StackFrame, visitor: PseudoVisitor, functions: Functions=None):
        self.currentFrame = stackFrame
        self.visitor = visitor
        self.inFunctionDef = False
        self.functions = functions

    def enterFunctionDef(self, ctx):
        if self.inFunctionDef:
            return
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