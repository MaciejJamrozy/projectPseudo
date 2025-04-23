grammar Pseudo;

program: (statement ';')* EOF;

statement
    : printStatement
    | varDeclStatement
    | assignmentStatement
    | ifStatement
    | whileStatement
    | forStatement
    | functionDefStatement
    | functionCallStatement
    ;

printStatement: ('print' | 'shout') '(' STRING ')';

varDeclStatement: TYPE ID (op=('=' | 'is' | '<<' | '<-') expr)?;

assignmentStatement: ID op=('=' | 'is' | '<<' | '<-') expr;

ifStatement
    : 'if' '(' expr ')' ':' body ('else' ':' body)? 'end' ('if')?
    | 'if' expr ':' body ('else' ':' body)? 'end' ('if')?
    | 'if' '(' expr ')' 'then' body ('else' ':' body)? 'end' ('if')?
    | 'if' expr 'then' body ('else' ':' body)? 'end' ('if')?
    ;

whileStatement: 'while' '(' expr ')' ':' body 'end' ('loop')?;

forStatement
    : 'for' '(' TYPE_INT ID OP=('=' | 'is' | '<<' | '<-') NUMBER ';' expr ';' assignmentStatement ')' ':' body 'end' ('loop')?
    ;

functionDefStatement
    : 'function' ID '(' paramList? ')' ':' body 'end' ('function')?
    ;

paramList
    : ID (',' ID)*
    ;

functionCallStatement
    : ID '(' argumentList? ')'
    ;

argumentList
    : expr (',' expr)*
    ;

body
    : (statement ';')* 
    ;

expr
    : ('input'|'scan'|'listen') '(' (STRING)? ')'
    | expr op=(MULT | DIV) expr
    | expr op=(PLUS | MINUS) expr
    | expr op=(GREATER | SMALLER | EQUAL | DIFFERENT) expr
    | '!' expr
    | expr '&&' expr
    | expr '||' expr
    | 'not' expr
    | expr 'and' expr
    | expr 'or' expr 
    | '(' expr ')' 
    | STRING
    | NUMBER
    | DOUBLE
    | BOOL
    | ID
    ;

STRING
    : '"' (ESC | ~["\\])* '"'
    | '\'' (ESC | ~['\\])* '\''
    ;
NUMBER: [0-9]+;
DOUBLE: [0-9]+ '.' [0-9]+;
BOOL
    : 'true'
    | 'false'
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
ESC: '\\' ["'\\rnt];

PLUS      : '+';
MINUS     : '-';
MULT      : '*';
DIV       : '/';
EQ        : '=';
GREATER   : '>';
SMALLER   : '<';
EQUAL     : '==';
DIFFERENT : '!=';

TYPE
    : TYPE_INT
    | TYPE_FLOAT
    | TYPE_STRING
    | TYPE_BOOL
    ;

TYPE_INT: 'int';
TYPE_FLOAT: 'float';
TYPE_STRING: 'string';
TYPE_BOOL: 'boolean';