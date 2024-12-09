from scanner import scan
from parser import parser


#scanner input
input = "castSpell nomidnight(): if (clock > 12): happilyEverAfter clock paint('bye bye cinderella')"
scanner_output = scan(input)
print(scanner_output)
parser_output = parser(scanner_output)
print(parser_output)

#Expected scanner output
'''output = ['<KEYWORD, castSpell>', 
'<IDENTIFIER, nomidnight>', 
'<PUNCTUATION, (>', 
'<PUNCTUATION, )>', 
'<PUNCTUATION, :>', 
'<KEYWORD, if>', 
'<PUNCTUATION, (>', 
'<IDENTIFIER, clock>', 
'<OPERATOR, >>', '<INT, 12>', 
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
'''unreachable code detected at stage IDENTIFIER and value clock'''