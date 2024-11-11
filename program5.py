
from parser import parser, token
from scanner import scan

#scanner input
input = 'castSpell howmanyvillains(): if (numberofprinces > 5): numberofvillains = 0 happilyEverAfter villain'
scanner_output = scan(input)
parser(scanner_output)

# Expected scanner output
'''
output = ['<KEYWORD, castSpell>', 
          '<IDENTIFIER, howmanyvillains>', 
          '<PUNCTUATION, (>', 
          '<PUNCTUATION, )>', 
          '<PUNCTUATION, :>', 
          '<KEYWORD, if>', 
          '<PUNCTUATION, (>', 
          '<IDENTIFIER, numberofprinces>', 
          '<OPERATOR, >>', 
          '<INT, 5>', 
          '<PUNCTUATION, )>', 
          '<PUNCTUATION, :>', 
          '<IDENTIFIER, numberofvillains>', 
          '<ASSIGNMENT_OPERATOR, =>', 
          '<INT, 0>', 
          '<KEYWORD, happilyEverAfter>', 
          '<IDENTIFIER, villain>']
'''
# Expected parser output: 
'''
FUNCTION (castSpell)
 ├──   IDENTIFIER (howmanyvillains)
 └──   STATEMENT_BLOCK
   └──     FUNCTION (if)
     ├──       EXPRESSION
       ├──         IDENTIFIER (numberofprinces)
       ├──         >
       └──         INT (5)
     └──       STATEMENT_BLOCK
       ├──         ASSIGNMENT
         ├──           IDENTIFIER (numberofvillains)
         ├──           =
         └──           INT (0)
       └──         FUNCTION (happilyEverAfter)
         └──           IDENTIFIER (villain)
'''