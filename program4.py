
from parser import parser, token
#scanner input

# castSpell error(): 
# 	a +


#scanner output

output = ['<KEYWORD, castSpell>', 
 '<IDENTIFIER, error>', 
 '<PUNCTUATION, (>', 
 '<PUNCTUATION, )>', 
 '<PUNCTUATION, :>', 
 '<IDENTIFIER, a>', 
 '<OPERATOR, +>']


parser(output)
# Expected Output: 
# Parse Error: Invalid expression syntax: Expected an int, id, or bool