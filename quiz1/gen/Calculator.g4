grammar Calculator;

NUMBER : DIGIT+ ('.' DIGIT+)?;
DIGIT : [0-9];

expr : term (('+'|'-') term)*;
term : factor (('*'|'/') factor)*;
factor : power;
power : atom ('^' atom)?;
atom : NUMBER | '(' expr ')';

WS : [ \t\r\n]+ -> skip;
