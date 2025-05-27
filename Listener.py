# Name 'PseudoListener' was occupated so I called this class just 'Listener' ~ Maciek
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
        self.inFunctionDef = False

    def enterFunctionDef(self, ctx):
        self.inFunctionDef = True
        name = ctx.name.text
        return_type = ctx.type_.text
        body = ctx.block

        params = []
        if ctx.paramList():
            for param_ctx in ctx.paramList().param():
                param_type = param_ctx.TYPE().getText()
                param_name = param_ctx.ID().getText()
                params.append((param_name, param_type))

        self.memory.functions[name] = {"return_type": return_type,
                                       "params": params,
                                       "body": body
                                       }
        
    def exitFunctionDef(self, ctx):
        self.inFunctionDef = False


    def enterVarDeclStatement(self, ctx:PseudoParser.VarDeclStatementContext):
        if self.inFunctionDef:
            return
        else:
            var_id = ctx.ID().getText()
            var_type = ctx.TYPE().getText()
            decl_line = ctx.start.line

            if var_id in self.memory.variables.keys():
                decl_line = self.memory.variables[var_id]["decl_line"]
                throw_var_redeclaration_exception(ctx.start.line, ctx.start.column, var_id, decl_line)
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

                self.memory.variables[var_id] = {"value": value,
                                                "type": var_type,
                                                "decl_line": decl_line
                                                }
            else:
                self.memory.variables[var_id] = {"value": None,
                                                "type": var_type,
                                                "decl_line": decl_line
                                                }
            