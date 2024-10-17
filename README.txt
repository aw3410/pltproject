Teammates: Annika Wang (aw3410) and Kira Ariyan (kna2121)
1. Define the lexical grammar

Identifier
Variable names are letters or digits, starting with a letter
[a-z][a-z0-9]*
IDENTIFIER(value = “x”)

Intliteral
A non-empty string of digits
[0-9]+
INTLITERAL(value = “5”)

Keyword
A fixed set of reserved words 
[princess|villain|prince|crown|tiara|king|queen|rose|castSpell|paint|onceuponatime|happilyeverafter|while|if|alive|dead]
KEYWORD(value = “prince”)

Operator
Arithmetic/assignment operators 
[+ | = | -| == | != | * | / | < | > | <= | >=] 
OPERATOR(value = “+”)

Punctuation 
Commas, semicolons, braces, colons, parentheses 
[ , | . | ( | ) | { | } | ; | :]
PUNCTUATION(value = “{”)

String Literal 
String literals are contained in quotation marks 
“Aurora is sleeping”
[a-z0-9]*
STRING(value= “aurora is sleeping”)


