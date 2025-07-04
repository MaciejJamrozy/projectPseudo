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


    # Enter a parse tree produced by PseudoParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:PseudoParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:PseudoParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#ifStatement.
    def enterIfStatement(self, ctx:PseudoParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#ifStatement.
    def exitIfStatement(self, ctx:PseudoParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#whileStatement.
    def enterWhileStatement(self, ctx:PseudoParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#whileStatement.
    def exitWhileStatement(self, ctx:PseudoParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#forStatement.
    def enterForStatement(self, ctx:PseudoParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#forStatement.
    def exitForStatement(self, ctx:PseudoParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#initStatement.
    def enterInitStatement(self, ctx:PseudoParser.InitStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#initStatement.
    def exitInitStatement(self, ctx:PseudoParser.InitStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#breakStatement.
    def enterBreakStatement(self, ctx:PseudoParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#breakStatement.
    def exitBreakStatement(self, ctx:PseudoParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#continueStatement.
    def enterContinueStatement(self, ctx:PseudoParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#continueStatement.
    def exitContinueStatement(self, ctx:PseudoParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#functionDef.
    def enterFunctionDef(self, ctx:PseudoParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by PseudoParser#functionDef.
    def exitFunctionDef(self, ctx:PseudoParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by PseudoParser#returnStatement.
    def enterReturnStatement(self, ctx:PseudoParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#returnStatement.
    def exitReturnStatement(self, ctx:PseudoParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#paramList.
    def enterParamList(self, ctx:PseudoParser.ParamListContext):
        pass

    # Exit a parse tree produced by PseudoParser#paramList.
    def exitParamList(self, ctx:PseudoParser.ParamListContext):
        pass


    # Enter a parse tree produced by PseudoParser#param.
    def enterParam(self, ctx:PseudoParser.ParamContext):
        pass

    # Exit a parse tree produced by PseudoParser#param.
    def exitParam(self, ctx:PseudoParser.ParamContext):
        pass


    # Enter a parse tree produced by PseudoParser#functionCallStatement.
    def enterFunctionCallStatement(self, ctx:PseudoParser.FunctionCallStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#functionCallStatement.
    def exitFunctionCallStatement(self, ctx:PseudoParser.FunctionCallStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#argumentList.
    def enterArgumentList(self, ctx:PseudoParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by PseudoParser#argumentList.
    def exitArgumentList(self, ctx:PseudoParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by PseudoParser#codeBlock.
    def enterCodeBlock(self, ctx:PseudoParser.CodeBlockContext):
        pass

    # Exit a parse tree produced by PseudoParser#codeBlock.
    def exitCodeBlock(self, ctx:PseudoParser.CodeBlockContext):
        pass


    # Enter a parse tree produced by PseudoParser#body.
    def enterBody(self, ctx:PseudoParser.BodyContext):
        pass

    # Exit a parse tree produced by PseudoParser#body.
    def exitBody(self, ctx:PseudoParser.BodyContext):
        pass


    # Enter a parse tree produced by PseudoParser#varDeclStatement.
    def enterVarDeclStatement(self, ctx:PseudoParser.VarDeclStatementContext):
        pass

    # Exit a parse tree produced by PseudoParser#varDeclStatement.
    def exitVarDeclStatement(self, ctx:PseudoParser.VarDeclStatementContext):
        pass


    # Enter a parse tree produced by PseudoParser#expr.
    def enterExpr(self, ctx:PseudoParser.ExprContext):
        pass

    # Exit a parse tree produced by PseudoParser#expr.
    def exitExpr(self, ctx:PseudoParser.ExprContext):
        pass



del PseudoParser