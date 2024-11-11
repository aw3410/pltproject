from scanner import scan
from parser import parser, token


#scanner input
input = "castSpell error(): a +"
scanner_output = scan(input)
parser(scanner_output)

#Expected scanner output
'''output = ['<KEYWORD, castSpell>', 
 '<IDENTIFIER, error>', 
 '<PUNCTUATION, (>', 
 '<PUNCTUATION, )>', 
 '<PUNCTUATION, :>', 
 '<IDENTIFIER, a>', 
 '<OPERATOR, +>']'''


# Expected parser output: 
# Parse Error: Invalid expression syntax: Expected an int, id, or bool