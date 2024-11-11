from parser import parser, token
from scanner import scan


input = 'castSpell repeat(): clock = 12 untilClockStrikes (12): clock = clock - 1 paint(clock)'
scanner_output = scan(input)
parser(scanner_output) #pass scanner output to parser

#Expected scanner output:

'''output = ['<KEYWORD, castSpell>', 
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
          '<PUNCTUATION, )>'] '''


#Expected parser output 
''' FUNCTION (castSpell)
 ├──   IDENTIFIER (repeat)
 └──   STATEMENT_BLOCK
   ├──     ASSIGNMENT
     ├──       IDENTIFIER (clock)
     ├──       =
     └──       INT (12)
   └──     FUNCTION (untilClockStrikes)
     ├──       INT (12)
     └──       STATEMENT_BLOCK
       ├──         ASSIGNMENT
         ├──           IDENTIFIER (clock)
         ├──           =
         └──           EXPRESSION
           ├──             IDENTIFIER (clock)
           ├──             -
           └──             INT (1)
       └──         FUNCTION (paint)
         └──           IDENTIFIER (clock) '''

