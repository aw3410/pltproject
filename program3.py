from scanner import scan
from parser import parser


#scanner input
input = "castSpell helloWorld: paint('Hello kingdom')"
scanner_output = scan(input)
parser(scanner_output)

#Expected scanner output

'''scan_output = ['<KEYWORD, castSpell>', 
          '<IDENTIFIER, repeat>', 
          '<PUNCTUATION, (>', 
          '<PUNCTUATION, )>', 
          '<PUNCTUATION, :>', 
          '<IDENTIFIER, clock>', 
          '<ASSIGNMENT_OPERATOR, =>', 
          '<INT, 12>', 
          '<KEYWORD, untilClockStrikes>', 
          '<PUNCTUATION, (>',
          '<PUNCTUATION, )>', 
          '<PUNCTUATION, :>', 
          '<IDENTIFIER, clock>', 
          '<ASSIGNMENT_OPERATOR, =>', 
          '<IDENTIFIER, clock>', 
          '<OPERATOR, ->', 
          '<INT, 1>', 
          '<KEYWORD, paint>', 
          '<PUNCTUATION, (>',  
          '<PUNCTUATION, )>'] '''


#Expected parser output: 
#Parse Error: Function declaration must have parentheses after the identifier.