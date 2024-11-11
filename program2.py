from parser import parser, token

#INPUT 2
tokens = [
    token('KEYWORD', 'castSpell'),        
    token('IDENTIFIER', 'repeat'),        
    token('PUNCTUATION', '('),             
    token('PUNCTUATION', ')'),            
    token('PUNCTUATION', ':'),            
    token('IDENTIFIER', 'clock'),          
    token('ASSIGNMENT_OPERATOR', '='),             
    token('INT', '12'),             
    token('KEYWORD', 'untilClockStrikes'), 
    token('PUNCTUATION', '('),             
    token('INT', '12'),  
    token('PUNCTUATION', ')'),            
    token('PUNCTUATION', ':'),             
    token('IDENTIFIER', 'clock2'),          
    token('ASSIGNMENT_OPERATOR', '='),             
    token('IDENTIFIER', 'clock3'),          
    token('OPERATOR', '-'),                
    token('INT', '1'),            
    token('KEYWORD', 'paint'),
    token('PUNCTUATION', '('),
    token('IDENTIFIER', 'clock4'),
    token('PUNCTUATION', ')')
]
parser(tokens)

#expected output 
# FUNCTION (castSpell)
# ├──   IDENTIFIER (repeat)
# └──   STATEMENT_BLOCK
#   ├──     ASSIGNMENT
#     ├──       IDENTIFIER (clock)
#     ├──       =
#     └──       INT (12)
#   └──     FUNCTION (untilClockStrikes)
#     ├──       INT (12)
#     └──       STATEMENT_BLOCK
#       ├──         ASSIGNMENT
#         ├──           IDENTIFIER (clock2)
#         ├──           =
#         └──           EXPRESSION
#           ├──             IDENTIFIER (clock3)
#           ├──             -
#           └──             INT (1)
#       └──         FUNCTION (paint)
#         └──           IDENTIFIER (clock4)

