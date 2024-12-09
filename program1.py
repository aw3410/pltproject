
from scanner import scan
from parser import parser
from generator import generator

input = "castSpell princess(): paint('hello princess')"
scanner_output = scan(input) 
parser(scanner_output)
generator(scanner_output)



#Expected scanner output:
'''['<KEYWORD, castSpell>', 
'<IDENTIFIER, princess>', 
'<PUNCTUATION, (>', 
'<PUNCTUATION, )>', 
'<PUNCTUATION, :>', 
'<KEYWORD, paint>', 
'<PUNCTUATION, (>', 
"<STRING, 'hello princess'>", 
'<PUNCTUATION, )>'] '''


#Expected parser output: 
'''FUNCTION (castSpell)
 ├──   IDENTIFIER (princess)
 └──   STATEMENT_BLOCK
   └──     FUNCTION (paint)
     └──       STRING ('hello princess') '''

#Expected codegen output:
'''def princess():
  print('hello princess')'''
