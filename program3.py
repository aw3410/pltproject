
from parser import parser, token


tokens = [
   token('KEYWORD', 'castSpell'),       
   token('IDENTIFIER', 'helloWorld'),       
   token('PUNCTUATION', ':'),                      
   token('KEYWORD', 'paint'),
   token('PUNCTUATION', '('),
   token('STRING', 'Hello Kingdom'),
   token('PUNCTUATION', ')') ]

parser(tokens)
#expected output: 
#Parse Error: Function declaration must have parentheses after the identifier.