
from scanner import scan
from parser import parser
from generator import CodeGenerator

def main():
  # scanner input 
  input = "castSpell princess(): paint('hello princess')"
  scanner_output = scan(input) 
  ast = parser(scanner_output) #pass scanner output to parser 

  codegen = CodeGenerator(ast)
  codegen.generate_code()
  generated_code = codegen.output_code()
  print(generated_code)


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
