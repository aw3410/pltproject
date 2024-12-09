from scanner import scan
from parser import parser
from generator import generator


#scanner input
input = "castSpell nomidnight(): clock = 13 if (clock > 12): happilyEverAfter clock paint('bye bye cinderella')"
scanner_output = scan(input)
ast = parser(scanner_output)
generator_output = generator(ast)
final_pipeline_code = generator_output + "\nprint(nomidnight())"
print(final_pipeline_code)


#Expected scanner output
'''output = ['<KEYWORD, castSpell>', 
'<IDENTIFIER, nomidnight>', 
'<PUNCTUATION, (>', 
'<PUNCTUATION, )>', 
'<PUNCTUATION, :>', 
'<IDENTIFIER, clock>', 
'<ASSIGNMENT_OPERATOR, =>', 
'<INT, 13>', 
'<KEYWORD, if>', 
'<PUNCTUATION, (>', 
'<IDENTIFIER, clock>', 
'<OPERATOR, >>', 
'<INT, 12>', 
'<PUNCTUATION, )>', 
'<PUNCTUATION, :>', 
'<KEYWORD, happilyEverAfter>', 
'<IDENTIFIER, clock>', 
'<KEYWORD, paint>', 
'<PUNCTUATION, (>', 
"<STRING, 'bye bye cinderella'>", 
'<PUNCTUATION, )>']
'''

# Expected parser output: 
'''
FUNCTION (castSpell)
├──   IDENTIFIER (nomidnight)
└──   STATEMENT_BLOCK
  ├──     ASSIGNMENT
    ├──       IDENTIFIER (clock)
    ├──       =
    └──       INT (13)
  └──     FUNCTION (if)
    ├──       EXPRESSION
      ├──         IDENTIFIER (clock)
      ├──         >
      └──         INT (12)
    └──       STATEMENT_BLOCK
      ├──         FUNCTION (happilyEverAfter)
        └──           IDENTIFIER (clock)
      └──         FUNCTION (paint)
        └──           STRING ('bye bye cinderella')
'''
# Expected codegen output
'''#unreachable code detected at stage FUNCTION and value paint

def nomidnight():
    clock = 13
    if clock>12:
        return clock'''

#Expected program output
'''13'''