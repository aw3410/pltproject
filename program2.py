from parser import parser
from scanner import scan
from generator import generator

#scanner input
input = "castSpell repeat(): clock = 12 untilClockStrikes (12): clock = clock - 1 paint(clock)"
scanner_output = scan(input)
ast = parser(scanner_output)
generator_output = generator(ast)

final_pipeline_code = generator_output + "\nrepeat()" #function call
print(final_pipeline_code)


#Expected scanner output:
'''output = ['<KEYWORD, castSpell>', 
          '<IDENTIFIER, repeat>', 
          '<PUNCTUATION, (>', 
          '<PUNCTUATION, )>', 
          '<PUNCTUATION, :>', 
          '<IDENTIFIER, clock>', 
          '<ASSIGNMENT_OPERATOR, =>', 
          '<INT, 12>', 
          '<KEYWORD, untilClockStrikes>', 
          '<PUNCTUATION, (>',
          '<INT, 12>', 
          '<PUNCTUATION, )>', 
          '<PUNCTUATION, :>', 
          '<IDENTIFIER, clock>', 
          '<ASSIGNMENT_OPERATOR, =>', 
          '<IDENTIFIER, clock>', 
          '<OPERATOR, ->', 
          '<INT, 1>', 
          '<KEYWORD, paint>', 
          '<PUNCTUATION, (>', 
          '<IDENTIFIER, clock>', 
          '<PUNCTUATION, )>'] '''


#Expected parser output 
''' FUNCTION (castSpell)
 ├──   IDENTIFIER (repeat)
 └──   STATEMENT_BLOCK
   ├──     ASSIGNMENT
     ├──       IDENTIFIER (clock)
     ├──       =
     └──       INT (12)
   └──     FUNCTION (untilClockStrikes)
     ├──       INT (12)
     └──       STATEMENT_BLOCK
       ├──         ASSIGNMENT
         ├──           IDENTIFIER (clock)
         ├──           =
         └──           EXPRESSION
           ├──             IDENTIFIER (clock)
           ├──             -
           └──             INT (1)
       └──         FUNCTION (paint)
         └──           IDENTIFIER (clock) '''

# Expected codegen output
'''castSpell repeat(): 
        clock = 12 
        untilClockStrikes (12): 
          clock = clock - 1 
            paint(clock)'''