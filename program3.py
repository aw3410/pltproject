
from parser import parser, token
#scanner input 

# castSpell helloWorld:
#     paint('Hello kingdom')

#scanner output

output = ['<KEYWORD, castSpell>', 
 '<IDENTIFIER, helloWorld>', 
 '<PUNCTUATION, :>', 
 '<KEYWORD, paint>', 
 '<PUNCTUATION, (>', 
 "<STRING, 'Hello kingdom'>", 
 '<PUNCTUATION, )>']


parser(output)
#expected output: 
#Parse Error: Function declaration must have parentheses after the identifier.