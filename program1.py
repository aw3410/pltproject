
from parser import parser, token
# scanner input 

# castSpell princess():
#   paint('hello princess)


#scanner output

output = ['<KEYWORD, castSpell>', 
 '<IDENTIFIER, princess>', 
 '<PUNCTUATION, (>', 
 '<PUNCTUATION, )>', 
 '<PUNCTUATION, :>', 
 '<KEYWORD, paint>',
'<PUNCTUATION, (>', 
'<STRING, "hello princess">', 
'<PUNCTUATION, )>']


parser(output)

# expected output: 
# FUNCTION (castSpell)
# ├──   IDENTIFIER (princess)
# └──   STATEMENT_BLOCK
#   └──     FUNCTION (paint)
#     └──       STRING ("hello princess")