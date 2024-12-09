from scanner import scan
from parser import parser
from generator import generator


#scanner input
input = 'castSpell repeat(): clock = 12 untilClockStrikes (): clock = clock - 1 paint()'
scanner_output = scan(input)
parser(scanner_output)
generator_output = generator(scanner_output)
print(generator_output)

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