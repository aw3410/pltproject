
from parser import parser, token
#scanner input

# castSpell error(): 
# 	a +

#scanner output
output = [
    token('KEYWORD', 'castSpell'),        
    token('IDENTIFIER', 'error'),          
    token('PUNCTUATION', '('),             
    token('PUNCTUATION', ')'),             
    token('PUNCTUATION', ':'),             
    token('IDENTIFIER', 'a'),              
    token('OPERATOR', '+') 
]
parser(output)
# Expected Output: 
# Parse Error: Invalid expression syntax: Expected an int, id, or bool