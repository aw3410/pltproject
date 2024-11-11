Teammates: Annika Wang (aw3410) and Kira Ariyan (kna2121)

1. Production Rules 
        S → FUNCTION 

        FUNCTION → ( FUNCTION ) | CONDITION | STATEMENT_BLOCK | id  | int | string | keyword | keyword FUNCTION | id STATEMENT_BLOCK | keyword id(): STATEMENT_BLOCK

        CONDITION → ASSIGNMENT | EXPRESSION

        STATEMENT_BLOCK → FUNCTION STATEMENT_BLOCK | CONDITION STATEMENT_BLOCK | ε 

        EXPRESSION →  int operator int | bool | id operator id | id operator int | id equality_operator bool | id equality_operator int

        ASSIGNMENT → id = int | id = string | id = bool | id = EXPRESSION

    TERMINALS
        Identifier
            Variable names are letters or digits, starting with a letter
            [a-z][a-z0-9]*
            IDENTIFIER(value = “x”)

        Int
            A non-empty string of digits
            [0-9]+
            INT(value = “5”)

        Keyword
            A fixed set of reserved words 
            ['castSpell', 'if', 'untilClockStrikes','paint','happilyEverAfter']
            KEYWORD(value = "castSpell")

        String Literal 
            String literals are contained in quotation marks 
            “Aurora is sleeping”
            [a-z0-9]*
            STRING(value= “aurora is sleeping”)

        Bool 
            A result that can only have one of two possible values: true or false
            ['alive', 'dead']
            BOOL(value = "alive")

        Operator
            Arithmetic operators
            ['>=', '<=','>','<','-', '+', '*', '/']
            OPERATOR(value = "+")

        Assignment Operator
            Assignment operator
            ['=']
            ASSIGNMENT_OPERATOR(value = "=")

        Punctuation 
            Commas, semicolons, braces, colons, parentheses 
            [ , | . | ( | ) | { | } | ; | :]
            PUNCTUATION(value = “:”)

        Equality Operators 
            equality operators 
            ['is', 'is not']
            EQUALITY_OPERATOR(value = 'is')