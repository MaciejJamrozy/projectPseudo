# Generated from Pseudo.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PseudoParser import PseudoParser
else:
    from PseudoParser import PseudoParser

# This class defines a complete listener for a parse tree produced by PseudoParser.
class PseudoListener(ParseTreeListener):

    # Enter a parse tree produced by PseudoParser#program.
    def enterProgram(self, ctx:PseudoParser.ProgramContext):
        pass

    # Exit a parse tree produced by PseudoParser#program.
    def exitProgram(self, ctx:PseudoParser.ProgramContext):
        pass


    # Enter a parse tree produced by PseudoParser#statement.
    def enterStatement(self, ctx:PseudoParser.StatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#statement.
    def exitStatement(self, ctx:PseudoParser.StatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#printStatement.
    def enterPrintStatement(self, ctx:PseudoParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#printStatement.
    def exitPrintStatement(self, ctx:PseudoParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#assignStatement.
    def enterAssignStatement(self, ctx:PseudoParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#assignStatement.
    def exitAssignStatement(self, ctx:PseudoParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#expr.
    def enterExpr(self, ctx:PseudoParser.ExprContext):
        pass

    # Exit a parse tree produced by PseudoParser#expr.
    def exitExpr(self, ctx:PseudoParser.ExprContext):
        pass



del PseudoParser