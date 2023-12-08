grammar Hello;

greet : 'Hello' ID;
ID : [a-zA-Z]+;
WS : [ \t\r\n]+ -> skip;
