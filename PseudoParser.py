# Generated from Pseudo.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,236,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,47,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,
        3,58,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        73,8,5,1,5,1,5,3,5,77,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,86,8,5,
        1,5,1,5,3,5,90,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,101,8,
        5,1,5,1,5,3,5,105,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,114,8,5,1,
        5,1,5,3,5,118,8,5,3,5,120,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,130,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,3,7,147,8,7,1,8,1,8,1,8,1,8,3,8,153,8,8,1,8,1,8,1,8,1,8,1,
        8,3,8,160,8,8,1,9,1,9,1,9,1,9,1,9,5,9,167,8,9,10,9,12,9,170,9,9,
        1,10,1,10,1,10,3,10,175,8,10,1,10,1,10,1,11,1,11,1,11,5,11,182,8,
        11,10,11,12,11,185,9,11,1,12,1,12,1,12,5,12,190,8,12,10,12,12,12,
        193,9,12,1,13,1,13,1,13,1,13,3,13,199,8,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,214,8,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,5,13,231,8,13,10,13,12,13,234,9,13,1,13,0,1,26,14,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,0,7,1,0,2,3,1,0,6,9,1,0,40,41,1,0,20,22,
        1,0,30,31,1,0,28,29,1,0,32,35,263,0,33,1,0,0,0,2,46,1,0,0,0,4,48,
        1,0,0,0,6,53,1,0,0,0,8,59,1,0,0,0,10,119,1,0,0,0,12,121,1,0,0,0,
        14,131,1,0,0,0,16,148,1,0,0,0,18,161,1,0,0,0,20,171,1,0,0,0,22,178,
        1,0,0,0,24,191,1,0,0,0,26,213,1,0,0,0,28,29,3,2,1,0,29,30,5,1,0,
        0,30,32,1,0,0,0,31,28,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,
        1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,37,5,0,0,1,37,1,1,0,0,0,38,
        47,3,4,2,0,39,47,3,6,3,0,40,47,3,8,4,0,41,47,3,10,5,0,42,47,3,12,
        6,0,43,47,3,14,7,0,44,47,3,16,8,0,45,47,3,20,10,0,46,38,1,0,0,0,
        46,39,1,0,0,0,46,40,1,0,0,0,46,41,1,0,0,0,46,42,1,0,0,0,46,43,1,
        0,0,0,46,44,1,0,0,0,46,45,1,0,0,0,47,3,1,0,0,0,48,49,7,0,0,0,49,
        50,5,4,0,0,50,51,3,26,13,0,51,52,5,5,0,0,52,5,1,0,0,0,53,54,5,39,
        0,0,54,57,5,44,0,0,55,56,7,1,0,0,56,58,3,26,13,0,57,55,1,0,0,0,57,
        58,1,0,0,0,58,7,1,0,0,0,59,60,5,44,0,0,60,61,7,1,0,0,61,62,3,26,
        13,0,62,9,1,0,0,0,63,64,5,10,0,0,64,65,5,4,0,0,65,66,3,26,13,0,66,
        67,5,5,0,0,67,68,5,11,0,0,68,72,3,24,12,0,69,70,5,12,0,0,70,71,5,
        11,0,0,71,73,3,24,12,0,72,69,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,
        74,76,5,13,0,0,75,77,5,10,0,0,76,75,1,0,0,0,76,77,1,0,0,0,77,120,
        1,0,0,0,78,79,5,10,0,0,79,80,3,26,13,0,80,81,5,11,0,0,81,85,3,24,
        12,0,82,83,5,12,0,0,83,84,5,11,0,0,84,86,3,24,12,0,85,82,1,0,0,0,
        85,86,1,0,0,0,86,87,1,0,0,0,87,89,5,13,0,0,88,90,5,10,0,0,89,88,
        1,0,0,0,89,90,1,0,0,0,90,120,1,0,0,0,91,92,5,10,0,0,92,93,5,4,0,
        0,93,94,3,26,13,0,94,95,5,5,0,0,95,96,5,14,0,0,96,100,3,24,12,0,
        97,98,5,12,0,0,98,99,5,11,0,0,99,101,3,24,12,0,100,97,1,0,0,0,100,
        101,1,0,0,0,101,102,1,0,0,0,102,104,5,13,0,0,103,105,5,10,0,0,104,
        103,1,0,0,0,104,105,1,0,0,0,105,120,1,0,0,0,106,107,5,10,0,0,107,
        108,3,26,13,0,108,109,5,14,0,0,109,113,3,24,12,0,110,111,5,12,0,
        0,111,112,5,11,0,0,112,114,3,24,12,0,113,110,1,0,0,0,113,114,1,0,
        0,0,114,115,1,0,0,0,115,117,5,13,0,0,116,118,5,10,0,0,117,116,1,
        0,0,0,117,118,1,0,0,0,118,120,1,0,0,0,119,63,1,0,0,0,119,78,1,0,
        0,0,119,91,1,0,0,0,119,106,1,0,0,0,120,11,1,0,0,0,121,122,5,15,0,
        0,122,123,5,4,0,0,123,124,3,26,13,0,124,125,5,5,0,0,125,126,5,11,
        0,0,126,127,3,24,12,0,127,129,5,13,0,0,128,130,5,16,0,0,129,128,
        1,0,0,0,129,130,1,0,0,0,130,13,1,0,0,0,131,132,5,17,0,0,132,133,
        5,4,0,0,133,134,7,2,0,0,134,135,5,44,0,0,135,136,7,1,0,0,136,137,
        5,24,0,0,137,138,5,1,0,0,138,139,3,26,13,0,139,140,5,1,0,0,140,141,
        3,8,4,0,141,142,5,5,0,0,142,143,5,11,0,0,143,144,3,24,12,0,144,146,
        5,13,0,0,145,147,5,16,0,0,146,145,1,0,0,0,146,147,1,0,0,0,147,15,
        1,0,0,0,148,149,5,18,0,0,149,150,5,44,0,0,150,152,5,4,0,0,151,153,
        3,18,9,0,152,151,1,0,0,0,152,153,1,0,0,0,153,154,1,0,0,0,154,155,
        5,5,0,0,155,156,5,11,0,0,156,157,3,24,12,0,157,159,5,13,0,0,158,
        160,5,18,0,0,159,158,1,0,0,0,159,160,1,0,0,0,160,17,1,0,0,0,161,
        162,5,39,0,0,162,168,5,44,0,0,163,164,5,19,0,0,164,165,5,39,0,0,
        165,167,5,44,0,0,166,163,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,
        168,169,1,0,0,0,169,19,1,0,0,0,170,168,1,0,0,0,171,172,5,44,0,0,
        172,174,5,4,0,0,173,175,3,22,11,0,174,173,1,0,0,0,174,175,1,0,0,
        0,175,176,1,0,0,0,176,177,5,5,0,0,177,21,1,0,0,0,178,183,3,26,13,
        0,179,180,5,19,0,0,180,182,3,26,13,0,181,179,1,0,0,0,182,185,1,0,
        0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,23,1,0,0,0,185,183,1,0,0,
        0,186,187,3,2,1,0,187,188,5,1,0,0,188,190,1,0,0,0,189,186,1,0,0,
        0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,25,1,0,0,0,
        193,191,1,0,0,0,194,195,6,13,-1,0,195,196,7,3,0,0,196,198,5,4,0,
        0,197,199,5,23,0,0,198,197,1,0,0,0,198,199,1,0,0,0,199,200,1,0,0,
        0,200,214,5,5,0,0,201,214,3,20,10,0,202,203,5,38,0,0,203,214,3,26,
        13,7,204,205,5,4,0,0,205,206,3,26,13,0,206,207,5,5,0,0,207,214,1,
        0,0,0,208,214,5,23,0,0,209,214,5,24,0,0,210,214,5,25,0,0,211,214,
        5,26,0,0,212,214,5,44,0,0,213,194,1,0,0,0,213,201,1,0,0,0,213,202,
        1,0,0,0,213,204,1,0,0,0,213,208,1,0,0,0,213,209,1,0,0,0,213,210,
        1,0,0,0,213,211,1,0,0,0,213,212,1,0,0,0,214,232,1,0,0,0,215,216,
        10,12,0,0,216,217,7,4,0,0,217,231,3,26,13,13,218,219,10,11,0,0,219,
        220,7,5,0,0,220,231,3,26,13,12,221,222,10,10,0,0,222,223,7,6,0,0,
        223,231,3,26,13,11,224,225,10,9,0,0,225,226,5,36,0,0,226,231,3,26,
        13,10,227,228,10,8,0,0,228,229,5,37,0,0,229,231,3,26,13,9,230,215,
        1,0,0,0,230,218,1,0,0,0,230,221,1,0,0,0,230,224,1,0,0,0,230,227,
        1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,27,1,
        0,0,0,234,232,1,0,0,0,24,33,46,57,72,76,85,89,100,104,113,117,119,
        129,146,152,159,168,174,183,191,198,213,230,232
    ]

class PseudoParser ( Parser ):

    grammarFileName = "Pseudo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'print'", "'shout'", "'('", "')'", 
                     "'='", "'is'", "'<<'", "'<-'", "'if'", "':'", "'else'", 
                     "'end'", "'then'", "'while'", "'loop'", "'for'", "'function'", 
                     "','", "'input'", "'scan'", "'listen'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'int'", "'float'", "'string'", 
                     "'boolean'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "NUMBER", 
                      "DOUBLE", "BOOL", "WS", "PLUS", "MINUS", "MULT", "DIV", 
                      "GREATER", "SMALLER", "EQUAL", "DIFFERENT", "AND", 
                      "OR", "NOT", "TYPE", "TYPE_INT", "TYPE_FLOAT", "TYPE_STRING", 
                      "TYPE_BOOL", "ID" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_printStatement = 2
    RULE_varDeclStatement = 3
    RULE_assignmentStatement = 4
    RULE_ifStatement = 5
    RULE_whileStatement = 6
    RULE_forStatement = 7
    RULE_functionDefStatement = 8
    RULE_paramList = 9
    RULE_functionCallStatement = 10
    RULE_argumentList = 11
    RULE_body = 12
    RULE_expr = 13

    ruleNames =  [ "program", "statement", "printStatement", "varDeclStatement", 
                   "assignmentStatement", "ifStatement", "whileStatement", 
                   "forStatement", "functionDefStatement", "paramList", 
                   "functionCallStatement", "argumentList", "body", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    STRING=23
    NUMBER=24
    DOUBLE=25
    BOOL=26
    WS=27
    PLUS=28
    MINUS=29
    MULT=30
    DIV=31
    GREATER=32
    SMALLER=33
    EQUAL=34
    DIFFERENT=35
    AND=36
    OR=37
    NOT=38
    TYPE=39
    TYPE_INT=40
    TYPE_FLOAT=41
    TYPE_STRING=42
    TYPE_BOOL=43
    ID=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PseudoParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoParser.StatementContext)
            else:
                return self.getTypedRuleContext(PseudoParser.StatementContext,i)


        def getRuleIndex(self):
            return PseudoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PseudoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18141942285324) != 0):
                self.state = 28
                self.statement()
                self.state = 29
                self.match(PseudoParser.T__0)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(PseudoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printStatement(self):
            return self.getTypedRuleContext(PseudoParser.PrintStatementContext,0)


        def varDeclStatement(self):
            return self.getTypedRuleContext(PseudoParser.VarDeclStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(PseudoParser.AssignmentStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(PseudoParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(PseudoParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(PseudoParser.ForStatementContext,0)


        def functionDefStatement(self):
            return self.getTypedRuleContext(PseudoParser.FunctionDefStatementContext,0)


        def functionCallStatement(self):
            return self.getTypedRuleContext(PseudoParser.FunctionCallStatementContext,0)


        def getRuleIndex(self):
            return PseudoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PseudoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.printStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.varDeclStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.assignmentStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 43
                self.forStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 44
                self.functionDefStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 45
                self.functionCallStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PseudoParser.ExprContext,0)


        def getRuleIndex(self):
            return PseudoParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = PseudoParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_printStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 49
            self.match(PseudoParser.T__3)
            self.state = 50
            self.expr(0)
            self.state = 51
            self.match(PseudoParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def TYPE(self):
            return self.getToken(PseudoParser.TYPE, 0)

        def ID(self):
            return self.getToken(PseudoParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(PseudoParser.ExprContext,0)


        def getRuleIndex(self):
            return PseudoParser.RULE_varDeclStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclStatement" ):
                listener.enterVarDeclStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclStatement" ):
                listener.exitVarDeclStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclStatement" ):
                return visitor.visitVarDeclStatement(self)
            else:
                return visitor.visitChildren(self)




    def varDeclStatement(self):

        localctx = PseudoParser.VarDeclStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(PseudoParser.TYPE)
            self.state = 54
            self.match(PseudoParser.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0):
                self.state = 55
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 56
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def ID(self):
            return self.getToken(PseudoParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(PseudoParser.ExprContext,0)


        def getRuleIndex(self):
            return PseudoParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = PseudoParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignmentStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(PseudoParser.ID)
            self.state = 60
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 61
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PseudoParser.ExprContext,0)


        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoParser.BodyContext)
            else:
                return self.getTypedRuleContext(PseudoParser.BodyContext,i)


        def getRuleIndex(self):
            return PseudoParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = PseudoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(PseudoParser.T__9)
                self.state = 64
                self.match(PseudoParser.T__3)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(PseudoParser.T__4)
                self.state = 67
                self.match(PseudoParser.T__10)
                self.state = 68
                self.body()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 69
                    self.match(PseudoParser.T__11)
                    self.state = 70
                    self.match(PseudoParser.T__10)
                    self.state = 71
                    self.body()


                self.state = 74
                self.match(PseudoParser.T__12)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 75
                    self.match(PseudoParser.T__9)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(PseudoParser.T__9)
                self.state = 79
                self.expr(0)
                self.state = 80
                self.match(PseudoParser.T__10)
                self.state = 81
                self.body()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 82
                    self.match(PseudoParser.T__11)
                    self.state = 83
                    self.match(PseudoParser.T__10)
                    self.state = 84
                    self.body()


                self.state = 87
                self.match(PseudoParser.T__12)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 88
                    self.match(PseudoParser.T__9)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(PseudoParser.T__9)
                self.state = 92
                self.match(PseudoParser.T__3)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(PseudoParser.T__4)
                self.state = 95
                self.match(PseudoParser.T__13)
                self.state = 96
                self.body()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 97
                    self.match(PseudoParser.T__11)
                    self.state = 98
                    self.match(PseudoParser.T__10)
                    self.state = 99
                    self.body()


                self.state = 102
                self.match(PseudoParser.T__12)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 103
                    self.match(PseudoParser.T__9)


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.match(PseudoParser.T__9)
                self.state = 107
                self.expr(0)
                self.state = 108
                self.match(PseudoParser.T__13)
                self.state = 109
                self.body()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 110
                    self.match(PseudoParser.T__11)
                    self.state = 111
                    self.match(PseudoParser.T__10)
                    self.state = 112
                    self.body()


                self.state = 115
                self.match(PseudoParser.T__12)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 116
                    self.match(PseudoParser.T__9)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PseudoParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(PseudoParser.BodyContext,0)


        def getRuleIndex(self):
            return PseudoParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = PseudoParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(PseudoParser.T__14)
            self.state = 122
            self.match(PseudoParser.T__3)
            self.state = 123
            self.expr(0)
            self.state = 124
            self.match(PseudoParser.T__4)
            self.state = 125
            self.match(PseudoParser.T__10)
            self.state = 126
            self.body()
            self.state = 127
            self.match(PseudoParser.T__12)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 128
                self.match(PseudoParser.T__15)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.OP = None # Token

        def ID(self):
            return self.getToken(PseudoParser.ID, 0)

        def NUMBER(self):
            return self.getToken(PseudoParser.NUMBER, 0)

        def expr(self):
            return self.getTypedRuleContext(PseudoParser.ExprContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(PseudoParser.AssignmentStatementContext,0)


        def body(self):
            return self.getTypedRuleContext(PseudoParser.BodyContext,0)


        def TYPE_INT(self):
            return self.getToken(PseudoParser.TYPE_INT, 0)

        def TYPE_FLOAT(self):
            return self.getToken(PseudoParser.TYPE_FLOAT, 0)

        def getRuleIndex(self):
            return PseudoParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = PseudoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(PseudoParser.T__16)
            self.state = 132
            self.match(PseudoParser.T__3)
            self.state = 133
            _la = self._input.LA(1)
            if not(_la==40 or _la==41):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 134
            self.match(PseudoParser.ID)
            self.state = 135
            localctx.OP = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0)):
                localctx.OP = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 136
            self.match(PseudoParser.NUMBER)
            self.state = 137
            self.match(PseudoParser.T__0)
            self.state = 138
            self.expr(0)
            self.state = 139
            self.match(PseudoParser.T__0)
            self.state = 140
            self.assignmentStatement()
            self.state = 141
            self.match(PseudoParser.T__4)
            self.state = 142
            self.match(PseudoParser.T__10)
            self.state = 143
            self.body()
            self.state = 144
            self.match(PseudoParser.T__12)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 145
                self.match(PseudoParser.T__15)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PseudoParser.ID, 0)

        def body(self):
            return self.getTypedRuleContext(PseudoParser.BodyContext,0)


        def paramList(self):
            return self.getTypedRuleContext(PseudoParser.ParamListContext,0)


        def getRuleIndex(self):
            return PseudoParser.RULE_functionDefStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefStatement" ):
                listener.enterFunctionDefStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefStatement" ):
                listener.exitFunctionDefStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefStatement" ):
                return visitor.visitFunctionDefStatement(self)
            else:
                return visitor.visitChildren(self)




    def functionDefStatement(self):

        localctx = PseudoParser.FunctionDefStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionDefStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(PseudoParser.T__17)
            self.state = 149
            self.match(PseudoParser.ID)
            self.state = 150
            self.match(PseudoParser.T__3)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 151
                self.paramList()


            self.state = 154
            self.match(PseudoParser.T__4)
            self.state = 155
            self.match(PseudoParser.T__10)
            self.state = 156
            self.body()
            self.state = 157
            self.match(PseudoParser.T__12)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 158
                self.match(PseudoParser.T__17)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoParser.TYPE)
            else:
                return self.getToken(PseudoParser.TYPE, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PseudoParser.ID)
            else:
                return self.getToken(PseudoParser.ID, i)

        def getRuleIndex(self):
            return PseudoParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = PseudoParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(PseudoParser.TYPE)
            self.state = 162
            self.match(PseudoParser.ID)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 163
                self.match(PseudoParser.T__18)
                self.state = 164
                self.match(PseudoParser.TYPE)
                self.state = 165
                self.match(PseudoParser.ID)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PseudoParser.ID, 0)

        def argumentList(self):
            return self.getTypedRuleContext(PseudoParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return PseudoParser.RULE_functionCallStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallStatement" ):
                listener.enterFunctionCallStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallStatement" ):
                listener.exitFunctionCallStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallStatement" ):
                return visitor.visitFunctionCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def functionCallStatement(self):

        localctx = PseudoParser.FunctionCallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functionCallStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(PseudoParser.ID)
            self.state = 172
            self.match(PseudoParser.T__3)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17867197120528) != 0):
                self.state = 173
                self.argumentList()


            self.state = 176
            self.match(PseudoParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoParser.ExprContext)
            else:
                return self.getTypedRuleContext(PseudoParser.ExprContext,i)


        def getRuleIndex(self):
            return PseudoParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = PseudoParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.expr(0)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 179
                self.match(PseudoParser.T__18)
                self.state = 180
                self.expr(0)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoParser.StatementContext)
            else:
                return self.getTypedRuleContext(PseudoParser.StatementContext,i)


        def getRuleIndex(self):
            return PseudoParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = PseudoParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18141942285324) != 0):
                self.state = 186
                self.statement()
                self.state = 187
                self.match(PseudoParser.T__0)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def STRING(self):
            return self.getToken(PseudoParser.STRING, 0)

        def functionCallStatement(self):
            return self.getTypedRuleContext(PseudoParser.FunctionCallStatementContext,0)


        def NOT(self):
            return self.getToken(PseudoParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudoParser.ExprContext)
            else:
                return self.getTypedRuleContext(PseudoParser.ExprContext,i)


        def NUMBER(self):
            return self.getToken(PseudoParser.NUMBER, 0)

        def DOUBLE(self):
            return self.getToken(PseudoParser.DOUBLE, 0)

        def BOOL(self):
            return self.getToken(PseudoParser.BOOL, 0)

        def ID(self):
            return self.getToken(PseudoParser.ID, 0)

        def MULT(self):
            return self.getToken(PseudoParser.MULT, 0)

        def DIV(self):
            return self.getToken(PseudoParser.DIV, 0)

        def PLUS(self):
            return self.getToken(PseudoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(PseudoParser.MINUS, 0)

        def GREATER(self):
            return self.getToken(PseudoParser.GREATER, 0)

        def SMALLER(self):
            return self.getToken(PseudoParser.SMALLER, 0)

        def EQUAL(self):
            return self.getToken(PseudoParser.EQUAL, 0)

        def DIFFERENT(self):
            return self.getToken(PseudoParser.DIFFERENT, 0)

        def AND(self):
            return self.getToken(PseudoParser.AND, 0)

        def OR(self):
            return self.getToken(PseudoParser.OR, 0)

        def getRuleIndex(self):
            return PseudoParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 195
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 196
                self.match(PseudoParser.T__3)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 197
                    self.match(PseudoParser.STRING)


                self.state = 200
                self.match(PseudoParser.T__4)
                pass

            elif la_ == 2:
                self.state = 201
                self.functionCallStatement()
                pass

            elif la_ == 3:
                self.state = 202
                self.match(PseudoParser.NOT)
                self.state = 203
                self.expr(7)
                pass

            elif la_ == 4:
                self.state = 204
                self.match(PseudoParser.T__3)
                self.state = 205
                self.expr(0)
                self.state = 206
                self.match(PseudoParser.T__4)
                pass

            elif la_ == 5:
                self.state = 208
                self.match(PseudoParser.STRING)
                pass

            elif la_ == 6:
                self.state = 209
                self.match(PseudoParser.NUMBER)
                pass

            elif la_ == 7:
                self.state = 210
                self.match(PseudoParser.DOUBLE)
                pass

            elif la_ == 8:
                self.state = 211
                self.match(PseudoParser.BOOL)
                pass

            elif la_ == 9:
                self.state = 212
                self.match(PseudoParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 230
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = PseudoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 215
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 216
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==30 or _la==31):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 217
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = PseudoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 218
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 219
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==29):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 220
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = PseudoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 221
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 222
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64424509440) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 223
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = PseudoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 224
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 225
                        self.match(PseudoParser.AND)
                        self.state = 226
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = PseudoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 227
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 228
                        self.match(PseudoParser.OR)
                        self.state = 229
                        self.expr(9)
                        pass

             
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         




