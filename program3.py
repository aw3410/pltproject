from scanner import scan
from parser import parser, token



input = "castSpell helloWorld: paint('Hello kingdom')"
scanner_output = scan(input)
parser(scanner_output)


#expected scanner output

'''output = ['<KEYWORD, castSpell>', 
 '<IDENTIFIER, helloWorld>', 
 '<PUNCTUATION, :>', 
 '<KEYWORD, paint>', 
 '<PUNCTUATION, (>', 
 "<STRING, 'Hello kingdom'>", 
 '<PUNCTUATION, )>']'''


<<<<<<< HEAD
parser(output)
=======

>>>>>>> a25ee5ed4819db62d2777d0bb01f520ab4ed7772
#expected output: 
#Parse Error: Function declaration must have parentheses after the identifier.