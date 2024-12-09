from generator import generator
from parser import parser
from scanner import scan

input = 'castSpell howmanyvillains(): numberofprinces = 10 if (numberofprinces > 5): numberofvillains = 0 happilyEverAfter numberofvillains'
scanner_output = scan(input)
parser(scanner_output)
generator_output = generator(scanner_output)

final_pipeline_code = generator_output + "\nprint(howmanyvillains())"
print(final_pipeline_code)

# Expected scanner output
'''
output = ['<KEYWORD, castSpell>', 
'<IDENTIFIER, howmanyvillains>', 
'<PUNCTUATION, (>', '<PUNCTUATION, )>', 
'<PUNCTUATION, :>', 
'<IDENTIFIER, numberofprinces>', 
'<ASSIGNMENT_OPERATOR, =>', 
'<INT, 10>', 
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
  ├──     ASSIGNMENT
    ├──       IDENTIFIER (numberofprinces)
    ├──       =
    └──       INT (10)
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
    numberofprinces = 10
    if numberofprinces>5:
        numberofvillains = 0
        return numberofvillains'''