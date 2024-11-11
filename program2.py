from parser import parser, token

# scanner input

#castSpell repeat():
#   clock = 12
#   untilClockStrikes (12):
# 	    clock = clock - 1
# 	    paint(clock)

#INPUT 2 
#scanner output

output = ['<KEYWORD, castSpell>', 
          '<IDENTIFIER, repeat>', 
          '<PUNCTUATION, (>', 
          '<PUNCTUATION, )>', 
          '<PUNCTUATION, :>', 
          '<IDENTIFIER, clock>', 
          '<ASSIGNMENT_OPERATOR, =>', 
          '<INT, 12>', 
          '<KEYWORD, untilClockStrikes>', 
          '<PUNCTUATION, (>',
          '<INT, 12>', 
          '<PUNCTUATION, )>', 
          '<PUNCTUATION, :>', 
          '<IDENTIFIER, clock>', 
          '<ASSIGNMENT_OPERATOR, =>', 
          '<IDENTIFIER, clock>', 
          '<OPERATOR, ->', 
          '<INT, 1>', 
          '<KEYWORD, paint>', 
          '<PUNCTUATION, (>', 
          '<IDENTIFIER, clock>', 
          '<PUNCTUATION, )>']

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
#         ├──           IDENTIFIER (clock)
#         ├──           =
#         └──           EXPRESSION
#           ├──             IDENTIFIER (clock)
#           ├──             -
#           └──             INT (1)
#       └──         FUNCTION (paint)
#         └──           IDENTIFIER (clock)

