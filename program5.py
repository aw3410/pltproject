
from parser import parser, token

# scanner output
output = [
    token('KEYWORD', 'castSpell'),
    token('IDENTIFIER', 'howmanyvillains'),
    token('PUNCTUATION', '('),
    token('PUNCTUATION', ')'),
    token('PUNCTUATION', ':'),
    token('KEYWORD', 'if'),
    token('PUNCTUATION', '('),
    token('IDENTIFIER', 'numberofprinces'),
    token('OPERATOR', '>'),
    token('INT', '5'),
    token('PUNCTUATION', ')'),
    token('PUNCTUATION', ':'),
    token('IDENTIFIER', 'numberofvillains'),
    token('ASSIGNMENT_OPERATOR', '='),
    token('INT', '0'),
    token('KEYWORD', 'happilyEverAfter'),
    token('IDENTIFIER', 'villain')
]
parser(output)
# expected output: 
# FUNCTION (castSpell)
# ├──   IDENTIFIER (howmanyvillains)
# └──   STATEMENT_BLOCK
#   └──     FUNCTION (if)
#     ├──       EXPRESSION
#       ├──         IDENTIFIER (numberofprinces)
#       ├──         >
#       └──         INT (5)
#     └──       STATEMENT_BLOCK
#       ├──         ASSIGNMENT
#         ├──           IDENTIFIER (numberofvillains)
#         ├──           =
#         └──           INT (0)
#       └──         FUNCTION (happilyEverAfter)
#         └──           IDENTIFIER (villain)