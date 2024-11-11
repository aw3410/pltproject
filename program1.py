
from scanner import scan
from parser import parser, token

# scanner input 
input = "castSpell princess(): paint('hello princess')"
scanner_output = scan(input) 
parser(scanner_output) #pass scanner output to parser 

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