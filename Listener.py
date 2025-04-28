# Name 'PseudoListener' was occupated so I called this class just 'Listener'
from PseudoListener import PseudoListener
from PseudoParser import PseudoParser
from PseudoVisitor import PseudoVisitor
from Memory import Memory
from PseudoExceptions import throw_var_redeclaration_exception


class Listener(PseudoListener):
    def __init__(self, memory: Memory):
        self.memory = memory

    def enterVarDeclStatement(self, ctx:PseudoParser.VarDeclStatementContext):
        var_id = ctx.ID().getText()

        if var_id in self.memory.variables.keys():
            throw_var_redeclaration_exception(ctx.start.line, ctx.start.column, var_id)
        else:
            self.memory.variables[var_id] = [ctx.expr().getText() if ctx.op else None, ctx.TYPE().getText()]
