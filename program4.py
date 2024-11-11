
from parser import parser, token

tokens = [
    token('KEYWORD', 'castSpell'),        
    token('IDENTIFIER', 'error'),          
    token('PUNCTUATION', '('),             
    token('PUNCTUATION', ')'),             
    token('PUNCTUATION', ':'),             
    token('IDENTIFIER', 'a'),              
    token('OPERATOR', '+') 
]
parser(tokens)
# Expected Output: 
# Parse Error: Invalid expression syntax: Expected an int, id, or bool