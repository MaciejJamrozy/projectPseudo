grammar Pseudo;

program: ((functionDef | statement) ';')* EOF;

statement:
	printStatement
	| assignmentStatement
	| ifStatement
	| whileStatement
	| forStatement
	| functionCallStatement
	| returnStatement
	| breakStatement
	| continueStatement
	| varDeclStatement;

printStatement: ('print' | 'shout') '(' expr ')';

assignmentStatement
	: (global = 'global')? ID op = ('=' | 'is' | '<<' | '<-') expr
	| (global = 'global')? ID op = ('++' | '--')
	;

ifStatement:
	'if' ('(' expr ')' | expr) (':' | 'then') body (
		'elseif' ('(' expr ')' | expr) (':' | 'then') body
	)* ('else' ':' body)? 'end' ('if')?;

whileStatement: 'while' '(' expr ')' ':' body 'end' ('loop')?;

forStatement:
	'for' '(' (entryStmt=initStatement)? ';' expr? ';' assignmentStatement? ')' ':' body 'end' ('loop')?;

initStatement
	: varDeclStatement
	| assignmentStatement
	;

breakStatement: 'break' ('loop')? | 'exit' ('loop')?;

continueStatement: 'continue' ('loop')? | 'next' ('loop')?;

functionDef:
	'function' type = TYPE name = ID '(' params = paramList? ')' ':' block = body 'end' (
		'function'
	)?
	| 'fun' type = TYPE name = ID '(' params = paramList? ')' ':' block = body 'end' (
		'fun'
	)?
	| 'def' type = TYPE name = ID '(' params = paramList? ')' ':' block = body 'end' (
		'def'
	)?
	| 'function' name = ID '(' params = paramList? ')' '->' type = TYPE ':' block = body 'end' (
		'function'
	)?
	| 'fun' name = ID '(' params = paramList? ')' '->' type = TYPE ':' block = body ';'
	| 'end' ('fun')?
	| 'def' name = ID '(' params = paramList? ')' '->' type = TYPE ':' block = body ';' 'end' (
		'def'
	)?;

returnStatement: 'return' val = expr;

paramList: param (',' param)*;

param: type = TYPE name = ID;

functionCallStatement: name = ID '(' args = argumentList? ')';

argumentList: expr (',' expr)*;

body: ((functionDef | statement) ';')*;

varDeclStatement:
	(global = 'global')? TYPE ID (op = ('=' | 'is' | '<<' | '<-') expr)?;

expr: ('input' | 'scan' | 'listen') '(' (STRING)? ')'
	| functionCallStatement
	| expr op = (MULT | DIV) expr
	| expr op = (PLUS | MINUS) expr
	| expr op = (
		GREATER
		| SMALLER
		| EQUAL
		| DIFFERENT
		| GREATEREQUAL
		| SMALLEREQUAL
	) expr
	| expr op = (
		GREATER
		| SMALLER
		| EQUAL
		| DIFFERENT
		| GREATEREQUAL
		| SMALLEREQUAL
	) expr
	| expr op = INTDIV expr
	| op = MINUS expr
	| expr op = AND expr
	| expr op = OR expr
	| op = NOT expr
	| op = PARENT expr
	| '(' op = TYPE ')' expr
	| '(' expr ')'
	| STRING
	| NUMBER
	| DOUBLE
	| BOOL
	| ID;

STRING: '"' (ESC | ~["\\])* '"' | '\'' (ESC | ~['\\])* '\'';
fragment ESC: '\\' ["'\\rbnt];

NUMBER: [0-9]+;
DOUBLE: [0-9]+ '.' [0-9]+;
BOOL: 'True' | 'False';

WS: [ \t\n\r]+ -> skip;

SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT: '/*' .*? '*/' -> skip;

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
INTDIV: '/#';
INCREMENT: '++';
DECREMENT: '--';
GREATER: '>' | 'greater than';
SMALLER: '<' | 'smaller than';
GREATEREQUAL: '>=' | 'greater or equal than';
SMALLEREQUAL: '<=' | 'smaller or equal than';
EQUAL: '==' | 'equals';
DIFFERENT: '!=' | 'differs';
AND: '&&' | 'and';
OR: '||' | 'or';
NOT: '!' | 'not';
PARENT: 'parent::';

TYPE:
	TYPE_INT
	| TYPE_FLOAT
	| TYPE_STRING
	| TYPE_BOOL
	| TYPE_VOID;

TYPE_INT: 'int';
TYPE_FLOAT: 'float';
TYPE_STRING: 'string';
TYPE_BOOL: 'boolean';
TYPE_VOID: 'void';

ID: [a-zA-Z_][a-zA-Z0-9_]*;