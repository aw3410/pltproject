
from parser import parser, token

#scanner output
output = [
   token('KEYWORD', 'castSpell'),       
   token('IDENTIFIER', 'helloWorld'),       
   token('PUNCTUATION', ':'),                      
   token('KEYWORD', 'paint'),
   token('PUNCTUATION', '('),
   token('STRING', 'Hello Kingdom'),
   token('PUNCTUATION', ')') ]

parser(output)
#expected output: 
#Parse Error: Function declaration must have parentheses after the identifier.