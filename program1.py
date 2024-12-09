
from scanner import scan
from parser import parser
from generator import generator

input = "castSpell princess(): paint('hello princess')"
scanner_output = scan(input) 
ast = parser(scanner_output)
generator_output = generator(ast)

final_pipeline_code = generator_output + "\nprincess()" #function call
print(final_pipeline_code)


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
