grammar Pseudo;

program: ((functionDef | statement) ';')* EOF;

statement
    : printStatement
    | assignmentStatement
    | ifStatement
    | whileStatement
    | forStatement
    | functionCallStatement
    | returnStatement
    | varDeclStatement
    ;

printStatement: ('print' | 'shout') '(' expr ')';

assignmentStatement: ID op = ('=' | 'is' | '<<' | '<-') expr;

ifStatement:
	'if' '(' expr ')' ':' body ('else' ':' body)? 'end' ('if')?
	| 'if' expr ':' body ('else' ':' body)? 'end' ('if')?
	| 'if' '(' expr ')' 'then' body ('else' ':' body)? 'end' (
		'if'
	)?
	| 'if' expr 'then' body ('else' ':' body)? 'end' ('if')?;

whileStatement: 'while' '(' expr ')' ':' body 'end' ('loop')?;

forStatement:
	'for' '(' TYPE ID OP = ('=' | 'is' | '<<' | '<-') NUMBER ';' expr ';' assignmentStatement ')'
		':' body 'end' ('loop')?
	| 'for' '(' ';' expr ';' assignmentStatement ')' ':' body 'end' (
		'loop'
	)?
	| 'for' '(' ';' expr ';' ')' ':' body 'end' ('loop')?;

functionDef
    : 'function' type=TYPE name=ID '(' params=paramList? ')' ':' block=body 'end' ('function')?
    | 'fun' type=TYPE name=ID '(' params=paramList? ')' ':' block=body 'end' ('fun')?
    | 'def' type=TYPE name=ID '(' params=paramList? ')' ':' block=body 'end' ('def')?

    | 'function' name=ID '(' params=paramList? ')' '->' type=TYPE ':' block=body 'end' ('function')?
    | 'fun' name=ID '(' params=paramList? ')' '->' type=TYPE ':' block=body ';' |'end' ('fun')?
    | 'def' name=ID '(' params=paramList? ')' '->' type=TYPE ':' block=body ';' 'end' ('def')?
    ;

returnStatement
    : 'return' val=expr
    ;

paramList
    : param (',' param)*
    ;

param
    : type=TYPE name=ID
    ;

functionCallStatement
    : name=ID '(' args=argumentList? ')'
    ;

argumentList: expr (',' expr)*;

body
    : (statement ';')*
    ;

varDeclStatement: TYPE ID (op=('=' | 'is' | '<<' | '<-') expr)?;

expr
    : ('input'|'scan'|'listen') '(' (STRING)? ')'
    | functionCallStatement
    | expr op=(MULT | DIV) expr
    | expr op=(PLUS | MINUS) expr
    | expr op=(GREATER | SMALLER | EQUAL | DIFFERENT) expr
    | expr op=INTDIV expr
    | expr AND expr
    | expr OR expr
    | op=NOT expr
    | '(' expr ')'
    | STRING
    | NUMBER
    | DOUBLE
    | BOOL
    | ID
    ;

STRING: '"' (ESC | ~["\\])* '"' | '\'' (ESC | ~['\\])* '\'';
fragment ESC: '\\' ["'\\rbnt];

NUMBER: [0-9]+;
DOUBLE: [0-9]+ '.' [0-9]+;
BOOL: 'true' | 'false';

WS: [ \t\n\r]+ -> skip;

PLUS      : '+';
MINUS     : '-';
MULT      : '*';
DIV       : '/';
INTDIV    : '//';
GREATER   : '>'| 'greater than';
SMALLER   : '<'| 'smaller than';
EQUAL     : '=='|'equals';
DIFFERENT : '!='| 'differs';
AND       : '&&'|'and';
OR        : '||'|'or';
NOT       : '!'|'not';

TYPE
    : TYPE_INT
    | TYPE_FLOAT
    | TYPE_STRING
    | TYPE_BOOL
    | TYPE_VOID
    ;

TYPE_INT: 'int';
TYPE_FLOAT: 'float';
TYPE_STRING: 'string';
TYPE_BOOL: 'boolean';
TYPE_VOID: 'void';

ID: [a-zA-Z_][a-zA-Z0-9_]*;