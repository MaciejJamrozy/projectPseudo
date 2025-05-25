# Name 'PseudoListener' was occupated so I called this class just 'Listener'
from PseudoListener import PseudoListener
from PseudoParser import PseudoParser
from PseudoVisitor import PseudoVisitor
from Memory import Memory
from PseudoExceptions import throw_var_redeclaration_exception, throw_wrong_type_exception
import re

class Listener(PseudoListener):
    def __init__(self, memory: Memory, visitor: PseudoVisitor):
        self.memory = memory
        self.visitor = visitor


    def enterVarDeclStatement(self, ctx:PseudoParser.VarDeclStatementContext):
        var_id = ctx.ID().getText()
        var_type = ctx.TYPE().getText()

        if var_id in self.memory.variables.keys():
            throw_var_redeclaration_exception(ctx.start.line, ctx.start.column, var_id)
        elif ctx.op:
            value = str(self.visitor.visit(ctx.expr()))
            try:
                if var_type == 'string':
                    if not re.fullmatch(r'(?:\\.|(?!(["\'])).)*', value):
                        print(type(value))
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
            except Exception as e:
                throw_wrong_type_exception(ctx.start.line, ctx.start.column, var_type)

            self.memory.variables[var_id] = [value, var_type]
        else:
            self.memory.variables[var_id] = [None, var_type]
