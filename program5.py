from generator import generator
from parser import parser
from scanner import scan

#scanner input
input = 'castSpell howmanyvillains(): if (numberofprinces > 5): numberofvillains = 0 happilyEverAfter numberofvillains'
scanner_output = scan(input)
parser_output = parser(scanner_output)
generator(scanner_output)


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
          '<IDENTIFIER, numberofvillains>']
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
         └──           IDENTIFIER (numberofvillains)
'''

# Expected codegen output: 
'''def howmanyvillains():
    if numberofprinces>5:
        numberofvillains = 0
        return(numberofvillains)'''