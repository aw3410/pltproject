from scanner import scan
from parser import parser, token


#scanner input
input = "castSpell helloWorld: paint('Hello kingdom')"
scanner_output = scan(input)
parser(scanner_output)

#Expected scanner output

'''output = ['<KEYWORD, castSpell>', 
 '<IDENTIFIER, helloWorld>', 
 '<PUNCTUATION, :>', 
 '<KEYWORD, paint>', 
 '<PUNCTUATION, (>', 
 "<STRING, 'Hello kingdom'>", 
 '<PUNCTUATION, )>']'''


#Expected parser output: 
#Parse Error: Function declaration must have parentheses after the identifier.