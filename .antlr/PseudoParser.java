// Generated from /Users/robertjacak/Documents/Kompilatory/pseudo/projectPseudo/Pseudo.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PseudoParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, STRING=33, NUMBER=34, DOUBLE=35, BOOL=36, WS=37, SINGLE_LINE_COMMENT=38, 
		MULTI_LINE_COMMENT=39, PLUS=40, MINUS=41, MULT=42, DIV=43, INTDIV=44, 
		INCREMENT=45, DECREMENT=46, GREATER=47, SMALLER=48, GREATEREQUAL=49, SMALLEREQUAL=50, 
		EQUAL=51, DIFFERENT=52, AND=53, OR=54, NOT=55, PARENT=56, TYPE=57, TYPE_INT=58, 
		TYPE_FLOAT=59, TYPE_STRING=60, TYPE_BOOL=61, TYPE_VOID=62, ID=63;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_printStatement = 2, RULE_assignmentStatement = 3, 
		RULE_ifStatement = 4, RULE_whileStatement = 5, RULE_forStatement = 6, 
		RULE_initStatement = 7, RULE_breakStatement = 8, RULE_continueStatement = 9, 
		RULE_functionDef = 10, RULE_returnStatement = 11, RULE_paramList = 12, 
		RULE_param = 13, RULE_functionCallStatement = 14, RULE_argumentList = 15, 
		RULE_body = 16, RULE_varDeclStatement = 17, RULE_expr = 18;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "printStatement", "assignmentStatement", "ifStatement", 
			"whileStatement", "forStatement", "initStatement", "breakStatement", 
			"continueStatement", "functionDef", "returnStatement", "paramList", "param", 
			"functionCallStatement", "argumentList", "body", "varDeclStatement", 
			"expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'print'", "'shout'", "'('", "')'", "'global'", "'='", "'is'", 
			"'<<'", "'<-'", "'if'", "':'", "'then'", "'elseif'", "'else'", "'end'", 
			"'while'", "'loop'", "'for'", "'break'", "'exit'", "'continue'", "'next'", 
			"'function'", "'fun'", "'def'", "'->'", "'return'", "','", "'input'", 
			"'scan'", "'listen'", null, null, null, null, null, null, null, "'+'", 
			"'-'", "'*'", "'/'", "'/#'", "'++'", "'--'", null, null, null, null, 
			null, null, null, null, null, "'parent::'", null, "'int'", "'float'", 
			"'string'", "'boolean'", "'void'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, "STRING", "NUMBER", 
			"DOUBLE", "BOOL", "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
			"PLUS", "MINUS", "MULT", "DIV", "INTDIV", "INCREMENT", "DECREMENT", "GREATER", 
			"SMALLER", "GREATEREQUAL", "SMALLEREQUAL", "EQUAL", "DIFFERENT", "AND", 
			"OR", "NOT", "PARENT", "TYPE", "TYPE_INT", "TYPE_FLOAT", "TYPE_STRING", 
			"TYPE_BOOL", "TYPE_VOID", "ID"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Pseudo.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PseudoParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(PseudoParser.EOF, 0); }
		public List<FunctionDefContext> functionDef() {
			return getRuleContexts(FunctionDefContext.class);
		}
		public FunctionDefContext functionDef(int i) {
			return getRuleContext(FunctionDefContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & -9079256848376592308L) != 0)) {
				{
				{
				setState(40);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__15:
				case T__23:
				case T__24:
				case T__25:
					{
					setState(38);
					functionDef();
					}
					break;
				case T__1:
				case T__2:
				case T__5:
				case T__10:
				case T__16:
				case T__18:
				case T__19:
				case T__20:
				case T__21:
				case T__22:
				case T__27:
				case TYPE:
				case ID:
					{
					setState(39);
					statement();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(42);
				match(T__0);
				}
				}
				setState(48);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(49);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public PrintStatementContext printStatement() {
			return getRuleContext(PrintStatementContext.class,0);
		}
		public AssignmentStatementContext assignmentStatement() {
			return getRuleContext(AssignmentStatementContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public FunctionCallStatementContext functionCallStatement() {
			return getRuleContext(FunctionCallStatementContext.class,0);
		}
		public ReturnStatementContext returnStatement() {
			return getRuleContext(ReturnStatementContext.class,0);
		}
		public BreakStatementContext breakStatement() {
			return getRuleContext(BreakStatementContext.class,0);
		}
		public ContinueStatementContext continueStatement() {
			return getRuleContext(ContinueStatementContext.class,0);
		}
		public VarDeclStatementContext varDeclStatement() {
			return getRuleContext(VarDeclStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(61);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(51);
				printStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(52);
				assignmentStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(53);
				ifStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(54);
				whileStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(55);
				forStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(56);
				functionCallStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(57);
				returnStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(58);
				breakStatement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(59);
				continueStatement();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(60);
				varDeclStatement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintStatementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public PrintStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStatement; }
	}

	public final PrintStatementContext printStatement() throws RecognitionException {
		PrintStatementContext _localctx = new PrintStatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_printStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			_la = _input.LA(1);
			if ( !(_la==T__1 || _la==T__2) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(64);
			match(T__3);
			setState(65);
			expr(0);
			setState(66);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentStatementContext extends ParserRuleContext {
		public Token global;
		public Token op;
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode INCREMENT() { return getToken(PseudoParser.INCREMENT, 0); }
		public TerminalNode DECREMENT() { return getToken(PseudoParser.DECREMENT, 0); }
		public AssignmentStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentStatement; }
	}

	public final AssignmentStatementContext assignmentStatement() throws RecognitionException {
		AssignmentStatementContext _localctx = new AssignmentStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_assignmentStatement);
		int _la;
		try {
			setState(79);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(68);
					((AssignmentStatementContext)_localctx).global = match(T__5);
					}
				}

				setState(71);
				match(ID);
				setState(72);
				((AssignmentStatementContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1920L) != 0)) ) {
					((AssignmentStatementContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(73);
				expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(75);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(74);
					((AssignmentStatementContext)_localctx).global = match(T__5);
					}
				}

				setState(77);
				match(ID);
				setState(78);
				((AssignmentStatementContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==INCREMENT || _la==DECREMENT) ) {
					((AssignmentStatementContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public List<BodyContext> body() {
			return getRuleContexts(BodyContext.class);
		}
		public BodyContext body(int i) {
			return getRuleContext(BodyContext.class,i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_ifStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(T__10);
			setState(87);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(82);
				match(T__3);
				setState(83);
				expr(0);
				setState(84);
				match(T__4);
				}
				break;
			case 2:
				{
				setState(86);
				expr(0);
				}
				break;
			}
			setState(89);
			_la = _input.LA(1);
			if ( !(_la==T__11 || _la==T__12) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(90);
			body();
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__13) {
				{
				{
				setState(91);
				match(T__13);
				setState(97);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
				case 1:
					{
					setState(92);
					match(T__3);
					setState(93);
					expr(0);
					setState(94);
					match(T__4);
					}
					break;
				case 2:
					{
					setState(96);
					expr(0);
					}
					break;
				}
				setState(99);
				_la = _input.LA(1);
				if ( !(_la==T__11 || _la==T__12) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(100);
				body();
				}
				}
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(107);
				match(T__14);
				setState(108);
				match(T__11);
				setState(109);
				body();
				}
			}

			setState(112);
			match(T__15);
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__10) {
				{
				setState(113);
				match(T__10);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_whileStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(T__16);
			setState(117);
			match(T__3);
			setState(118);
			expr(0);
			setState(119);
			match(T__4);
			setState(120);
			match(T__11);
			setState(121);
			body();
			setState(122);
			match(T__15);
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__17) {
				{
				setState(123);
				match(T__17);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStatementContext extends ParserRuleContext {
		public InitStatementContext entryStmt;
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentStatementContext assignmentStatement() {
			return getRuleContext(AssignmentStatementContext.class,0);
		}
		public InitStatementContext initStatement() {
			return getRuleContext(InitStatementContext.class,0);
		}
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_forStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(T__18);
			setState(127);
			match(T__3);
			setState(129);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & -9079256848778919872L) != 0)) {
				{
				setState(128);
				((ForStatementContext)_localctx).entryStmt = initStatement();
				}
			}

			setState(131);
			match(T__0);
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & -8971168122333560816L) != 0)) {
				{
				setState(132);
				expr(0);
				}
			}

			setState(135);
			match(T__0);
			setState(137);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5 || _la==ID) {
				{
				setState(136);
				assignmentStatement();
				}
			}

			setState(139);
			match(T__4);
			setState(140);
			match(T__11);
			setState(141);
			body();
			setState(142);
			match(T__15);
			setState(144);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__17) {
				{
				setState(143);
				match(T__17);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InitStatementContext extends ParserRuleContext {
		public VarDeclStatementContext varDeclStatement() {
			return getRuleContext(VarDeclStatementContext.class,0);
		}
		public AssignmentStatementContext assignmentStatement() {
			return getRuleContext(AssignmentStatementContext.class,0);
		}
		public InitStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initStatement; }
	}

	public final InitStatementContext initStatement() throws RecognitionException {
		InitStatementContext _localctx = new InitStatementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_initStatement);
		try {
			setState(148);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(146);
				varDeclStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(147);
				assignmentStatement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BreakStatementContext extends ParserRuleContext {
		public BreakStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakStatement; }
	}

	public final BreakStatementContext breakStatement() throws RecognitionException {
		BreakStatementContext _localctx = new BreakStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_breakStatement);
		int _la;
		try {
			setState(158);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__19:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				match(T__19);
				setState(152);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__17) {
					{
					setState(151);
					match(T__17);
					}
				}

				}
				break;
			case T__20:
				enterOuterAlt(_localctx, 2);
				{
				setState(154);
				match(T__20);
				setState(156);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__17) {
					{
					setState(155);
					match(T__17);
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContinueStatementContext extends ParserRuleContext {
		public ContinueStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continueStatement; }
	}

	public final ContinueStatementContext continueStatement() throws RecognitionException {
		ContinueStatementContext _localctx = new ContinueStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_continueStatement);
		int _la;
		try {
			setState(168);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__21:
				enterOuterAlt(_localctx, 1);
				{
				setState(160);
				match(T__21);
				setState(162);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__17) {
					{
					setState(161);
					match(T__17);
					}
				}

				}
				break;
			case T__22:
				enterOuterAlt(_localctx, 2);
				{
				setState(164);
				match(T__22);
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__17) {
					{
					setState(165);
					match(T__17);
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDefContext extends ParserRuleContext {
		public Token type;
		public Token name;
		public ParamListContext params;
		public BodyContext block;
		public TerminalNode TYPE() { return getToken(PseudoParser.TYPE, 0); }
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ParamListContext paramList() {
			return getRuleContext(ParamListContext.class,0);
		}
		public FunctionDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDef; }
	}

	public final FunctionDefContext functionDef() throws RecognitionException {
		FunctionDefContext _localctx = new FunctionDefContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_functionDef);
		int _la;
		try {
			setState(260);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(170);
				match(T__23);
				setState(171);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(172);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(173);
				match(T__3);
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(174);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(177);
				match(T__4);
				setState(178);
				match(T__11);
				setState(179);
				((FunctionDefContext)_localctx).block = body();
				setState(180);
				match(T__15);
				setState(182);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__23) {
					{
					setState(181);
					match(T__23);
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(184);
				match(T__24);
				setState(185);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(186);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(187);
				match(T__3);
				setState(189);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(188);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(191);
				match(T__4);
				setState(192);
				match(T__11);
				setState(193);
				((FunctionDefContext)_localctx).block = body();
				setState(194);
				match(T__15);
				setState(196);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__24) {
					{
					setState(195);
					match(T__24);
					}
				}

				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(198);
				match(T__25);
				setState(199);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(200);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(201);
				match(T__3);
				setState(203);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(202);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(205);
				match(T__4);
				setState(206);
				match(T__11);
				setState(207);
				((FunctionDefContext)_localctx).block = body();
				setState(208);
				match(T__15);
				setState(210);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__25) {
					{
					setState(209);
					match(T__25);
					}
				}

				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(212);
				match(T__23);
				setState(213);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(214);
				match(T__3);
				setState(216);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(215);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(218);
				match(T__4);
				setState(219);
				match(T__26);
				setState(220);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(221);
				match(T__11);
				setState(222);
				((FunctionDefContext)_localctx).block = body();
				setState(223);
				match(T__15);
				setState(225);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__23) {
					{
					setState(224);
					match(T__23);
					}
				}

				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(227);
				match(T__24);
				setState(228);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(229);
				match(T__3);
				setState(231);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(230);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(233);
				match(T__4);
				setState(234);
				match(T__26);
				setState(235);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(236);
				match(T__11);
				setState(237);
				((FunctionDefContext)_localctx).block = body();
				setState(238);
				match(T__0);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(240);
				match(T__15);
				setState(242);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__24) {
					{
					setState(241);
					match(T__24);
					}
				}

				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(244);
				match(T__25);
				setState(245);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(246);
				match(T__3);
				setState(248);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(247);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(250);
				match(T__4);
				setState(251);
				match(T__26);
				setState(252);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(253);
				match(T__11);
				setState(254);
				((FunctionDefContext)_localctx).block = body();
				setState(255);
				match(T__0);
				setState(256);
				match(T__15);
				setState(258);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__25) {
					{
					setState(257);
					match(T__25);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStatementContext extends ParserRuleContext {
		public ExprContext val;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ReturnStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStatement; }
	}

	public final ReturnStatementContext returnStatement() throws RecognitionException {
		ReturnStatementContext _localctx = new ReturnStatementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_returnStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(262);
			match(T__27);
			setState(263);
			((ReturnStatementContext)_localctx).val = expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamListContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public ParamListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramList; }
	}

	public final ParamListContext paramList() throws RecognitionException {
		ParamListContext _localctx = new ParamListContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_paramList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(265);
			param();
			setState(270);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__28) {
				{
				{
				setState(266);
				match(T__28);
				setState(267);
				param();
				}
				}
				setState(272);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public Token type;
		public Token name;
		public TerminalNode TYPE() { return getToken(PseudoParser.TYPE, 0); }
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(273);
			((ParamContext)_localctx).type = match(TYPE);
			setState(274);
			((ParamContext)_localctx).name = match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallStatementContext extends ParserRuleContext {
		public Token name;
		public ArgumentListContext args;
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public FunctionCallStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallStatement; }
	}

	public final FunctionCallStatementContext functionCallStatement() throws RecognitionException {
		FunctionCallStatementContext _localctx = new FunctionCallStatementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_functionCallStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			((FunctionCallStatementContext)_localctx).name = match(ID);
			setState(277);
			match(T__3);
			setState(279);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & -8971168122333560816L) != 0)) {
				{
				setState(278);
				((FunctionCallStatementContext)_localctx).args = argumentList();
				}
			}

			setState(281);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentListContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentList; }
	}

	public final ArgumentListContext argumentList() throws RecognitionException {
		ArgumentListContext _localctx = new ArgumentListContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			expr(0);
			setState(288);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__28) {
				{
				{
				setState(284);
				match(T__28);
				setState(285);
				expr(0);
				}
				}
				setState(290);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BodyContext extends ParserRuleContext {
		public List<FunctionDefContext> functionDef() {
			return getRuleContexts(FunctionDefContext.class);
		}
		public FunctionDefContext functionDef(int i) {
			return getRuleContext(FunctionDefContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_body);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(299);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(293);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case T__15:
					case T__23:
					case T__24:
					case T__25:
						{
						setState(291);
						functionDef();
						}
						break;
					case T__1:
					case T__2:
					case T__5:
					case T__10:
					case T__16:
					case T__18:
					case T__19:
					case T__20:
					case T__21:
					case T__22:
					case T__27:
					case TYPE:
					case ID:
						{
						setState(292);
						statement();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(295);
					match(T__0);
					}
					} 
				}
				setState(301);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclStatementContext extends ParserRuleContext {
		public Token global;
		public Token op;
		public TerminalNode TYPE() { return getToken(PseudoParser.TYPE, 0); }
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public VarDeclStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclStatement; }
	}

	public final VarDeclStatementContext varDeclStatement() throws RecognitionException {
		VarDeclStatementContext _localctx = new VarDeclStatementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_varDeclStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(303);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(302);
				((VarDeclStatementContext)_localctx).global = match(T__5);
				}
			}

			setState(305);
			match(TYPE);
			setState(306);
			match(ID);
			setState(309);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1920L) != 0)) {
				{
				setState(307);
				((VarDeclStatementContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1920L) != 0)) ) {
					((VarDeclStatementContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(308);
				expr(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public Token op;
		public TerminalNode STRING() { return getToken(PseudoParser.STRING, 0); }
		public FunctionCallStatementContext functionCallStatement() {
			return getRuleContext(FunctionCallStatementContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MINUS() { return getToken(PseudoParser.MINUS, 0); }
		public TerminalNode NOT() { return getToken(PseudoParser.NOT, 0); }
		public TerminalNode PARENT() { return getToken(PseudoParser.PARENT, 0); }
		public TerminalNode TYPE() { return getToken(PseudoParser.TYPE, 0); }
		public TerminalNode NUMBER() { return getToken(PseudoParser.NUMBER, 0); }
		public TerminalNode DOUBLE() { return getToken(PseudoParser.DOUBLE, 0); }
		public TerminalNode BOOL() { return getToken(PseudoParser.BOOL, 0); }
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public TerminalNode MULT() { return getToken(PseudoParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(PseudoParser.DIV, 0); }
		public TerminalNode PLUS() { return getToken(PseudoParser.PLUS, 0); }
		public TerminalNode GREATER() { return getToken(PseudoParser.GREATER, 0); }
		public TerminalNode SMALLER() { return getToken(PseudoParser.SMALLER, 0); }
		public TerminalNode EQUAL() { return getToken(PseudoParser.EQUAL, 0); }
		public TerminalNode DIFFERENT() { return getToken(PseudoParser.DIFFERENT, 0); }
		public TerminalNode GREATEREQUAL() { return getToken(PseudoParser.GREATEREQUAL, 0); }
		public TerminalNode SMALLEREQUAL() { return getToken(PseudoParser.SMALLEREQUAL, 0); }
		public TerminalNode INTDIV() { return getToken(PseudoParser.INTDIV, 0); }
		public TerminalNode AND() { return getToken(PseudoParser.AND, 0); }
		public TerminalNode OR() { return getToken(PseudoParser.OR, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(339);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,44,_ctx) ) {
			case 1:
				{
				setState(312);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7516192768L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(313);
				match(T__3);
				setState(315);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==STRING) {
					{
					setState(314);
					match(STRING);
					}
				}

				setState(317);
				match(T__4);
				}
				break;
			case 2:
				{
				setState(318);
				functionCallStatement();
				}
				break;
			case 3:
				{
				setState(319);
				((ExprContext)_localctx).op = match(MINUS);
				setState(320);
				expr(12);
				}
				break;
			case 4:
				{
				setState(321);
				((ExprContext)_localctx).op = match(NOT);
				setState(322);
				expr(9);
				}
				break;
			case 5:
				{
				setState(323);
				((ExprContext)_localctx).op = match(PARENT);
				setState(324);
				expr(8);
				}
				break;
			case 6:
				{
				setState(325);
				((ExprContext)_localctx).op = match(TYPE);
				setState(326);
				match(T__3);
				setState(327);
				expr(0);
				setState(328);
				match(T__4);
				}
				break;
			case 7:
				{
				setState(330);
				match(T__3);
				setState(331);
				expr(0);
				setState(332);
				match(T__4);
				}
				break;
			case 8:
				{
				setState(334);
				match(STRING);
				}
				break;
			case 9:
				{
				setState(335);
				match(NUMBER);
				}
				break;
			case 10:
				{
				setState(336);
				match(DOUBLE);
				}
				break;
			case 11:
				{
				setState(337);
				match(BOOL);
				}
				break;
			case 12:
				{
				setState(338);
				match(ID);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(364);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,46,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(362);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(341);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(342);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MULT || _la==DIV) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(343);
						expr(18);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(344);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(345);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(346);
						expr(17);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(347);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(348);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 8866461766385664L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(349);
						expr(16);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(350);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(351);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 8866461766385664L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(352);
						expr(15);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(353);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(354);
						((ExprContext)_localctx).op = match(INTDIV);
						setState(355);
						expr(14);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(356);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(357);
						((ExprContext)_localctx).op = match(AND);
						setState(358);
						expr(12);
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(359);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(360);
						((ExprContext)_localctx).op = match(OR);
						setState(361);
						expr(11);
						}
						break;
					}
					} 
				}
				setState(366);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,46,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 18:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 17);
		case 1:
			return precpred(_ctx, 16);
		case 2:
			return precpred(_ctx, 15);
		case 3:
			return precpred(_ctx, 14);
		case 4:
			return precpred(_ctx, 13);
		case 5:
			return precpred(_ctx, 11);
		case 6:
			return precpred(_ctx, 10);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001?\u0170\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0001\u0000\u0001\u0000\u0003\u0000)\b\u0000\u0001\u0000\u0001\u0000"+
		"\u0005\u0000-\b\u0000\n\u0000\f\u00000\t\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001>\b\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0003\u0003F\b\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0003\u0003L\b\u0003\u0001\u0003\u0001\u0003\u0003\u0003P\b\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004X\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004b\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0005\u0004g\b\u0004\n\u0004\f\u0004j\t"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004o\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0003\u0004s\b\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003"+
		"\u0005}\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u0082"+
		"\b\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u0086\b\u0006\u0001\u0006"+
		"\u0001\u0006\u0003\u0006\u008a\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0003\u0006\u0091\b\u0006\u0001\u0007\u0001\u0007"+
		"\u0003\u0007\u0095\b\u0007\u0001\b\u0001\b\u0003\b\u0099\b\b\u0001\b\u0001"+
		"\b\u0003\b\u009d\b\b\u0003\b\u009f\b\b\u0001\t\u0001\t\u0003\t\u00a3\b"+
		"\t\u0001\t\u0001\t\u0003\t\u00a7\b\t\u0003\t\u00a9\b\t\u0001\n\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0003\n\u00b0\b\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0003\n\u00b7\b\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003"+
		"\n\u00be\b\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00c5\b\n"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00cc\b\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0003\n\u00d3\b\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n\u00d9\b\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n\u00e2\b\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00e8\b\n"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n\u00f3\b\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00f9\b\n"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003"+
		"\n\u0103\b\n\u0003\n\u0105\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0005\f\u010d\b\f\n\f\f\f\u0110\t\f\u0001\r\u0001\r"+
		"\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u0118\b\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f"+
		"\u011f\b\u000f\n\u000f\f\u000f\u0122\t\u000f\u0001\u0010\u0001\u0010\u0003"+
		"\u0010\u0126\b\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u012a\b\u0010"+
		"\n\u0010\f\u0010\u012d\t\u0010\u0001\u0011\u0003\u0011\u0130\b\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u0136\b\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u013c\b\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u0154\b\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0005\u0012\u016b\b\u0012\n\u0012\f\u0012"+
		"\u016e\t\u0012\u0001\u0012\u0000\u0001$\u0013\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$\u0000"+
		"\b\u0001\u0000\u0002\u0003\u0001\u0000\u0007\n\u0001\u0000-.\u0001\u0000"+
		"\f\r\u0001\u0000\u001e \u0001\u0000*+\u0001\u0000()\u0001\u0000/4\u01a7"+
		"\u0000.\u0001\u0000\u0000\u0000\u0002=\u0001\u0000\u0000\u0000\u0004?"+
		"\u0001\u0000\u0000\u0000\u0006O\u0001\u0000\u0000\u0000\bQ\u0001\u0000"+
		"\u0000\u0000\nt\u0001\u0000\u0000\u0000\f~\u0001\u0000\u0000\u0000\u000e"+
		"\u0094\u0001\u0000\u0000\u0000\u0010\u009e\u0001\u0000\u0000\u0000\u0012"+
		"\u00a8\u0001\u0000\u0000\u0000\u0014\u0104\u0001\u0000\u0000\u0000\u0016"+
		"\u0106\u0001\u0000\u0000\u0000\u0018\u0109\u0001\u0000\u0000\u0000\u001a"+
		"\u0111\u0001\u0000\u0000\u0000\u001c\u0114\u0001\u0000\u0000\u0000\u001e"+
		"\u011b\u0001\u0000\u0000\u0000 \u012b\u0001\u0000\u0000\u0000\"\u012f"+
		"\u0001\u0000\u0000\u0000$\u0153\u0001\u0000\u0000\u0000&)\u0003\u0014"+
		"\n\u0000\')\u0003\u0002\u0001\u0000(&\u0001\u0000\u0000\u0000(\'\u0001"+
		"\u0000\u0000\u0000)*\u0001\u0000\u0000\u0000*+\u0005\u0001\u0000\u0000"+
		"+-\u0001\u0000\u0000\u0000,(\u0001\u0000\u0000\u0000-0\u0001\u0000\u0000"+
		"\u0000.,\u0001\u0000\u0000\u0000./\u0001\u0000\u0000\u0000/1\u0001\u0000"+
		"\u0000\u00000.\u0001\u0000\u0000\u000012\u0005\u0000\u0000\u00012\u0001"+
		"\u0001\u0000\u0000\u00003>\u0003\u0004\u0002\u00004>\u0003\u0006\u0003"+
		"\u00005>\u0003\b\u0004\u00006>\u0003\n\u0005\u00007>\u0003\f\u0006\u0000"+
		"8>\u0003\u001c\u000e\u00009>\u0003\u0016\u000b\u0000:>\u0003\u0010\b\u0000"+
		";>\u0003\u0012\t\u0000<>\u0003\"\u0011\u0000=3\u0001\u0000\u0000\u0000"+
		"=4\u0001\u0000\u0000\u0000=5\u0001\u0000\u0000\u0000=6\u0001\u0000\u0000"+
		"\u0000=7\u0001\u0000\u0000\u0000=8\u0001\u0000\u0000\u0000=9\u0001\u0000"+
		"\u0000\u0000=:\u0001\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000=<\u0001"+
		"\u0000\u0000\u0000>\u0003\u0001\u0000\u0000\u0000?@\u0007\u0000\u0000"+
		"\u0000@A\u0005\u0004\u0000\u0000AB\u0003$\u0012\u0000BC\u0005\u0005\u0000"+
		"\u0000C\u0005\u0001\u0000\u0000\u0000DF\u0005\u0006\u0000\u0000ED\u0001"+
		"\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000"+
		"GH\u0005?\u0000\u0000HI\u0007\u0001\u0000\u0000IP\u0003$\u0012\u0000J"+
		"L\u0005\u0006\u0000\u0000KJ\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000"+
		"\u0000LM\u0001\u0000\u0000\u0000MN\u0005?\u0000\u0000NP\u0007\u0002\u0000"+
		"\u0000OE\u0001\u0000\u0000\u0000OK\u0001\u0000\u0000\u0000P\u0007\u0001"+
		"\u0000\u0000\u0000QW\u0005\u000b\u0000\u0000RS\u0005\u0004\u0000\u0000"+
		"ST\u0003$\u0012\u0000TU\u0005\u0005\u0000\u0000UX\u0001\u0000\u0000\u0000"+
		"VX\u0003$\u0012\u0000WR\u0001\u0000\u0000\u0000WV\u0001\u0000\u0000\u0000"+
		"XY\u0001\u0000\u0000\u0000YZ\u0007\u0003\u0000\u0000Zh\u0003 \u0010\u0000"+
		"[a\u0005\u000e\u0000\u0000\\]\u0005\u0004\u0000\u0000]^\u0003$\u0012\u0000"+
		"^_\u0005\u0005\u0000\u0000_b\u0001\u0000\u0000\u0000`b\u0003$\u0012\u0000"+
		"a\\\u0001\u0000\u0000\u0000a`\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000"+
		"\u0000cd\u0007\u0003\u0000\u0000de\u0003 \u0010\u0000eg\u0001\u0000\u0000"+
		"\u0000f[\u0001\u0000\u0000\u0000gj\u0001\u0000\u0000\u0000hf\u0001\u0000"+
		"\u0000\u0000hi\u0001\u0000\u0000\u0000in\u0001\u0000\u0000\u0000jh\u0001"+
		"\u0000\u0000\u0000kl\u0005\u000f\u0000\u0000lm\u0005\f\u0000\u0000mo\u0003"+
		" \u0010\u0000nk\u0001\u0000\u0000\u0000no\u0001\u0000\u0000\u0000op\u0001"+
		"\u0000\u0000\u0000pr\u0005\u0010\u0000\u0000qs\u0005\u000b\u0000\u0000"+
		"rq\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000s\t\u0001\u0000\u0000"+
		"\u0000tu\u0005\u0011\u0000\u0000uv\u0005\u0004\u0000\u0000vw\u0003$\u0012"+
		"\u0000wx\u0005\u0005\u0000\u0000xy\u0005\f\u0000\u0000yz\u0003 \u0010"+
		"\u0000z|\u0005\u0010\u0000\u0000{}\u0005\u0012\u0000\u0000|{\u0001\u0000"+
		"\u0000\u0000|}\u0001\u0000\u0000\u0000}\u000b\u0001\u0000\u0000\u0000"+
		"~\u007f\u0005\u0013\u0000\u0000\u007f\u0081\u0005\u0004\u0000\u0000\u0080"+
		"\u0082\u0003\u000e\u0007\u0000\u0081\u0080\u0001\u0000\u0000\u0000\u0081"+
		"\u0082\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083"+
		"\u0085\u0005\u0001\u0000\u0000\u0084\u0086\u0003$\u0012\u0000\u0085\u0084"+
		"\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u0087"+
		"\u0001\u0000\u0000\u0000\u0087\u0089\u0005\u0001\u0000\u0000\u0088\u008a"+
		"\u0003\u0006\u0003\u0000\u0089\u0088\u0001\u0000\u0000\u0000\u0089\u008a"+
		"\u0001\u0000\u0000\u0000\u008a\u008b\u0001\u0000\u0000\u0000\u008b\u008c"+
		"\u0005\u0005\u0000\u0000\u008c\u008d\u0005\f\u0000\u0000\u008d\u008e\u0003"+
		" \u0010\u0000\u008e\u0090\u0005\u0010\u0000\u0000\u008f\u0091\u0005\u0012"+
		"\u0000\u0000\u0090\u008f\u0001\u0000\u0000\u0000\u0090\u0091\u0001\u0000"+
		"\u0000\u0000\u0091\r\u0001\u0000\u0000\u0000\u0092\u0095\u0003\"\u0011"+
		"\u0000\u0093\u0095\u0003\u0006\u0003\u0000\u0094\u0092\u0001\u0000\u0000"+
		"\u0000\u0094\u0093\u0001\u0000\u0000\u0000\u0095\u000f\u0001\u0000\u0000"+
		"\u0000\u0096\u0098\u0005\u0014\u0000\u0000\u0097\u0099\u0005\u0012\u0000"+
		"\u0000\u0098\u0097\u0001\u0000\u0000\u0000\u0098\u0099\u0001\u0000\u0000"+
		"\u0000\u0099\u009f\u0001\u0000\u0000\u0000\u009a\u009c\u0005\u0015\u0000"+
		"\u0000\u009b\u009d\u0005\u0012\u0000\u0000\u009c\u009b\u0001\u0000\u0000"+
		"\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009d\u009f\u0001\u0000\u0000"+
		"\u0000\u009e\u0096\u0001\u0000\u0000\u0000\u009e\u009a\u0001\u0000\u0000"+
		"\u0000\u009f\u0011\u0001\u0000\u0000\u0000\u00a0\u00a2\u0005\u0016\u0000"+
		"\u0000\u00a1\u00a3\u0005\u0012\u0000\u0000\u00a2\u00a1\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a3\u0001\u0000\u0000\u0000\u00a3\u00a9\u0001\u0000\u0000"+
		"\u0000\u00a4\u00a6\u0005\u0017\u0000\u0000\u00a5\u00a7\u0005\u0012\u0000"+
		"\u0000\u00a6\u00a5\u0001\u0000\u0000\u0000\u00a6\u00a7\u0001\u0000\u0000"+
		"\u0000\u00a7\u00a9\u0001\u0000\u0000\u0000\u00a8\u00a0\u0001\u0000\u0000"+
		"\u0000\u00a8\u00a4\u0001\u0000\u0000\u0000\u00a9\u0013\u0001\u0000\u0000"+
		"\u0000\u00aa\u00ab\u0005\u0018\u0000\u0000\u00ab\u00ac\u00059\u0000\u0000"+
		"\u00ac\u00ad\u0005?\u0000\u0000\u00ad\u00af\u0005\u0004\u0000\u0000\u00ae"+
		"\u00b0\u0003\u0018\f\u0000\u00af\u00ae\u0001\u0000\u0000\u0000\u00af\u00b0"+
		"\u0001\u0000\u0000\u0000\u00b0\u00b1\u0001\u0000\u0000\u0000\u00b1\u00b2"+
		"\u0005\u0005\u0000\u0000\u00b2\u00b3\u0005\f\u0000\u0000\u00b3\u00b4\u0003"+
		" \u0010\u0000\u00b4\u00b6\u0005\u0010\u0000\u0000\u00b5\u00b7\u0005\u0018"+
		"\u0000\u0000\u00b6\u00b5\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000"+
		"\u0000\u0000\u00b7\u0105\u0001\u0000\u0000\u0000\u00b8\u00b9\u0005\u0019"+
		"\u0000\u0000\u00b9\u00ba\u00059\u0000\u0000\u00ba\u00bb\u0005?\u0000\u0000"+
		"\u00bb\u00bd\u0005\u0004\u0000\u0000\u00bc\u00be\u0003\u0018\f\u0000\u00bd"+
		"\u00bc\u0001\u0000\u0000\u0000\u00bd\u00be\u0001\u0000\u0000\u0000\u00be"+
		"\u00bf\u0001\u0000\u0000\u0000\u00bf\u00c0\u0005\u0005\u0000\u0000\u00c0"+
		"\u00c1\u0005\f\u0000\u0000\u00c1\u00c2\u0003 \u0010\u0000\u00c2\u00c4"+
		"\u0005\u0010\u0000\u0000\u00c3\u00c5\u0005\u0019\u0000\u0000\u00c4\u00c3"+
		"\u0001\u0000\u0000\u0000\u00c4\u00c5\u0001\u0000\u0000\u0000\u00c5\u0105"+
		"\u0001\u0000\u0000\u0000\u00c6\u00c7\u0005\u001a\u0000\u0000\u00c7\u00c8"+
		"\u00059\u0000\u0000\u00c8\u00c9\u0005?\u0000\u0000\u00c9\u00cb\u0005\u0004"+
		"\u0000\u0000\u00ca\u00cc\u0003\u0018\f\u0000\u00cb\u00ca\u0001\u0000\u0000"+
		"\u0000\u00cb\u00cc\u0001\u0000\u0000\u0000\u00cc\u00cd\u0001\u0000\u0000"+
		"\u0000\u00cd\u00ce\u0005\u0005\u0000\u0000\u00ce\u00cf\u0005\f\u0000\u0000"+
		"\u00cf\u00d0\u0003 \u0010\u0000\u00d0\u00d2\u0005\u0010\u0000\u0000\u00d1"+
		"\u00d3\u0005\u001a\u0000\u0000\u00d2\u00d1\u0001\u0000\u0000\u0000\u00d2"+
		"\u00d3\u0001\u0000\u0000\u0000\u00d3\u0105\u0001\u0000\u0000\u0000\u00d4"+
		"\u00d5\u0005\u0018\u0000\u0000\u00d5\u00d6\u0005?\u0000\u0000\u00d6\u00d8"+
		"\u0005\u0004\u0000\u0000\u00d7\u00d9\u0003\u0018\f\u0000\u00d8\u00d7\u0001"+
		"\u0000\u0000\u0000\u00d8\u00d9\u0001\u0000\u0000\u0000\u00d9\u00da\u0001"+
		"\u0000\u0000\u0000\u00da\u00db\u0005\u0005\u0000\u0000\u00db\u00dc\u0005"+
		"\u001b\u0000\u0000\u00dc\u00dd\u00059\u0000\u0000\u00dd\u00de\u0005\f"+
		"\u0000\u0000\u00de\u00df\u0003 \u0010\u0000\u00df\u00e1\u0005\u0010\u0000"+
		"\u0000\u00e0\u00e2\u0005\u0018\u0000\u0000\u00e1\u00e0\u0001\u0000\u0000"+
		"\u0000\u00e1\u00e2\u0001\u0000\u0000\u0000\u00e2\u0105\u0001\u0000\u0000"+
		"\u0000\u00e3\u00e4\u0005\u0019\u0000\u0000\u00e4\u00e5\u0005?\u0000\u0000"+
		"\u00e5\u00e7\u0005\u0004\u0000\u0000\u00e6\u00e8\u0003\u0018\f\u0000\u00e7"+
		"\u00e6\u0001\u0000\u0000\u0000\u00e7\u00e8\u0001\u0000\u0000\u0000\u00e8"+
		"\u00e9\u0001\u0000\u0000\u0000\u00e9\u00ea\u0005\u0005\u0000\u0000\u00ea"+
		"\u00eb\u0005\u001b\u0000\u0000\u00eb\u00ec\u00059\u0000\u0000\u00ec\u00ed"+
		"\u0005\f\u0000\u0000\u00ed\u00ee\u0003 \u0010\u0000\u00ee\u00ef\u0005"+
		"\u0001\u0000\u0000\u00ef\u0105\u0001\u0000\u0000\u0000\u00f0\u00f2\u0005"+
		"\u0010\u0000\u0000\u00f1\u00f3\u0005\u0019\u0000\u0000\u00f2\u00f1\u0001"+
		"\u0000\u0000\u0000\u00f2\u00f3\u0001\u0000\u0000\u0000\u00f3\u0105\u0001"+
		"\u0000\u0000\u0000\u00f4\u00f5\u0005\u001a\u0000\u0000\u00f5\u00f6\u0005"+
		"?\u0000\u0000\u00f6\u00f8\u0005\u0004\u0000\u0000\u00f7\u00f9\u0003\u0018"+
		"\f\u0000\u00f8\u00f7\u0001\u0000\u0000\u0000\u00f8\u00f9\u0001\u0000\u0000"+
		"\u0000\u00f9\u00fa\u0001\u0000\u0000\u0000\u00fa\u00fb\u0005\u0005\u0000"+
		"\u0000\u00fb\u00fc\u0005\u001b\u0000\u0000\u00fc\u00fd\u00059\u0000\u0000"+
		"\u00fd\u00fe\u0005\f\u0000\u0000\u00fe\u00ff\u0003 \u0010\u0000\u00ff"+
		"\u0100\u0005\u0001\u0000\u0000\u0100\u0102\u0005\u0010\u0000\u0000\u0101"+
		"\u0103\u0005\u001a\u0000\u0000\u0102\u0101\u0001\u0000\u0000\u0000\u0102"+
		"\u0103\u0001\u0000\u0000\u0000\u0103\u0105\u0001\u0000\u0000\u0000\u0104"+
		"\u00aa\u0001\u0000\u0000\u0000\u0104\u00b8\u0001\u0000\u0000\u0000\u0104"+
		"\u00c6\u0001\u0000\u0000\u0000\u0104\u00d4\u0001\u0000\u0000\u0000\u0104"+
		"\u00e3\u0001\u0000\u0000\u0000\u0104\u00f0\u0001\u0000\u0000\u0000\u0104"+
		"\u00f4\u0001\u0000\u0000\u0000\u0105\u0015\u0001\u0000\u0000\u0000\u0106"+
		"\u0107\u0005\u001c\u0000\u0000\u0107\u0108\u0003$\u0012\u0000\u0108\u0017"+
		"\u0001\u0000\u0000\u0000\u0109\u010e\u0003\u001a\r\u0000\u010a\u010b\u0005"+
		"\u001d\u0000\u0000\u010b\u010d\u0003\u001a\r\u0000\u010c\u010a\u0001\u0000"+
		"\u0000\u0000\u010d\u0110\u0001\u0000\u0000\u0000\u010e\u010c\u0001\u0000"+
		"\u0000\u0000\u010e\u010f\u0001\u0000\u0000\u0000\u010f\u0019\u0001\u0000"+
		"\u0000\u0000\u0110\u010e\u0001\u0000\u0000\u0000\u0111\u0112\u00059\u0000"+
		"\u0000\u0112\u0113\u0005?\u0000\u0000\u0113\u001b\u0001\u0000\u0000\u0000"+
		"\u0114\u0115\u0005?\u0000\u0000\u0115\u0117\u0005\u0004\u0000\u0000\u0116"+
		"\u0118\u0003\u001e\u000f\u0000\u0117\u0116\u0001\u0000\u0000\u0000\u0117"+
		"\u0118\u0001\u0000\u0000\u0000\u0118\u0119\u0001\u0000\u0000\u0000\u0119"+
		"\u011a\u0005\u0005\u0000\u0000\u011a\u001d\u0001\u0000\u0000\u0000\u011b"+
		"\u0120\u0003$\u0012\u0000\u011c\u011d\u0005\u001d\u0000\u0000\u011d\u011f"+
		"\u0003$\u0012\u0000\u011e\u011c\u0001\u0000\u0000\u0000\u011f\u0122\u0001"+
		"\u0000\u0000\u0000\u0120\u011e\u0001\u0000\u0000\u0000\u0120\u0121\u0001"+
		"\u0000\u0000\u0000\u0121\u001f\u0001\u0000\u0000\u0000\u0122\u0120\u0001"+
		"\u0000\u0000\u0000\u0123\u0126\u0003\u0014\n\u0000\u0124\u0126\u0003\u0002"+
		"\u0001\u0000\u0125\u0123\u0001\u0000\u0000\u0000\u0125\u0124\u0001\u0000"+
		"\u0000\u0000\u0126\u0127\u0001\u0000\u0000\u0000\u0127\u0128\u0005\u0001"+
		"\u0000\u0000\u0128\u012a\u0001\u0000\u0000\u0000\u0129\u0125\u0001\u0000"+
		"\u0000\u0000\u012a\u012d\u0001\u0000\u0000\u0000\u012b\u0129\u0001\u0000"+
		"\u0000\u0000\u012b\u012c\u0001\u0000\u0000\u0000\u012c!\u0001\u0000\u0000"+
		"\u0000\u012d\u012b\u0001\u0000\u0000\u0000\u012e\u0130\u0005\u0006\u0000"+
		"\u0000\u012f\u012e\u0001\u0000\u0000\u0000\u012f\u0130\u0001\u0000\u0000"+
		"\u0000\u0130\u0131\u0001\u0000\u0000\u0000\u0131\u0132\u00059\u0000\u0000"+
		"\u0132\u0135\u0005?\u0000\u0000\u0133\u0134\u0007\u0001\u0000\u0000\u0134"+
		"\u0136\u0003$\u0012\u0000\u0135\u0133\u0001\u0000\u0000\u0000\u0135\u0136"+
		"\u0001\u0000\u0000\u0000\u0136#\u0001\u0000\u0000\u0000\u0137\u0138\u0006"+
		"\u0012\uffff\uffff\u0000\u0138\u0139\u0007\u0004\u0000\u0000\u0139\u013b"+
		"\u0005\u0004\u0000\u0000\u013a\u013c\u0005!\u0000\u0000\u013b\u013a\u0001"+
		"\u0000\u0000\u0000\u013b\u013c\u0001\u0000\u0000\u0000\u013c\u013d\u0001"+
		"\u0000\u0000\u0000\u013d\u0154\u0005\u0005\u0000\u0000\u013e\u0154\u0003"+
		"\u001c\u000e\u0000\u013f\u0140\u0005)\u0000\u0000\u0140\u0154\u0003$\u0012"+
		"\f\u0141\u0142\u00057\u0000\u0000\u0142\u0154\u0003$\u0012\t\u0143\u0144"+
		"\u00058\u0000\u0000\u0144\u0154\u0003$\u0012\b\u0145\u0146\u00059\u0000"+
		"\u0000\u0146\u0147\u0005\u0004\u0000\u0000\u0147\u0148\u0003$\u0012\u0000"+
		"\u0148\u0149\u0005\u0005\u0000\u0000\u0149\u0154\u0001\u0000\u0000\u0000"+
		"\u014a\u014b\u0005\u0004\u0000\u0000\u014b\u014c\u0003$\u0012\u0000\u014c"+
		"\u014d\u0005\u0005\u0000\u0000\u014d\u0154\u0001\u0000\u0000\u0000\u014e"+
		"\u0154\u0005!\u0000\u0000\u014f\u0154\u0005\"\u0000\u0000\u0150\u0154"+
		"\u0005#\u0000\u0000\u0151\u0154\u0005$\u0000\u0000\u0152\u0154\u0005?"+
		"\u0000\u0000\u0153\u0137\u0001\u0000\u0000\u0000\u0153\u013e\u0001\u0000"+
		"\u0000\u0000\u0153\u013f\u0001\u0000\u0000\u0000\u0153\u0141\u0001\u0000"+
		"\u0000\u0000\u0153\u0143\u0001\u0000\u0000\u0000\u0153\u0145\u0001\u0000"+
		"\u0000\u0000\u0153\u014a\u0001\u0000\u0000\u0000\u0153\u014e\u0001\u0000"+
		"\u0000\u0000\u0153\u014f\u0001\u0000\u0000\u0000\u0153\u0150\u0001\u0000"+
		"\u0000\u0000\u0153\u0151\u0001\u0000\u0000\u0000\u0153\u0152\u0001\u0000"+
		"\u0000\u0000\u0154\u016c\u0001\u0000\u0000\u0000\u0155\u0156\n\u0011\u0000"+
		"\u0000\u0156\u0157\u0007\u0005\u0000\u0000\u0157\u016b\u0003$\u0012\u0012"+
		"\u0158\u0159\n\u0010\u0000\u0000\u0159\u015a\u0007\u0006\u0000\u0000\u015a"+
		"\u016b\u0003$\u0012\u0011\u015b\u015c\n\u000f\u0000\u0000\u015c\u015d"+
		"\u0007\u0007\u0000\u0000\u015d\u016b\u0003$\u0012\u0010\u015e\u015f\n"+
		"\u000e\u0000\u0000\u015f\u0160\u0007\u0007\u0000\u0000\u0160\u016b\u0003"+
		"$\u0012\u000f\u0161\u0162\n\r\u0000\u0000\u0162\u0163\u0005,\u0000\u0000"+
		"\u0163\u016b\u0003$\u0012\u000e\u0164\u0165\n\u000b\u0000\u0000\u0165"+
		"\u0166\u00055\u0000\u0000\u0166\u016b\u0003$\u0012\f\u0167\u0168\n\n\u0000"+
		"\u0000\u0168\u0169\u00056\u0000\u0000\u0169\u016b\u0003$\u0012\u000b\u016a"+
		"\u0155\u0001\u0000\u0000\u0000\u016a\u0158\u0001\u0000\u0000\u0000\u016a"+
		"\u015b\u0001\u0000\u0000\u0000\u016a\u015e\u0001\u0000\u0000\u0000\u016a"+
		"\u0161\u0001\u0000\u0000\u0000\u016a\u0164\u0001\u0000\u0000\u0000\u016a"+
		"\u0167\u0001\u0000\u0000\u0000\u016b\u016e\u0001\u0000\u0000\u0000\u016c"+
		"\u016a\u0001\u0000\u0000\u0000\u016c\u016d\u0001\u0000\u0000\u0000\u016d"+
		"%\u0001\u0000\u0000\u0000\u016e\u016c\u0001\u0000\u0000\u0000/(.=EKOW"+
		"ahnr|\u0081\u0085\u0089\u0090\u0094\u0098\u009c\u009e\u00a2\u00a6\u00a8"+
		"\u00af\u00b6\u00bd\u00c4\u00cb\u00d2\u00d8\u00e1\u00e7\u00f2\u00f8\u0102"+
		"\u0104\u010e\u0117\u0120\u0125\u012b\u012f\u0135\u013b\u0153\u016a\u016c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}