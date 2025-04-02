grammar Pseudo++;

program: statement* EOF;

statement
    : printStatement
    | assignStatement
    ;

printStatement: ('print' | 'say' | 'write' | 'shout') '(' STRING ')';

assignStatement: ID ('=' | 'is' | '<<' | '<-') expr;

expr
    : expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | expr ('<'|'>'|'=='|'!=') expr
    | '(' expr ')' 
    | STRING
    | NUMBER
    | DOUBLE
    | ID
    ;

STRING
    : '"' (ESC | ~["\\])* '"'
    | '\'' (ESC | ~['\\])* '\''
    ;
NUMBER: [0-9]+;
DOUBLE : [0-9]+ '.' [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
ESC: '\\' ["\\rnt];

PLUS    : '+';
MINUS   : '-';
MULT    : '*';
DIV     : '/';
EQ      : '=';







