from parser import parser, token

#castSpell repeat():
# clock = 12
# untilClockStrikes (12):
# 	clock = clock - 1
# 	paint(clock)

#INPUT 2 
#scanner output

output = [
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
parser(output)

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

