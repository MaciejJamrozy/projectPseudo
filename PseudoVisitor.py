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


    # Visit a parse tree produced by PseudoParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:PseudoParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#ifStatement.
    def visitIfStatement(self, ctx:PseudoParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#whileStatement.
    def visitWhileStatement(self, ctx:PseudoParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#forStatement.
    def visitForStatement(self, ctx:PseudoParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#initStatement.
    def visitInitStatement(self, ctx:PseudoParser.InitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#breakStatement.
    def visitBreakStatement(self, ctx:PseudoParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#continueStatement.
    def visitContinueStatement(self, ctx:PseudoParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#functionDef.
    def visitFunctionDef(self, ctx:PseudoParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#returnStatement.
    def visitReturnStatement(self, ctx:PseudoParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#paramList.
    def visitParamList(self, ctx:PseudoParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#param.
    def visitParam(self, ctx:PseudoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#functionCallStatement.
    def visitFunctionCallStatement(self, ctx:PseudoParser.FunctionCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#argumentList.
    def visitArgumentList(self, ctx:PseudoParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#codeBlock.
    def visitCodeBlock(self, ctx:PseudoParser.CodeBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#body.
    def visitBody(self, ctx:PseudoParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#varDeclStatement.
    def visitVarDeclStatement(self, ctx:PseudoParser.VarDeclStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudoParser#expr.
    def visitExpr(self, ctx:PseudoParser.ExprContext):
        return self.visitChildren(ctx)



del PseudoParser