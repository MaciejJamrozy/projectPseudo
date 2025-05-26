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
		T__24=25, T__25=26, STRING=27, NUMBER=28, DOUBLE=29, BOOL=30, WS=31, PLUS=32, 
		MINUS=33, MULT=34, DIV=35, INTDIV=36, GREATER=37, SMALLER=38, EQUAL=39, 
		DIFFERENT=40, AND=41, OR=42, NOT=43, TYPE=44, TYPE_INT=45, TYPE_FLOAT=46, 
		TYPE_STRING=47, TYPE_BOOL=48, TYPE_VOID=49, ID=50;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_printStatement = 2, RULE_assignmentStatement = 3, 
		RULE_ifStatement = 4, RULE_whileStatement = 5, RULE_forStatement = 6, 
		RULE_functionDef = 7, RULE_returnStatement = 8, RULE_paramList = 9, RULE_param = 10, 
		RULE_functionCallStatement = 11, RULE_argumentList = 12, RULE_body = 13, 
		RULE_varDeclStatement = 14, RULE_expr = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "printStatement", "assignmentStatement", "ifStatement", 
			"whileStatement", "forStatement", "functionDef", "returnStatement", "paramList", 
			"param", "functionCallStatement", "argumentList", "body", "varDeclStatement", 
			"expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'print'", "'shout'", "'('", "')'", "'='", "'is'", "'<<'", 
			"'<-'", "'if'", "':'", "'else'", "'end'", "'then'", "'while'", "'loop'", 
			"'for'", "'function'", "'fun'", "'def'", "'->'", "'return'", "','", "'input'", 
			"'scan'", "'listen'", null, null, null, null, null, "'+'", "'-'", "'*'", 
			"'/'", "'//'", null, null, null, null, null, null, null, null, "'int'", 
			"'float'", "'string'", "'boolean'", "'void'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "STRING", "NUMBER", "DOUBLE", "BOOL", "WS", "PLUS", 
			"MINUS", "MULT", "DIV", "INTDIV", "GREATER", "SMALLER", "EQUAL", "DIFFERENT", 
			"AND", "OR", "NOT", "TYPE", "TYPE_INT", "TYPE_FLOAT", "TYPE_STRING", 
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
			setState(40);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1143492099089420L) != 0)) {
				{
				{
				setState(34);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__12:
				case T__17:
				case T__18:
				case T__19:
					{
					setState(32);
					functionDef();
					}
					break;
				case T__1:
				case T__2:
				case T__9:
				case T__14:
				case T__16:
				case T__21:
				case TYPE:
				case ID:
					{
					setState(33);
					statement();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(36);
				match(T__0);
				}
				}
				setState(42);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(43);
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
			setState(53);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				printStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(46);
				assignmentStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(47);
				ifStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(48);
				whileStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(49);
				forStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(50);
				functionCallStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(51);
				returnStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(52);
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
			setState(55);
			_la = _input.LA(1);
			if ( !(_la==T__1 || _la==T__2) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(56);
			match(T__3);
			setState(57);
			expr(0);
			setState(58);
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
		public Token op;
		public TerminalNode ID() { return getToken(PseudoParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
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
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(ID);
			setState(61);
			((AssignmentStatementContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 960L) != 0)) ) {
				((AssignmentStatementContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(62);
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
		enterRule(_localctx, 8, RULE_ifStatement);
		int _la;
		try {
			setState(120);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(64);
				match(T__9);
				setState(65);
				match(T__3);
				setState(66);
				expr(0);
				setState(67);
				match(T__4);
				setState(68);
				match(T__10);
				setState(69);
				body();
				setState(73);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__11) {
					{
					setState(70);
					match(T__11);
					setState(71);
					match(T__10);
					setState(72);
					body();
					}
				}

				setState(75);
				match(T__12);
				setState(77);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__9) {
					{
					setState(76);
					match(T__9);
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				match(T__9);
				setState(80);
				expr(0);
				setState(81);
				match(T__10);
				setState(82);
				body();
				setState(86);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__11) {
					{
					setState(83);
					match(T__11);
					setState(84);
					match(T__10);
					setState(85);
					body();
					}
				}

				setState(88);
				match(T__12);
				setState(90);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__9) {
					{
					setState(89);
					match(T__9);
					}
				}

				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(92);
				match(T__9);
				setState(93);
				match(T__3);
				setState(94);
				expr(0);
				setState(95);
				match(T__4);
				setState(96);
				match(T__13);
				setState(97);
				body();
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__11) {
					{
					setState(98);
					match(T__11);
					setState(99);
					match(T__10);
					setState(100);
					body();
					}
				}

				setState(103);
				match(T__12);
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__9) {
					{
					setState(104);
					match(T__9);
					}
				}

				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(107);
				match(T__9);
				setState(108);
				expr(0);
				setState(109);
				match(T__13);
				setState(110);
				body();
				setState(114);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__11) {
					{
					setState(111);
					match(T__11);
					setState(112);
					match(T__10);
					setState(113);
					body();
					}
				}

				setState(116);
				match(T__12);
				setState(118);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__9) {
					{
					setState(117);
					match(T__9);
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
		enterRule(_localctx, 10, RULE_whileStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(T__14);
			setState(123);
			match(T__3);
			setState(124);
			expr(0);
			setState(125);
			match(T__4);
			setState(126);
			match(T__10);
			setState(127);
			body();
			setState(128);
			match(T__12);
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__15) {
				{
				setState(129);
				match(T__15);
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
		public TerminalNode TYPE() { return getToken(PseudoParser.TYPE, 0); }
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
			setState(174);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(132);
				match(T__16);
				setState(133);
				match(T__3);
				setState(134);
				match(TYPE);
				setState(135);
				match(ID);
				setState(136);
				((ForStatementContext)_localctx).OP = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 960L) != 0)) ) {
					((ForStatementContext)_localctx).OP = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(137);
				match(NUMBER);
				setState(138);
				match(T__0);
				setState(139);
				expr(0);
				setState(140);
				match(T__0);
				setState(141);
				assignmentStatement();
				setState(142);
				match(T__4);
				setState(143);
				match(T__10);
				setState(144);
				body();
				setState(145);
				match(T__12);
				setState(147);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__15) {
					{
					setState(146);
					match(T__15);
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(149);
				match(T__16);
				setState(150);
				match(T__3);
				setState(151);
				match(T__0);
				setState(152);
				expr(0);
				setState(153);
				match(T__0);
				setState(154);
				assignmentStatement();
				setState(155);
				match(T__4);
				setState(156);
				match(T__10);
				setState(157);
				body();
				setState(158);
				match(T__12);
				setState(160);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__15) {
					{
					setState(159);
					match(T__15);
					}
				}

				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(162);
				match(T__16);
				setState(163);
				match(T__3);
				setState(164);
				match(T__0);
				setState(165);
				expr(0);
				setState(166);
				match(T__0);
				setState(167);
				match(T__4);
				setState(168);
				match(T__10);
				setState(169);
				body();
				setState(170);
				match(T__12);
				setState(172);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__15) {
					{
					setState(171);
					match(T__15);
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
		enterRule(_localctx, 14, RULE_functionDef);
		int _la;
		try {
			setState(266);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(176);
				match(T__17);
				setState(177);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(178);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(179);
				match(T__3);
				setState(181);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(180);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(183);
				match(T__4);
				setState(184);
				match(T__10);
				setState(185);
				((FunctionDefContext)_localctx).block = body();
				setState(186);
				match(T__12);
				setState(188);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__17) {
					{
					setState(187);
					match(T__17);
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(190);
				match(T__18);
				setState(191);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(192);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(193);
				match(T__3);
				setState(195);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(194);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(197);
				match(T__4);
				setState(198);
				match(T__10);
				setState(199);
				((FunctionDefContext)_localctx).block = body();
				setState(200);
				match(T__12);
				setState(202);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__18) {
					{
					setState(201);
					match(T__18);
					}
				}

				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(204);
				match(T__19);
				setState(205);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(206);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(207);
				match(T__3);
				setState(209);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(208);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(211);
				match(T__4);
				setState(212);
				match(T__10);
				setState(213);
				((FunctionDefContext)_localctx).block = body();
				setState(214);
				match(T__12);
				setState(216);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__19) {
					{
					setState(215);
					match(T__19);
					}
				}

				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(218);
				match(T__17);
				setState(219);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(220);
				match(T__3);
				setState(222);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(221);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(224);
				match(T__4);
				setState(225);
				match(T__20);
				setState(226);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(227);
				match(T__10);
				setState(228);
				((FunctionDefContext)_localctx).block = body();
				setState(229);
				match(T__12);
				setState(231);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__17) {
					{
					setState(230);
					match(T__17);
					}
				}

				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(233);
				match(T__18);
				setState(234);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(235);
				match(T__3);
				setState(237);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(236);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(239);
				match(T__4);
				setState(240);
				match(T__20);
				setState(241);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(242);
				match(T__10);
				setState(243);
				((FunctionDefContext)_localctx).block = body();
				setState(244);
				match(T__0);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(246);
				match(T__12);
				setState(248);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__18) {
					{
					setState(247);
					match(T__18);
					}
				}

				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(250);
				match(T__19);
				setState(251);
				((FunctionDefContext)_localctx).name = match(ID);
				setState(252);
				match(T__3);
				setState(254);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==TYPE) {
					{
					setState(253);
					((FunctionDefContext)_localctx).params = paramList();
					}
				}

				setState(256);
				match(T__4);
				setState(257);
				match(T__20);
				setState(258);
				((FunctionDefContext)_localctx).type = match(TYPE);
				setState(259);
				match(T__10);
				setState(260);
				((FunctionDefContext)_localctx).block = body();
				setState(261);
				match(T__0);
				setState(262);
				match(T__12);
				setState(264);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__19) {
					{
					setState(263);
					match(T__19);
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
		enterRule(_localctx, 16, RULE_returnStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			match(T__21);
			setState(269);
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
		enterRule(_localctx, 18, RULE_paramList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			param();
			setState(276);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__22) {
				{
				{
				setState(272);
				match(T__22);
				setState(273);
				param();
				}
				}
				setState(278);
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
		enterRule(_localctx, 20, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(279);
			((ParamContext)_localctx).type = match(TYPE);
			setState(280);
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
		enterRule(_localctx, 22, RULE_functionCallStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(282);
			((FunctionCallStatementContext)_localctx).name = match(ID);
			setState(283);
			match(T__3);
			setState(285);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1134698130571280L) != 0)) {
				{
				setState(284);
				((FunctionCallStatementContext)_localctx).args = argumentList();
				}
			}

			setState(287);
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
		enterRule(_localctx, 24, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(289);
			expr(0);
			setState(294);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__22) {
				{
				{
				setState(290);
				match(T__22);
				setState(291);
				expr(0);
				}
				}
				setState(296);
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
		enterRule(_localctx, 26, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(302);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1143492097246220L) != 0)) {
				{
				{
				setState(297);
				statement();
				setState(298);
				match(T__0);
				}
				}
				setState(304);
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
	public static class VarDeclStatementContext extends ParserRuleContext {
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
		enterRule(_localctx, 28, RULE_varDeclStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(305);
			match(TYPE);
			setState(306);
			match(ID);
			setState(309);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 960L) != 0)) {
				{
				setState(307);
				((VarDeclStatementContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 960L) != 0)) ) {
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
		public TerminalNode NOT() { return getToken(PseudoParser.NOT, 0); }
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
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(330);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				{
				setState(312);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 117440512L) != 0)) ) {
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
				((ExprContext)_localctx).op = match(NOT);
				setState(320);
				expr(7);
				}
				break;
			case 4:
				{
				setState(321);
				match(T__3);
				setState(322);
				expr(0);
				setState(323);
				match(T__4);
				}
				break;
			case 5:
				{
				setState(325);
				match(STRING);
				}
				break;
			case 6:
				{
				setState(326);
				match(NUMBER);
				}
				break;
			case 7:
				{
				setState(327);
				match(DOUBLE);
				}
				break;
			case 8:
				{
				setState(328);
				match(BOOL);
				}
				break;
			case 9:
				{
				setState(329);
				match(ID);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(352);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(350);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(332);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(333);
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
						setState(334);
						expr(14);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(335);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(336);
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
						setState(337);
						expr(13);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(338);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(339);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2061584302080L) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(340);
						expr(12);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(341);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(342);
						((ExprContext)_localctx).op = match(INTDIV);
						setState(343);
						expr(11);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(344);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(345);
						match(AND);
						setState(346);
						expr(10);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(347);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(348);
						match(OR);
						setState(349);
						expr(9);
						}
						break;
					}
					} 
				}
				setState(354);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
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
		case 15:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 13);
		case 1:
			return precpred(_ctx, 12);
		case 2:
			return precpred(_ctx, 11);
		case 3:
			return precpred(_ctx, 10);
		case 4:
			return precpred(_ctx, 9);
		case 5:
			return precpred(_ctx, 8);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00012\u0164\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0001\u0000\u0001\u0000\u0003\u0000#\b\u0000\u0001\u0000\u0001\u0000"+
		"\u0005\u0000\'\b\u0000\n\u0000\f\u0000*\t\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u00016\b\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004J\b\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u0004N\b\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004"+
		"W\b\u0004\u0001\u0004\u0001\u0004\u0003\u0004[\b\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0003\u0004f\b\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004j\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0003\u0004s\b\u0004\u0001\u0004\u0001"+
		"\u0004\u0003\u0004w\b\u0004\u0003\u0004y\b\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005\u0083\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"\u0094\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006\u00a1\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006\u00ad\b\u0006\u0003\u0006\u00af\b\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u00b6\b\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u00bd"+
		"\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003"+
		"\u0007\u00c4\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0003\u0007\u00cb\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0003\u0007\u00d2\b\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u00d9\b\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u00df\b\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003"+
		"\u0007\u00e8\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003"+
		"\u0007\u00ee\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u00f9"+
		"\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u00ff"+
		"\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u0109\b\u0007\u0003\u0007\u010b"+
		"\b\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0005\t\u0113"+
		"\b\t\n\t\f\t\u0116\t\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0003\u000b\u011e\b\u000b\u0001\u000b\u0001\u000b\u0001\f"+
		"\u0001\f\u0001\f\u0005\f\u0125\b\f\n\f\f\f\u0128\t\f\u0001\r\u0001\r\u0001"+
		"\r\u0005\r\u012d\b\r\n\r\f\r\u0130\t\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0003\u000e\u0136\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0003\u000f\u013c\b\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u014b\b\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0005\u000f\u015f\b\u000f\n\u000f\f\u000f\u0162\t\u000f\u0001\u000f\u0000"+
		"\u0001\u001e\u0010\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e\u0000\u0006\u0001\u0000\u0002\u0003\u0001"+
		"\u0000\u0006\t\u0001\u0000\u0018\u001a\u0001\u0000\"#\u0001\u0000 !\u0001"+
		"\u0000%(\u0193\u0000(\u0001\u0000\u0000\u0000\u00025\u0001\u0000\u0000"+
		"\u0000\u00047\u0001\u0000\u0000\u0000\u0006<\u0001\u0000\u0000\u0000\b"+
		"x\u0001\u0000\u0000\u0000\nz\u0001\u0000\u0000\u0000\f\u00ae\u0001\u0000"+
		"\u0000\u0000\u000e\u010a\u0001\u0000\u0000\u0000\u0010\u010c\u0001\u0000"+
		"\u0000\u0000\u0012\u010f\u0001\u0000\u0000\u0000\u0014\u0117\u0001\u0000"+
		"\u0000\u0000\u0016\u011a\u0001\u0000\u0000\u0000\u0018\u0121\u0001\u0000"+
		"\u0000\u0000\u001a\u012e\u0001\u0000\u0000\u0000\u001c\u0131\u0001\u0000"+
		"\u0000\u0000\u001e\u014a\u0001\u0000\u0000\u0000 #\u0003\u000e\u0007\u0000"+
		"!#\u0003\u0002\u0001\u0000\" \u0001\u0000\u0000\u0000\"!\u0001\u0000\u0000"+
		"\u0000#$\u0001\u0000\u0000\u0000$%\u0005\u0001\u0000\u0000%\'\u0001\u0000"+
		"\u0000\u0000&\"\u0001\u0000\u0000\u0000\'*\u0001\u0000\u0000\u0000(&\u0001"+
		"\u0000\u0000\u0000()\u0001\u0000\u0000\u0000)+\u0001\u0000\u0000\u0000"+
		"*(\u0001\u0000\u0000\u0000+,\u0005\u0000\u0000\u0001,\u0001\u0001\u0000"+
		"\u0000\u0000-6\u0003\u0004\u0002\u0000.6\u0003\u0006\u0003\u0000/6\u0003"+
		"\b\u0004\u000006\u0003\n\u0005\u000016\u0003\f\u0006\u000026\u0003\u0016"+
		"\u000b\u000036\u0003\u0010\b\u000046\u0003\u001c\u000e\u00005-\u0001\u0000"+
		"\u0000\u00005.\u0001\u0000\u0000\u00005/\u0001\u0000\u0000\u000050\u0001"+
		"\u0000\u0000\u000051\u0001\u0000\u0000\u000052\u0001\u0000\u0000\u0000"+
		"53\u0001\u0000\u0000\u000054\u0001\u0000\u0000\u00006\u0003\u0001\u0000"+
		"\u0000\u000078\u0007\u0000\u0000\u000089\u0005\u0004\u0000\u00009:\u0003"+
		"\u001e\u000f\u0000:;\u0005\u0005\u0000\u0000;\u0005\u0001\u0000\u0000"+
		"\u0000<=\u00052\u0000\u0000=>\u0007\u0001\u0000\u0000>?\u0003\u001e\u000f"+
		"\u0000?\u0007\u0001\u0000\u0000\u0000@A\u0005\n\u0000\u0000AB\u0005\u0004"+
		"\u0000\u0000BC\u0003\u001e\u000f\u0000CD\u0005\u0005\u0000\u0000DE\u0005"+
		"\u000b\u0000\u0000EI\u0003\u001a\r\u0000FG\u0005\f\u0000\u0000GH\u0005"+
		"\u000b\u0000\u0000HJ\u0003\u001a\r\u0000IF\u0001\u0000\u0000\u0000IJ\u0001"+
		"\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000KM\u0005\r\u0000\u0000LN\u0005"+
		"\n\u0000\u0000ML\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000Ny\u0001"+
		"\u0000\u0000\u0000OP\u0005\n\u0000\u0000PQ\u0003\u001e\u000f\u0000QR\u0005"+
		"\u000b\u0000\u0000RV\u0003\u001a\r\u0000ST\u0005\f\u0000\u0000TU\u0005"+
		"\u000b\u0000\u0000UW\u0003\u001a\r\u0000VS\u0001\u0000\u0000\u0000VW\u0001"+
		"\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000XZ\u0005\r\u0000\u0000Y[\u0005"+
		"\n\u0000\u0000ZY\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000\u0000[y\u0001"+
		"\u0000\u0000\u0000\\]\u0005\n\u0000\u0000]^\u0005\u0004\u0000\u0000^_"+
		"\u0003\u001e\u000f\u0000_`\u0005\u0005\u0000\u0000`a\u0005\u000e\u0000"+
		"\u0000ae\u0003\u001a\r\u0000bc\u0005\f\u0000\u0000cd\u0005\u000b\u0000"+
		"\u0000df\u0003\u001a\r\u0000eb\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000"+
		"\u0000fg\u0001\u0000\u0000\u0000gi\u0005\r\u0000\u0000hj\u0005\n\u0000"+
		"\u0000ih\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000jy\u0001\u0000"+
		"\u0000\u0000kl\u0005\n\u0000\u0000lm\u0003\u001e\u000f\u0000mn\u0005\u000e"+
		"\u0000\u0000nr\u0003\u001a\r\u0000op\u0005\f\u0000\u0000pq\u0005\u000b"+
		"\u0000\u0000qs\u0003\u001a\r\u0000ro\u0001\u0000\u0000\u0000rs\u0001\u0000"+
		"\u0000\u0000st\u0001\u0000\u0000\u0000tv\u0005\r\u0000\u0000uw\u0005\n"+
		"\u0000\u0000vu\u0001\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000wy\u0001"+
		"\u0000\u0000\u0000x@\u0001\u0000\u0000\u0000xO\u0001\u0000\u0000\u0000"+
		"x\\\u0001\u0000\u0000\u0000xk\u0001\u0000\u0000\u0000y\t\u0001\u0000\u0000"+
		"\u0000z{\u0005\u000f\u0000\u0000{|\u0005\u0004\u0000\u0000|}\u0003\u001e"+
		"\u000f\u0000}~\u0005\u0005\u0000\u0000~\u007f\u0005\u000b\u0000\u0000"+
		"\u007f\u0080\u0003\u001a\r\u0000\u0080\u0082\u0005\r\u0000\u0000\u0081"+
		"\u0083\u0005\u0010\u0000\u0000\u0082\u0081\u0001\u0000\u0000\u0000\u0082"+
		"\u0083\u0001\u0000\u0000\u0000\u0083\u000b\u0001\u0000\u0000\u0000\u0084"+
		"\u0085\u0005\u0011\u0000\u0000\u0085\u0086\u0005\u0004\u0000\u0000\u0086"+
		"\u0087\u0005,\u0000\u0000\u0087\u0088\u00052\u0000\u0000\u0088\u0089\u0007"+
		"\u0001\u0000\u0000\u0089\u008a\u0005\u001c\u0000\u0000\u008a\u008b\u0005"+
		"\u0001\u0000\u0000\u008b\u008c\u0003\u001e\u000f\u0000\u008c\u008d\u0005"+
		"\u0001\u0000\u0000\u008d\u008e\u0003\u0006\u0003\u0000\u008e\u008f\u0005"+
		"\u0005\u0000\u0000\u008f\u0090\u0005\u000b\u0000\u0000\u0090\u0091\u0003"+
		"\u001a\r\u0000\u0091\u0093\u0005\r\u0000\u0000\u0092\u0094\u0005\u0010"+
		"\u0000\u0000\u0093\u0092\u0001\u0000\u0000\u0000\u0093\u0094\u0001\u0000"+
		"\u0000\u0000\u0094\u00af\u0001\u0000\u0000\u0000\u0095\u0096\u0005\u0011"+
		"\u0000\u0000\u0096\u0097\u0005\u0004\u0000\u0000\u0097\u0098\u0005\u0001"+
		"\u0000\u0000\u0098\u0099\u0003\u001e\u000f\u0000\u0099\u009a\u0005\u0001"+
		"\u0000\u0000\u009a\u009b\u0003\u0006\u0003\u0000\u009b\u009c\u0005\u0005"+
		"\u0000\u0000\u009c\u009d\u0005\u000b\u0000\u0000\u009d\u009e\u0003\u001a"+
		"\r\u0000\u009e\u00a0\u0005\r\u0000\u0000\u009f\u00a1\u0005\u0010\u0000"+
		"\u0000\u00a0\u009f\u0001\u0000\u0000\u0000\u00a0\u00a1\u0001\u0000\u0000"+
		"\u0000\u00a1\u00af\u0001\u0000\u0000\u0000\u00a2\u00a3\u0005\u0011\u0000"+
		"\u0000\u00a3\u00a4\u0005\u0004\u0000\u0000\u00a4\u00a5\u0005\u0001\u0000"+
		"\u0000\u00a5\u00a6\u0003\u001e\u000f\u0000\u00a6\u00a7\u0005\u0001\u0000"+
		"\u0000\u00a7\u00a8\u0005\u0005\u0000\u0000\u00a8\u00a9\u0005\u000b\u0000"+
		"\u0000\u00a9\u00aa\u0003\u001a\r\u0000\u00aa\u00ac\u0005\r\u0000\u0000"+
		"\u00ab\u00ad\u0005\u0010\u0000\u0000\u00ac\u00ab\u0001\u0000\u0000\u0000"+
		"\u00ac\u00ad\u0001\u0000\u0000\u0000\u00ad\u00af\u0001\u0000\u0000\u0000"+
		"\u00ae\u0084\u0001\u0000\u0000\u0000\u00ae\u0095\u0001\u0000\u0000\u0000"+
		"\u00ae\u00a2\u0001\u0000\u0000\u0000\u00af\r\u0001\u0000\u0000\u0000\u00b0"+
		"\u00b1\u0005\u0012\u0000\u0000\u00b1\u00b2\u0005,\u0000\u0000\u00b2\u00b3"+
		"\u00052\u0000\u0000\u00b3\u00b5\u0005\u0004\u0000\u0000\u00b4\u00b6\u0003"+
		"\u0012\t\u0000\u00b5\u00b4\u0001\u0000\u0000\u0000\u00b5\u00b6\u0001\u0000"+
		"\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000\u0000\u00b7\u00b8\u0005\u0005"+
		"\u0000\u0000\u00b8\u00b9\u0005\u000b\u0000\u0000\u00b9\u00ba\u0003\u001a"+
		"\r\u0000\u00ba\u00bc\u0005\r\u0000\u0000\u00bb\u00bd\u0005\u0012\u0000"+
		"\u0000\u00bc\u00bb\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001\u0000\u0000"+
		"\u0000\u00bd\u010b\u0001\u0000\u0000\u0000\u00be\u00bf\u0005\u0013\u0000"+
		"\u0000\u00bf\u00c0\u0005,\u0000\u0000\u00c0\u00c1\u00052\u0000\u0000\u00c1"+
		"\u00c3\u0005\u0004\u0000\u0000\u00c2\u00c4\u0003\u0012\t\u0000\u00c3\u00c2"+
		"\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000\u0000\u0000\u00c4\u00c5"+
		"\u0001\u0000\u0000\u0000\u00c5\u00c6\u0005\u0005\u0000\u0000\u00c6\u00c7"+
		"\u0005\u000b\u0000\u0000\u00c7\u00c8\u0003\u001a\r\u0000\u00c8\u00ca\u0005"+
		"\r\u0000\u0000\u00c9\u00cb\u0005\u0013\u0000\u0000\u00ca\u00c9\u0001\u0000"+
		"\u0000\u0000\u00ca\u00cb\u0001\u0000\u0000\u0000\u00cb\u010b\u0001\u0000"+
		"\u0000\u0000\u00cc\u00cd\u0005\u0014\u0000\u0000\u00cd\u00ce\u0005,\u0000"+
		"\u0000\u00ce\u00cf\u00052\u0000\u0000\u00cf\u00d1\u0005\u0004\u0000\u0000"+
		"\u00d0\u00d2\u0003\u0012\t\u0000\u00d1\u00d0\u0001\u0000\u0000\u0000\u00d1"+
		"\u00d2\u0001\u0000\u0000\u0000\u00d2\u00d3\u0001\u0000\u0000\u0000\u00d3"+
		"\u00d4\u0005\u0005\u0000\u0000\u00d4\u00d5\u0005\u000b\u0000\u0000\u00d5"+
		"\u00d6\u0003\u001a\r\u0000\u00d6\u00d8\u0005\r\u0000\u0000\u00d7\u00d9"+
		"\u0005\u0014\u0000\u0000\u00d8\u00d7\u0001\u0000\u0000\u0000\u00d8\u00d9"+
		"\u0001\u0000\u0000\u0000\u00d9\u010b\u0001\u0000\u0000\u0000\u00da\u00db"+
		"\u0005\u0012\u0000\u0000\u00db\u00dc\u00052\u0000\u0000\u00dc\u00de\u0005"+
		"\u0004\u0000\u0000\u00dd\u00df\u0003\u0012\t\u0000\u00de\u00dd\u0001\u0000"+
		"\u0000\u0000\u00de\u00df\u0001\u0000\u0000\u0000\u00df\u00e0\u0001\u0000"+
		"\u0000\u0000\u00e0\u00e1\u0005\u0005\u0000\u0000\u00e1\u00e2\u0005\u0015"+
		"\u0000\u0000\u00e2\u00e3\u0005,\u0000\u0000\u00e3\u00e4\u0005\u000b\u0000"+
		"\u0000\u00e4\u00e5\u0003\u001a\r\u0000\u00e5\u00e7\u0005\r\u0000\u0000"+
		"\u00e6\u00e8\u0005\u0012\u0000\u0000\u00e7\u00e6\u0001\u0000\u0000\u0000"+
		"\u00e7\u00e8\u0001\u0000\u0000\u0000\u00e8\u010b\u0001\u0000\u0000\u0000"+
		"\u00e9\u00ea\u0005\u0013\u0000\u0000\u00ea\u00eb\u00052\u0000\u0000\u00eb"+
		"\u00ed\u0005\u0004\u0000\u0000\u00ec\u00ee\u0003\u0012\t\u0000\u00ed\u00ec"+
		"\u0001\u0000\u0000\u0000\u00ed\u00ee\u0001\u0000\u0000\u0000\u00ee\u00ef"+
		"\u0001\u0000\u0000\u0000\u00ef\u00f0\u0005\u0005\u0000\u0000\u00f0\u00f1"+
		"\u0005\u0015\u0000\u0000\u00f1\u00f2\u0005,\u0000\u0000\u00f2\u00f3\u0005"+
		"\u000b\u0000\u0000\u00f3\u00f4\u0003\u001a\r\u0000\u00f4\u00f5\u0005\u0001"+
		"\u0000\u0000\u00f5\u010b\u0001\u0000\u0000\u0000\u00f6\u00f8\u0005\r\u0000"+
		"\u0000\u00f7\u00f9\u0005\u0013\u0000\u0000\u00f8\u00f7\u0001\u0000\u0000"+
		"\u0000\u00f8\u00f9\u0001\u0000\u0000\u0000\u00f9\u010b\u0001\u0000\u0000"+
		"\u0000\u00fa\u00fb\u0005\u0014\u0000\u0000\u00fb\u00fc\u00052\u0000\u0000"+
		"\u00fc\u00fe\u0005\u0004\u0000\u0000\u00fd\u00ff\u0003\u0012\t\u0000\u00fe"+
		"\u00fd\u0001\u0000\u0000\u0000\u00fe\u00ff\u0001\u0000\u0000\u0000\u00ff"+
		"\u0100\u0001\u0000\u0000\u0000\u0100\u0101\u0005\u0005\u0000\u0000\u0101"+
		"\u0102\u0005\u0015\u0000\u0000\u0102\u0103\u0005,\u0000\u0000\u0103\u0104"+
		"\u0005\u000b\u0000\u0000\u0104\u0105\u0003\u001a\r\u0000\u0105\u0106\u0005"+
		"\u0001\u0000\u0000\u0106\u0108\u0005\r\u0000\u0000\u0107\u0109\u0005\u0014"+
		"\u0000\u0000\u0108\u0107\u0001\u0000\u0000\u0000\u0108\u0109\u0001\u0000"+
		"\u0000\u0000\u0109\u010b\u0001\u0000\u0000\u0000\u010a\u00b0\u0001\u0000"+
		"\u0000\u0000\u010a\u00be\u0001\u0000\u0000\u0000\u010a\u00cc\u0001\u0000"+
		"\u0000\u0000\u010a\u00da\u0001\u0000\u0000\u0000\u010a\u00e9\u0001\u0000"+
		"\u0000\u0000\u010a\u00f6\u0001\u0000\u0000\u0000\u010a\u00fa\u0001\u0000"+
		"\u0000\u0000\u010b\u000f\u0001\u0000\u0000\u0000\u010c\u010d\u0005\u0016"+
		"\u0000\u0000\u010d\u010e\u0003\u001e\u000f\u0000\u010e\u0011\u0001\u0000"+
		"\u0000\u0000\u010f\u0114\u0003\u0014\n\u0000\u0110\u0111\u0005\u0017\u0000"+
		"\u0000\u0111\u0113\u0003\u0014\n\u0000\u0112\u0110\u0001\u0000\u0000\u0000"+
		"\u0113\u0116\u0001\u0000\u0000\u0000\u0114\u0112\u0001\u0000\u0000\u0000"+
		"\u0114\u0115\u0001\u0000\u0000\u0000\u0115\u0013\u0001\u0000\u0000\u0000"+
		"\u0116\u0114\u0001\u0000\u0000\u0000\u0117\u0118\u0005,\u0000\u0000\u0118"+
		"\u0119\u00052\u0000\u0000\u0119\u0015\u0001\u0000\u0000\u0000\u011a\u011b"+
		"\u00052\u0000\u0000\u011b\u011d\u0005\u0004\u0000\u0000\u011c\u011e\u0003"+
		"\u0018\f\u0000\u011d\u011c\u0001\u0000\u0000\u0000\u011d\u011e\u0001\u0000"+
		"\u0000\u0000\u011e\u011f\u0001\u0000\u0000\u0000\u011f\u0120\u0005\u0005"+
		"\u0000\u0000\u0120\u0017\u0001\u0000\u0000\u0000\u0121\u0126\u0003\u001e"+
		"\u000f\u0000\u0122\u0123\u0005\u0017\u0000\u0000\u0123\u0125\u0003\u001e"+
		"\u000f\u0000\u0124\u0122\u0001\u0000\u0000\u0000\u0125\u0128\u0001\u0000"+
		"\u0000\u0000\u0126\u0124\u0001\u0000\u0000\u0000\u0126\u0127\u0001\u0000"+
		"\u0000\u0000\u0127\u0019\u0001\u0000\u0000\u0000\u0128\u0126\u0001\u0000"+
		"\u0000\u0000\u0129\u012a\u0003\u0002\u0001\u0000\u012a\u012b\u0005\u0001"+
		"\u0000\u0000\u012b\u012d\u0001\u0000\u0000\u0000\u012c\u0129\u0001\u0000"+
		"\u0000\u0000\u012d\u0130\u0001\u0000\u0000\u0000\u012e\u012c\u0001\u0000"+
		"\u0000\u0000\u012e\u012f\u0001\u0000\u0000\u0000\u012f\u001b\u0001\u0000"+
		"\u0000\u0000\u0130\u012e\u0001\u0000\u0000\u0000\u0131\u0132\u0005,\u0000"+
		"\u0000\u0132\u0135\u00052\u0000\u0000\u0133\u0134\u0007\u0001\u0000\u0000"+
		"\u0134\u0136\u0003\u001e\u000f\u0000\u0135\u0133\u0001\u0000\u0000\u0000"+
		"\u0135\u0136\u0001\u0000\u0000\u0000\u0136\u001d\u0001\u0000\u0000\u0000"+
		"\u0137\u0138\u0006\u000f\uffff\uffff\u0000\u0138\u0139\u0007\u0002\u0000"+
		"\u0000\u0139\u013b\u0005\u0004\u0000\u0000\u013a\u013c\u0005\u001b\u0000"+
		"\u0000\u013b\u013a\u0001\u0000\u0000\u0000\u013b\u013c\u0001\u0000\u0000"+
		"\u0000\u013c\u013d\u0001\u0000\u0000\u0000\u013d\u014b\u0005\u0005\u0000"+
		"\u0000\u013e\u014b\u0003\u0016\u000b\u0000\u013f\u0140\u0005+\u0000\u0000"+
		"\u0140\u014b\u0003\u001e\u000f\u0007\u0141\u0142\u0005\u0004\u0000\u0000"+
		"\u0142\u0143\u0003\u001e\u000f\u0000\u0143\u0144\u0005\u0005\u0000\u0000"+
		"\u0144\u014b\u0001\u0000\u0000\u0000\u0145\u014b\u0005\u001b\u0000\u0000"+
		"\u0146\u014b\u0005\u001c\u0000\u0000\u0147\u014b\u0005\u001d\u0000\u0000"+
		"\u0148\u014b\u0005\u001e\u0000\u0000\u0149\u014b\u00052\u0000\u0000\u014a"+
		"\u0137\u0001\u0000\u0000\u0000\u014a\u013e\u0001\u0000\u0000\u0000\u014a"+
		"\u013f\u0001\u0000\u0000\u0000\u014a\u0141\u0001\u0000\u0000\u0000\u014a"+
		"\u0145\u0001\u0000\u0000\u0000\u014a\u0146\u0001\u0000\u0000\u0000\u014a"+
		"\u0147\u0001\u0000\u0000\u0000\u014a\u0148\u0001\u0000\u0000\u0000\u014a"+
		"\u0149\u0001\u0000\u0000\u0000\u014b\u0160\u0001\u0000\u0000\u0000\u014c"+
		"\u014d\n\r\u0000\u0000\u014d\u014e\u0007\u0003\u0000\u0000\u014e\u015f"+
		"\u0003\u001e\u000f\u000e\u014f\u0150\n\f\u0000\u0000\u0150\u0151\u0007"+
		"\u0004\u0000\u0000\u0151\u015f\u0003\u001e\u000f\r\u0152\u0153\n\u000b"+
		"\u0000\u0000\u0153\u0154\u0007\u0005\u0000\u0000\u0154\u015f\u0003\u001e"+
		"\u000f\f\u0155\u0156\n\n\u0000\u0000\u0156\u0157\u0005$\u0000\u0000\u0157"+
		"\u015f\u0003\u001e\u000f\u000b\u0158\u0159\n\t\u0000\u0000\u0159\u015a"+
		"\u0005)\u0000\u0000\u015a\u015f\u0003\u001e\u000f\n\u015b\u015c\n\b\u0000"+
		"\u0000\u015c\u015d\u0005*\u0000\u0000\u015d\u015f\u0003\u001e\u000f\t"+
		"\u015e\u014c\u0001\u0000\u0000\u0000\u015e\u014f\u0001\u0000\u0000\u0000"+
		"\u015e\u0152\u0001\u0000\u0000\u0000\u015e\u0155\u0001\u0000\u0000\u0000"+
		"\u015e\u0158\u0001\u0000\u0000\u0000\u015e\u015b\u0001\u0000\u0000\u0000"+
		"\u015f\u0162\u0001\u0000\u0000\u0000\u0160\u015e\u0001\u0000\u0000\u0000"+
		"\u0160\u0161\u0001\u0000\u0000\u0000\u0161\u001f\u0001\u0000\u0000\u0000"+
		"\u0162\u0160\u0001\u0000\u0000\u0000\'\"(5IMVZeirvx\u0082\u0093\u00a0"+
		"\u00ac\u00ae\u00b5\u00bc\u00c3\u00ca\u00d1\u00d8\u00de\u00e7\u00ed\u00f8"+
		"\u00fe\u0108\u010a\u0114\u011d\u0126\u012e\u0135\u013b\u014a\u015e\u0160";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}