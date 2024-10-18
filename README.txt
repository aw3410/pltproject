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

Our scanner algorithm is shown in scanner.txt. It lexes the input program character by character  and transitions states accordingly. 
The scanner ensures that strings are all opened and closed with quotation marks, and that parentheses and brackets are not left open. 
If either of these are untrue an error will be returned. The scanner ensures that the program follows the grammar rules specified below and goes to an error state which returns an error message.  
Upon processing the first lexical error, it will gracefully exit the program with an error message that states the error and the position in which the error occurs. 
After reading in a token successfully, as marked by whitespace, the scanner adds the token and its type to a list which is returned after the program results in success. Here are the states, accepting states, and some of the transition rules:  

State Machine Transition Description

S = {s0, s_string, s_stringEnd, s_digit, s_err, s_operator, s_alpha, s_punctuation)
F = {sStringEnd, sDigit, s_alpha}

𝛿(s0, “) → s_string
𝛿(s_string, [.]) → s_string
𝛿(s_string, ”) → s_stringEnd 

𝛿(s0, [0-9]) → s_digit
𝛿(s_digit, [0-9]) → s_digit
𝛿(s_digit, [a-z]) → s_err
𝛿(s_digit, [operators]) → s_operator
𝛿(s_digit, “) → s_string
𝛿(s_digit, [a-z]) → s_err


𝛿(s0, [operators]) → s_err
𝛿(s_digit, [operators]) → s_operator 

𝛿(s0, ( ) → s_bracket
𝛿(s_bracket, [bracket]) → s_bracket
𝛿(s_alphabet, [punctuation] ) → s_punctuation


𝛿(s_alpha, [0-9]) → s_alpha
𝛿(s_alpha, [a-z]) → s_alpha

