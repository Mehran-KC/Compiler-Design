// TextRecognizer.g4
grammar TextRecognizer;

COLON: ':';
COMMA: ',';

fragment LOCAL_SUBPART : [a-zA-Z0-9._%+-]+;
fragment DOMAIN_SUBPART : [a-zA-Z0-9.-]+;

EMAIL: LOCAL_SUBPART '@' DOMAIN_SUBPART '.' DOMAIN_SUBPART;
MELLI_NUMBER: DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT;
URL: (PROTOCOL 'www.' LOCAL_SUBPART '.' (DOMAIN_SUBPART | DOMAIN_SUBPART '/' DOMAIN_SUBPART+)) | (PROTOCOL LOCAL_SUBPART '.' (DOMAIN_SUBPART | DOMAIN_SUBPART '/' DOMAIN_SUBPART+)) | ('www.' LOCAL_SUBPART '.' (DOMAIN_SUBPART | DOMAIN_SUBPART '/' DOMAIN_SUBPART+)) | (LOCAL_SUBPART '.' (DOMAIN_SUBPART | DOMAIN_SUBPART '/' DOMAIN_SUBPART+));
PROTOCOL: 'http://' | 'https://';

emails: (email | melli_number | url | EOF) (COMMA (email | melli_number | url | EOF))*;
email: EMAIL;
melli_number: MELLI_NUMBER;
url: URL;

DIGIT: [0-9];
WS: [ \t\r\n ]+ -> skip;
