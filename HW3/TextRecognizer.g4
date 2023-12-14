// TextRecognizer.g4
grammar TextRecognizer;

COLON: ':';
COMMA: ',';

fragment DIGIT: [0-9];
fragment LOCAL_SUBPART : [a-zA-Z0-9._%+-]+;
fragment DOMAIN_SUBPART : [a-zA-Z0-9.-]+;

EMAIL: LOCAL_SUBPART '@' DOMAIN_SUBPART '.' DOMAIN_SUBPART;
MELLI_NUMBER: DIGIT+;

emails: (email | melli_number) (COMMA (email | melli_number))*; // Updated rule for multiple emails
email: EMAIL {print("**email found**")};
melli_number : MELLI_NUMBER;

WS: [\t\r\n]+ -> skip;
