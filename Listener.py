# Name 'PseudoListener' was occupated so I called this class just 'Listener' ~ Maciek
from PseudoListener import PseudoListener
from PseudoParser import PseudoParser
from PseudoVisitor import PseudoVisitor
from Memory import Memory
from Functions import Functions
from PseudoExceptions import throw_var_redeclaration_exception, throw_wrong_type_exception,throw_non_redeclaration_in_function_def,throw_non_defined_function_exception
import re

class Listener(PseudoListener):
    def __init__(self, memory: Memory, visitor: PseudoVisitor, functions: Functions):
        self.memory = memory
        self.visitor = visitor
        self.functions = functions
        self.inFunctionDef = False



    def enterFunctionDef(self, ctx):
        self.inFunctionDef = True
        name = ctx.name.text
        return_type = ctx.type_.text
        body = ctx.block

        params = {}
        if ctx.paramList():
            for param_ctx in ctx.paramList().param():
                param_type = param_ctx.TYPE().getText()
                param_name = param_ctx.ID().getText()
                if(param_name in params.keys()):
                    throw_non_redeclaration_in_function_def(ctx.start.line, ctx.start.column, param_name, ctx.start.line)
                else:
                    params[param_name] =  param_type

        self.functions.set_fun(name, return_type, params, body, ctx.start.line)
        
    def exitFunctionDef(self, ctx):
        self.inFunctionDef = False

    def enterVarDeclStatement(self, ctx:PseudoParser.VarDeclStatementContext):
        if self.inFunctionDef:
            return
        else:
            var_id = ctx.ID().getText()
            var_type = ctx.TYPE().getText()
            decl_line = ctx.start.line
            if self.memory.check_var(var_id):
                decl_line = self.memory.variables[var_id]["decl_line"]
                throw_var_redeclaration_exception(ctx.start.line, ctx.start.column, var_id, decl_line)
            else:
                self.memory.set_var(var_id, None, decl_line, var_type)
    def enterForStatement(self, ctx: PseudoParser.ForStatementContext):
        new_scope = Memory(name=f"for_scope_line_{ctx.start.line}")
        self.memory.add_child(new_scope)
        self.memory = new_scope
        

    def exitForStatement(self, ctx: PseudoParser.ForStatementContext):
        self.memory = self.memory.parent
                