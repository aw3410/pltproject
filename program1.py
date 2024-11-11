
from parser import parser, token

#scanner output

output = [ token('KEYWORD', 'castSpell'),
    token('IDENTIFIER', 'princess'),
    token('PUNCTUATION', '('),
    token('PUNCTUATION', ')'),
    token('PUNCTUATION', ':'),
    token('KEYWORD', 'paint'),
    token('PUNCTUATION', '('),
    token('STRING', 'hello princess'),
    token('PUNCTUATION', ')') ]

parser(output)

# expected output: 
# FUNCTION (castSpell)
# ├──   IDENTIFIER (princess)
# └──   STATEMENT_BLOCK
#   └──     FUNCTION (paint)
#     └──       STRING (hello princess)