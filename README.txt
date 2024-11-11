Teammates: Annika Wang (aw3410) and Kira Ariyan (kna2121)

1. Production Rules 
S → FUNCTION 

FUNCTION → ( FUNCTION ) | CONDITION | STATEMENT_BLOCK | id  | int | string | keyword | keyword FUNCTION | id STATEMENT_BLOCK | keyword id(): STATEMENT_BLOCK

CONDITION → ASSIGNMENT | EXPRESSION

STATEMENT_BLOCK → FUNCTION STATEMENT_BLOCK | CONDITION STATEMENT_BLOCK | ε 

EXPRESSION →  int operator int | bool | id operator id | id operator int | id equality_operator bool | id equality_operator int

ASSIGNMENT → id = int | id = string | id = bool | id = EXPRESSION
