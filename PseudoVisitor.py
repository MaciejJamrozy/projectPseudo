# Generated from Pseudo.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PseudoParser import PseudoParser
else:
    from PseudoParser import PseudoParser

# This class defines a complete generic visitor for a parse tree produced by PseudoParser.

class PseudoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PseudoParser#program.
    def visitProgram(self, ctx:PseudoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#statement.
    def visitStatement(self, ctx:PseudoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#printStatement.
    def visitPrintStatement(self, ctx:PseudoParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#assignStatement.
    def visitAssignStatement(self, ctx:PseudoParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#expr.
    def visitExpr(self, ctx:PseudoParser.ExprContext):
        return self.visitChildren(ctx)



del PseudoParser