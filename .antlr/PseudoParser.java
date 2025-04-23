// Generated from /Users/maciejjamrozy/Studia/Kompilatory/projectPseudo/Pseudo.g4 by ANTLR 4.13.1
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
		T__24=25, T__25=26, T__26=27, STRING=28, NUMBER=29, DOUBLE=30, BOOL=31, 
		ID=32, WS=33, ESC=34, PLUS=35, MINUS=36, MULT=37, DIV=38, EQ=39, GREATER=40, 
		SMALLER=41, EQUAL=42, DIFFERENT=43, TYPE=44, TYPE_INT=45, TYPE_FLOAT=46, 
		TYPE_STRING=47, TYPE_BOOL=48;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_printStatement = 2, RULE_varDeclStatement = 3, 
		RULE_assignmentStatement = 4, RULE_ifStatement = 5, RULE_whileStatement = 6, 
		RULE_forStatement = 7, RULE_functionDefStatement = 8, RULE_paramList = 9, 
		RULE_functionCallStatement = 10, RULE_argumentList = 11, RULE_body = 12, 
		RULE_expr = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "printStatement", "varDeclStatement", "assignmentStatement", 
			"ifStatement", "whileStatement", "forStatement", "functionDefStatement", 
			"paramList", "functionCallStatement", "argumentList", "body", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'print'", "'shout'", "'('", "')'", "'is'", "'<<'", "'<-'", 
			"'if'", "':'", "'else'", "'end'", "'then'", "'while'", "'loop'", "'for'", 
			"'function'", "','", "'input'", "'scan'", "'listen'", "'!'", "'&&'", 
			"'||'", "'not'", "'and'", "'or'", null, null, null, null, null, null, 
			null, "'+'", "'-'", "'*'", "'/'", "'='", "'>'", "'<'", "'=='", "'!='", 
			null, "'int'", "'float'", "'string'", "'boolean'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "STRING", "NUMBER", "DOUBLE", "BOOL", "ID", "WS", 
			"ESC", "PLUS", "MINUS", "MULT", "DIV", "EQ", "GREATER", "SMALLER", "EQUAL", 
			"DIFFERENT", "TYPE", "TYPE_INT", "TYPE_FLOAT", "TYPE_STRING", "TYPE_BOOL"
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
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17596481225228L) != 0)) {
				{
				{
				setState(28);
				statement();
				setState(29);
				match(T__0);
				}
				}
				setState(35);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(36);
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
		public VarDeclStatementContext varDeclStatement() {
			return getRuleContext(VarDeclStatementContext.class,0);
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
		public FunctionDefStatementContext functionDefStatement() {
			return getRuleContext(FunctionDefStatementContext.class,0);
		}
		public FunctionCallStatementContext functionCallStatement() {
			return getRuleContext(FunctionCallStatementContext.class,0);
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
			setState(46);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(38);
				printStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				varDeclStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(40);
				assignmentStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(41);
				ifStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(42);
				whileStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(43);
				forStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(44);
				functionDefStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(45);
				functionCallStatement();
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
		public TerminalNode STRING() { return getToken(PseudoParser.STRING, 0); }
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
			setState(48);
			_la = _input.LA(1);
			if ( !(_la==T__1 || _la==T__2) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(49);
			match(T__3);
			setState(50);
			match(STRING);
			setState(51);
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
	public static class VarDeclStatementContext extends ParserRuleContext {
		public Token op;
		public TerminalNode TYPE() { return getToken(PseudoParser.TYPE, 0); }
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode EQ() { return getToken(PseudoParser.EQ, 0); }
		public VarDeclStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclStatement; }
	}

	public final VarDeclStatementContext varDeclStatement() throws RecognitionException {
		VarDeclStatementContext _localctx = new VarDeclStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_varDeclStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(TYPE);
			setState(54);
			match(ID);
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549755814336L) != 0)) {
				{
				setState(55);
				((VarDeclStatementContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 549755814336L) != 0)) ) {
					((VarDeclStatementContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(56);
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
	public static class AssignmentStatementContext extends ParserRuleContext {
		public Token op;
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode EQ() { return getToken(PseudoParser.EQ, 0); }
		public AssignmentStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentStatement; }
	}

	public final AssignmentStatementContext assignmentStatement() throws RecognitionException {
		AssignmentStatementContext _localctx = new AssignmentStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_assignmentStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(ID);
			setState(60);
			((AssignmentStatementContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 549755814336L) != 0)) ) {
				((AssignmentStatementContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(61);
			expr(0);
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
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<BodyContext> body() {
			return getRuleContexts(BodyContext.class);
		}
		public BodyContext body(int i) {
			return getRuleContext(BodyContext.class,i);
		}
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_ifStatement);
		int _la;
		try {
			setState(119);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(63);
				match(T__8);
				setState(64);
				match(T__3);
				setState(65);
				expr(0);
				setState(66);
				match(T__4);
				setState(67);
				match(T__9);
				setState(68);
				body();
				setState(72);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__10) {
					{
					setState(69);
					match(T__10);
					setState(70);
					match(T__9);
					setState(71);
					body();
					}
				}

				setState(74);
				match(T__11);
				setState(76);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__8) {
					{
					setState(75);
					match(T__8);
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				match(T__8);
				setState(79);
				expr(0);
				setState(80);
				match(T__9);
				setState(81);
				body();
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__10) {
					{
					setState(82);
					match(T__10);
					setState(83);
					match(T__9);
					setState(84);
					body();
					}
				}

				setState(87);
				match(T__11);
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__8) {
					{
					setState(88);
					match(T__8);
					}
				}

				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(91);
				match(T__8);
				setState(92);
				match(T__3);
				setState(93);
				expr(0);
				setState(94);
				match(T__4);
				setState(95);
				match(T__12);
				setState(96);
				body();
				setState(100);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__10) {
					{
					setState(97);
					match(T__10);
					setState(98);
					match(T__9);
					setState(99);
					body();
					}
				}

				setState(102);
				match(T__11);
				setState(104);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__8) {
					{
					setState(103);
					match(T__8);
					}
				}

				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(106);
				match(T__8);
				setState(107);
				expr(0);
				setState(108);
				match(T__12);
				setState(109);
				body();
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__10) {
					{
					setState(110);
					match(T__10);
					setState(111);
					match(T__9);
					setState(112);
					body();
					}
				}

				setState(115);
				match(T__11);
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__8) {
					{
					setState(116);
					match(T__8);
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
		enterRule(_localctx, 12, RULE_whileStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			match(T__13);
			setState(122);
			match(T__3);
			setState(123);
			expr(0);
			setState(124);
			match(T__4);
			setState(125);
			match(T__9);
			setState(126);
			body();
			setState(127);
			match(T__11);
			setState(129);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(128);
				match(T__14);
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
		public Token OP;
		public TerminalNode TYPE_INT() { return getToken(PseudoParser.TYPE_INT, 0); }
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public TerminalNode NUMBER() { return getToken(PseudoParser.NUMBER, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentStatementContext assignmentStatement() {
			return getRuleContext(AssignmentStatementContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode EQ() { return getToken(PseudoParser.EQ, 0); }
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_forStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(T__15);
			setState(132);
			match(T__3);
			setState(133);
			match(TYPE_INT);
			setState(134);
			match(ID);
			setState(135);
			((ForStatementContext)_localctx).OP = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 549755814336L) != 0)) ) {
				((ForStatementContext)_localctx).OP = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(136);
			match(NUMBER);
			setState(137);
			match(T__0);
			setState(138);
			expr(0);
			setState(139);
			match(T__0);
			setState(140);
			assignmentStatement();
			setState(141);
			match(T__4);
			setState(142);
			match(T__9);
			setState(143);
			body();
			setState(144);
			match(T__11);
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(145);
				match(T__14);
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
	public static class FunctionDefStatementContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ParamListContext paramList() {
			return getRuleContext(ParamListContext.class,0);
		}
		public FunctionDefStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDefStatement; }
	}

	public final FunctionDefStatementContext functionDefStatement() throws RecognitionException {
		FunctionDefStatementContext _localctx = new FunctionDefStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_functionDefStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(T__16);
			setState(149);
			match(ID);
			setState(150);
			match(T__3);
			setState(152);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(151);
				paramList();
				}
			}

			setState(154);
			match(T__4);
			setState(155);
			match(T__9);
			setState(156);
			body();
			setState(157);
			match(T__11);
			setState(159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__16) {
				{
				setState(158);
				match(T__16);
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
	public static class ParamListContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(PseudoParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PseudoParser.ID, i);
		}
		public ParamListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramList; }
	}

	public final ParamListContext paramList() throws RecognitionException {
		ParamListContext _localctx = new ParamListContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_paramList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			match(ID);
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__17) {
				{
				{
				setState(162);
				match(T__17);
				setState(163);
				match(ID);
				}
				}
				setState(168);
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
	public static class FunctionCallStatementContext extends ParserRuleContext {
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
		enterRule(_localctx, 20, RULE_functionCallStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(ID);
			setState(170);
			match(T__3);
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8362917904L) != 0)) {
				{
				setState(171);
				argumentList();
				}
			}

			setState(174);
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
		enterRule(_localctx, 22, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			expr(0);
			setState(181);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__17) {
				{
				{
				setState(177);
				match(T__17);
				setState(178);
				expr(0);
				}
				}
				setState(183);
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
		enterRule(_localctx, 24, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17596481225228L) != 0)) {
				{
				{
				setState(184);
				statement();
				setState(185);
				match(T__0);
				}
				}
				setState(191);
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
	public static class ExprContext extends ParserRuleContext {
		public Token op;
		public TerminalNode STRING() { return getToken(PseudoParser.STRING, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode NUMBER() { return getToken(PseudoParser.NUMBER, 0); }
		public TerminalNode DOUBLE() { return getToken(PseudoParser.DOUBLE, 0); }
		public TerminalNode BOOL() { return getToken(PseudoParser.BOOL, 0); }
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public TerminalNode MULT() { return getToken(PseudoParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(PseudoParser.DIV, 0); }
		public TerminalNode PLUS() { return getToken(PseudoParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(PseudoParser.MINUS, 0); }
		public TerminalNode GREATER() { return getToken(PseudoParser.GREATER, 0); }
		public TerminalNode SMALLER() { return getToken(PseudoParser.SMALLER, 0); }
		public TerminalNode EQUAL() { return getToken(PseudoParser.EQUAL, 0); }
		public TerminalNode DIFFERENT() { return getToken(PseudoParser.DIFFERENT, 0); }
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
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__18:
			case T__19:
			case T__20:
				{
				setState(193);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3670016L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(194);
				match(T__3);
				setState(196);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==STRING) {
					{
					setState(195);
					match(STRING);
					}
				}

				setState(198);
				match(T__4);
				}
				break;
			case T__21:
				{
				setState(199);
				match(T__21);
				setState(200);
				expr(12);
				}
				break;
			case T__24:
				{
				setState(201);
				match(T__24);
				setState(202);
				expr(9);
				}
				break;
			case T__3:
				{
				setState(203);
				match(T__3);
				setState(204);
				expr(0);
				setState(205);
				match(T__4);
				}
				break;
			case STRING:
				{
				setState(207);
				match(STRING);
				}
				break;
			case NUMBER:
				{
				setState(208);
				match(NUMBER);
				}
				break;
			case DOUBLE:
				{
				setState(209);
				match(DOUBLE);
				}
				break;
			case BOOL:
				{
				setState(210);
				match(BOOL);
				}
				break;
			case ID:
				{
				setState(211);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(237);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(235);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(214);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(215);
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
						setState(216);
						expr(16);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(217);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(218);
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
						setState(219);
						expr(15);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(220);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(221);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 16492674416640L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(222);
						expr(14);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(223);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(224);
						match(T__22);
						setState(225);
						expr(12);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(226);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(227);
						match(T__23);
						setState(228);
						expr(11);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(229);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(230);
						match(T__25);
						setState(231);
						expr(9);
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(232);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(233);
						match(T__26);
						setState(234);
						expr(8);
						}
						break;
					}
					} 
				}
				setState(239);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
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
		case 13:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 15);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 11);
		case 4:
			return precpred(_ctx, 10);
		case 5:
			return precpred(_ctx, 8);
		case 6:
			return precpred(_ctx, 7);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00010\u00f1\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000"+
		" \b\u0000\n\u0000\f\u0000#\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001/\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0003\u0003:\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005I\b\u0005\u0001\u0005"+
		"\u0001\u0005\u0003\u0005M\b\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005V\b\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005Z\b\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0003\u0005e\b\u0005\u0001\u0005\u0001\u0005\u0003\u0005"+
		"i\b\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005r\b\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005v\b\u0005\u0003\u0005x\b\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003"+
		"\u0006\u0082\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u0093"+
		"\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u0099\b\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0003\b\u00a0\b\b\u0001\t\u0001\t\u0001\t\u0005"+
		"\t\u00a5\b\t\n\t\f\t\u00a8\t\t\u0001\n\u0001\n\u0001\n\u0003\n\u00ad\b"+
		"\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u00b4"+
		"\b\u000b\n\u000b\f\u000b\u00b7\t\u000b\u0001\f\u0001\f\u0001\f\u0005\f"+
		"\u00bc\b\f\n\f\f\f\u00bf\t\f\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00c5"+
		"\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00d5\b\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0005\r\u00ec\b\r\n\r\f\r\u00ef\t\r\u0001\r\u0000\u0001\u001a"+
		"\u000e\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u0000\u0006\u0001\u0000\u0002\u0003\u0002\u0000\u0006\b\'\'\u0001"+
		"\u0000\u0013\u0015\u0001\u0000%&\u0001\u0000#$\u0001\u0000(+\u010e\u0000"+
		"!\u0001\u0000\u0000\u0000\u0002.\u0001\u0000\u0000\u0000\u00040\u0001"+
		"\u0000\u0000\u0000\u00065\u0001\u0000\u0000\u0000\b;\u0001\u0000\u0000"+
		"\u0000\nw\u0001\u0000\u0000\u0000\fy\u0001\u0000\u0000\u0000\u000e\u0083"+
		"\u0001\u0000\u0000\u0000\u0010\u0094\u0001\u0000\u0000\u0000\u0012\u00a1"+
		"\u0001\u0000\u0000\u0000\u0014\u00a9\u0001\u0000\u0000\u0000\u0016\u00b0"+
		"\u0001\u0000\u0000\u0000\u0018\u00bd\u0001\u0000\u0000\u0000\u001a\u00d4"+
		"\u0001\u0000\u0000\u0000\u001c\u001d\u0003\u0002\u0001\u0000\u001d\u001e"+
		"\u0005\u0001\u0000\u0000\u001e \u0001\u0000\u0000\u0000\u001f\u001c\u0001"+
		"\u0000\u0000\u0000 #\u0001\u0000\u0000\u0000!\u001f\u0001\u0000\u0000"+
		"\u0000!\"\u0001\u0000\u0000\u0000\"$\u0001\u0000\u0000\u0000#!\u0001\u0000"+
		"\u0000\u0000$%\u0005\u0000\u0000\u0001%\u0001\u0001\u0000\u0000\u0000"+
		"&/\u0003\u0004\u0002\u0000\'/\u0003\u0006\u0003\u0000(/\u0003\b\u0004"+
		"\u0000)/\u0003\n\u0005\u0000*/\u0003\f\u0006\u0000+/\u0003\u000e\u0007"+
		"\u0000,/\u0003\u0010\b\u0000-/\u0003\u0014\n\u0000.&\u0001\u0000\u0000"+
		"\u0000.\'\u0001\u0000\u0000\u0000.(\u0001\u0000\u0000\u0000.)\u0001\u0000"+
		"\u0000\u0000.*\u0001\u0000\u0000\u0000.+\u0001\u0000\u0000\u0000.,\u0001"+
		"\u0000\u0000\u0000.-\u0001\u0000\u0000\u0000/\u0003\u0001\u0000\u0000"+
		"\u000001\u0007\u0000\u0000\u000012\u0005\u0004\u0000\u000023\u0005\u001c"+
		"\u0000\u000034\u0005\u0005\u0000\u00004\u0005\u0001\u0000\u0000\u0000"+
		"56\u0005,\u0000\u000069\u0005 \u0000\u000078\u0007\u0001\u0000\u00008"+
		":\u0003\u001a\r\u000097\u0001\u0000\u0000\u00009:\u0001\u0000\u0000\u0000"+
		":\u0007\u0001\u0000\u0000\u0000;<\u0005 \u0000\u0000<=\u0007\u0001\u0000"+
		"\u0000=>\u0003\u001a\r\u0000>\t\u0001\u0000\u0000\u0000?@\u0005\t\u0000"+
		"\u0000@A\u0005\u0004\u0000\u0000AB\u0003\u001a\r\u0000BC\u0005\u0005\u0000"+
		"\u0000CD\u0005\n\u0000\u0000DH\u0003\u0018\f\u0000EF\u0005\u000b\u0000"+
		"\u0000FG\u0005\n\u0000\u0000GI\u0003\u0018\f\u0000HE\u0001\u0000\u0000"+
		"\u0000HI\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000JL\u0005\f\u0000"+
		"\u0000KM\u0005\t\u0000\u0000LK\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000"+
		"\u0000Mx\u0001\u0000\u0000\u0000NO\u0005\t\u0000\u0000OP\u0003\u001a\r"+
		"\u0000PQ\u0005\n\u0000\u0000QU\u0003\u0018\f\u0000RS\u0005\u000b\u0000"+
		"\u0000ST\u0005\n\u0000\u0000TV\u0003\u0018\f\u0000UR\u0001\u0000\u0000"+
		"\u0000UV\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000WY\u0005\f\u0000"+
		"\u0000XZ\u0005\t\u0000\u0000YX\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000"+
		"\u0000Zx\u0001\u0000\u0000\u0000[\\\u0005\t\u0000\u0000\\]\u0005\u0004"+
		"\u0000\u0000]^\u0003\u001a\r\u0000^_\u0005\u0005\u0000\u0000_`\u0005\r"+
		"\u0000\u0000`d\u0003\u0018\f\u0000ab\u0005\u000b\u0000\u0000bc\u0005\n"+
		"\u0000\u0000ce\u0003\u0018\f\u0000da\u0001\u0000\u0000\u0000de\u0001\u0000"+
		"\u0000\u0000ef\u0001\u0000\u0000\u0000fh\u0005\f\u0000\u0000gi\u0005\t"+
		"\u0000\u0000hg\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ix\u0001"+
		"\u0000\u0000\u0000jk\u0005\t\u0000\u0000kl\u0003\u001a\r\u0000lm\u0005"+
		"\r\u0000\u0000mq\u0003\u0018\f\u0000no\u0005\u000b\u0000\u0000op\u0005"+
		"\n\u0000\u0000pr\u0003\u0018\f\u0000qn\u0001\u0000\u0000\u0000qr\u0001"+
		"\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000su\u0005\f\u0000\u0000tv\u0005"+
		"\t\u0000\u0000ut\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000vx\u0001"+
		"\u0000\u0000\u0000w?\u0001\u0000\u0000\u0000wN\u0001\u0000\u0000\u0000"+
		"w[\u0001\u0000\u0000\u0000wj\u0001\u0000\u0000\u0000x\u000b\u0001\u0000"+
		"\u0000\u0000yz\u0005\u000e\u0000\u0000z{\u0005\u0004\u0000\u0000{|\u0003"+
		"\u001a\r\u0000|}\u0005\u0005\u0000\u0000}~\u0005\n\u0000\u0000~\u007f"+
		"\u0003\u0018\f\u0000\u007f\u0081\u0005\f\u0000\u0000\u0080\u0082\u0005"+
		"\u000f\u0000\u0000\u0081\u0080\u0001\u0000\u0000\u0000\u0081\u0082\u0001"+
		"\u0000\u0000\u0000\u0082\r\u0001\u0000\u0000\u0000\u0083\u0084\u0005\u0010"+
		"\u0000\u0000\u0084\u0085\u0005\u0004\u0000\u0000\u0085\u0086\u0005-\u0000"+
		"\u0000\u0086\u0087\u0005 \u0000\u0000\u0087\u0088\u0007\u0001\u0000\u0000"+
		"\u0088\u0089\u0005\u001d\u0000\u0000\u0089\u008a\u0005\u0001\u0000\u0000"+
		"\u008a\u008b\u0003\u001a\r\u0000\u008b\u008c\u0005\u0001\u0000\u0000\u008c"+
		"\u008d\u0003\b\u0004\u0000\u008d\u008e\u0005\u0005\u0000\u0000\u008e\u008f"+
		"\u0005\n\u0000\u0000\u008f\u0090\u0003\u0018\f\u0000\u0090\u0092\u0005"+
		"\f\u0000\u0000\u0091\u0093\u0005\u000f\u0000\u0000\u0092\u0091\u0001\u0000"+
		"\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093\u000f\u0001\u0000"+
		"\u0000\u0000\u0094\u0095\u0005\u0011\u0000\u0000\u0095\u0096\u0005 \u0000"+
		"\u0000\u0096\u0098\u0005\u0004\u0000\u0000\u0097\u0099\u0003\u0012\t\u0000"+
		"\u0098\u0097\u0001\u0000\u0000\u0000\u0098\u0099\u0001\u0000\u0000\u0000"+
		"\u0099\u009a\u0001\u0000\u0000\u0000\u009a\u009b\u0005\u0005\u0000\u0000"+
		"\u009b\u009c\u0005\n\u0000\u0000\u009c\u009d\u0003\u0018\f\u0000\u009d"+
		"\u009f\u0005\f\u0000\u0000\u009e\u00a0\u0005\u0011\u0000\u0000\u009f\u009e"+
		"\u0001\u0000\u0000\u0000\u009f\u00a0\u0001\u0000\u0000\u0000\u00a0\u0011"+
		"\u0001\u0000\u0000\u0000\u00a1\u00a6\u0005 \u0000\u0000\u00a2\u00a3\u0005"+
		"\u0012\u0000\u0000\u00a3\u00a5\u0005 \u0000\u0000\u00a4\u00a2\u0001\u0000"+
		"\u0000\u0000\u00a5\u00a8\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001\u0000"+
		"\u0000\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000\u00a7\u0013\u0001\u0000"+
		"\u0000\u0000\u00a8\u00a6\u0001\u0000\u0000\u0000\u00a9\u00aa\u0005 \u0000"+
		"\u0000\u00aa\u00ac\u0005\u0004\u0000\u0000\u00ab\u00ad\u0003\u0016\u000b"+
		"\u0000\u00ac\u00ab\u0001\u0000\u0000\u0000\u00ac\u00ad\u0001\u0000\u0000"+
		"\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000\u00ae\u00af\u0005\u0005\u0000"+
		"\u0000\u00af\u0015\u0001\u0000\u0000\u0000\u00b0\u00b5\u0003\u001a\r\u0000"+
		"\u00b1\u00b2\u0005\u0012\u0000\u0000\u00b2\u00b4\u0003\u001a\r\u0000\u00b3"+
		"\u00b1\u0001\u0000\u0000\u0000\u00b4\u00b7\u0001\u0000\u0000\u0000\u00b5"+
		"\u00b3\u0001\u0000\u0000\u0000\u00b5\u00b6\u0001\u0000\u0000\u0000\u00b6"+
		"\u0017\u0001\u0000\u0000\u0000\u00b7\u00b5\u0001\u0000\u0000\u0000\u00b8"+
		"\u00b9\u0003\u0002\u0001\u0000\u00b9\u00ba\u0005\u0001\u0000\u0000\u00ba"+
		"\u00bc\u0001\u0000\u0000\u0000\u00bb\u00b8\u0001\u0000\u0000\u0000\u00bc"+
		"\u00bf\u0001\u0000\u0000\u0000\u00bd\u00bb\u0001\u0000\u0000\u0000\u00bd"+
		"\u00be\u0001\u0000\u0000\u0000\u00be\u0019\u0001\u0000\u0000\u0000\u00bf"+
		"\u00bd\u0001\u0000\u0000\u0000\u00c0\u00c1\u0006\r\uffff\uffff\u0000\u00c1"+
		"\u00c2\u0007\u0002\u0000\u0000\u00c2\u00c4\u0005\u0004\u0000\u0000\u00c3"+
		"\u00c5\u0005\u001c\u0000\u0000\u00c4\u00c3\u0001\u0000\u0000\u0000\u00c4"+
		"\u00c5\u0001\u0000\u0000\u0000\u00c5\u00c6\u0001\u0000\u0000\u0000\u00c6"+
		"\u00d5\u0005\u0005\u0000\u0000\u00c7\u00c8\u0005\u0016\u0000\u0000\u00c8"+
		"\u00d5\u0003\u001a\r\f\u00c9\u00ca\u0005\u0019\u0000\u0000\u00ca\u00d5"+
		"\u0003\u001a\r\t\u00cb\u00cc\u0005\u0004\u0000\u0000\u00cc\u00cd\u0003"+
		"\u001a\r\u0000\u00cd\u00ce\u0005\u0005\u0000\u0000\u00ce\u00d5\u0001\u0000"+
		"\u0000\u0000\u00cf\u00d5\u0005\u001c\u0000\u0000\u00d0\u00d5\u0005\u001d"+
		"\u0000\u0000\u00d1\u00d5\u0005\u001e\u0000\u0000\u00d2\u00d5\u0005\u001f"+
		"\u0000\u0000\u00d3\u00d5\u0005 \u0000\u0000\u00d4\u00c0\u0001\u0000\u0000"+
		"\u0000\u00d4\u00c7\u0001\u0000\u0000\u0000\u00d4\u00c9\u0001\u0000\u0000"+
		"\u0000\u00d4\u00cb\u0001\u0000\u0000\u0000\u00d4\u00cf\u0001\u0000\u0000"+
		"\u0000\u00d4\u00d0\u0001\u0000\u0000\u0000\u00d4\u00d1\u0001\u0000\u0000"+
		"\u0000\u00d4\u00d2\u0001\u0000\u0000\u0000\u00d4\u00d3\u0001\u0000\u0000"+
		"\u0000\u00d5\u00ed\u0001\u0000\u0000\u0000\u00d6\u00d7\n\u000f\u0000\u0000"+
		"\u00d7\u00d8\u0007\u0003\u0000\u0000\u00d8\u00ec\u0003\u001a\r\u0010\u00d9"+
		"\u00da\n\u000e\u0000\u0000\u00da\u00db\u0007\u0004\u0000\u0000\u00db\u00ec"+
		"\u0003\u001a\r\u000f\u00dc\u00dd\n\r\u0000\u0000\u00dd\u00de\u0007\u0005"+
		"\u0000\u0000\u00de\u00ec\u0003\u001a\r\u000e\u00df\u00e0\n\u000b\u0000"+
		"\u0000\u00e0\u00e1\u0005\u0017\u0000\u0000\u00e1\u00ec\u0003\u001a\r\f"+
		"\u00e2\u00e3\n\n\u0000\u0000\u00e3\u00e4\u0005\u0018\u0000\u0000\u00e4"+
		"\u00ec\u0003\u001a\r\u000b\u00e5\u00e6\n\b\u0000\u0000\u00e6\u00e7\u0005"+
		"\u001a\u0000\u0000\u00e7\u00ec\u0003\u001a\r\t\u00e8\u00e9\n\u0007\u0000"+
		"\u0000\u00e9\u00ea\u0005\u001b\u0000\u0000\u00ea\u00ec\u0003\u001a\r\b"+
		"\u00eb\u00d6\u0001\u0000\u0000\u0000\u00eb\u00d9\u0001\u0000\u0000\u0000"+
		"\u00eb\u00dc\u0001\u0000\u0000\u0000\u00eb\u00df\u0001\u0000\u0000\u0000"+
		"\u00eb\u00e2\u0001\u0000\u0000\u0000\u00eb\u00e5\u0001\u0000\u0000\u0000"+
		"\u00eb\u00e8\u0001\u0000\u0000\u0000\u00ec\u00ef\u0001\u0000\u0000\u0000"+
		"\u00ed\u00eb\u0001\u0000\u0000\u0000\u00ed\u00ee\u0001\u0000\u0000\u0000"+
		"\u00ee\u001b\u0001\u0000\u0000\u0000\u00ef\u00ed\u0001\u0000\u0000\u0000"+
		"\u0018!.9HLUYdhquw\u0081\u0092\u0098\u009f\u00a6\u00ac\u00b5\u00bd\u00c4"+
		"\u00d4\u00eb\u00ed";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}