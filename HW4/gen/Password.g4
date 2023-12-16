grammar Password;

password: CHAR+;

CHAR: (UPPER | LOWER | DIGIT | SYMBOL | EOF);

UPPER: [A-Z];
LOWER: [a-z];
DIGIT: [0-9];
SYMBOL: 
    '!' | '@' | '#' | '$' | '%' | '^' | '&' 
    | '*' | '(' | ')' | '_' | '+' | '{' | '}' 
    | '|' | ':' | '"' | '<' | '>' | '?' | '`' 
    | '-' | '=' | '[' | ']' | '\\' | ';' | '\'' 
    | ',' | '.' | '/';

WS: [ \t\r\n]+ -> skip;
