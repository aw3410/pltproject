
#scanner.py 

def scan(input):
    current = ''
    state = 's0'
    i = 0
    tokenType = ''
    keywords = ['castSpell', 'if', 'untilClockStrikes','paint','happilyEverAfter']
    bool = ['alive', 'dead']
    punctuation = [',', '.', '(', ')', '{', '}', ';', ':']
    operators = ['>=', '<=','>','<','-', '+', '*', '/']
    assignment_operator = '='
    equality_operators = ['is', 'is not']
    tokens = []
    errormessage = ["Error:"]
    open_brackets = 0

    while state != 's_err' and i < len(input):
        c = input[i]

        if c.isspace():
            i += 1
            continue
        
        if c in ('"', "'"):
            start = i
            tokenType = 'STRING'
            current = c  # Start capturing the string
            i += 1
            c = input[i]
            
            while c not in ('"', "'") and i < len(input):
                current += c
                i += 1
                c = input[i] if i < len(input) else 'eof'

            if c == 'eof':
                errormessage.append('Unclosed string starting at position ' + str(start))
                state = 's_err'
            else:
                current += c  # Add closing quote
                tokens.append('<' + tokenType + ', ' + current + '>')
                i += 1  # Move past the closing quote
            
        elif c.isdigit():
            tokenType = 'INT'
            current = c
            i += 1
            while i < len(input) and input[i].isdigit():
                c = input[i]
                current += c
                i += 1
            tokens.append('<' + tokenType + ', ' + current + '>')
        
        elif c in operators:
            tokenType = 'OPERATOR'
            current = c
            i += 1
            tokens.append('<' + tokenType + ', ' + current + '>')
        
        elif c in punctuation:
            tokenType = 'PUNCTUATION'
            current = c
            tokens.append('<' + tokenType + ', ' + current + '>')
            i += 1

            if c == '(' or c == '{':
                open_brackets += 1
            elif c == ')' or c == '}':
                open_brackets -= 1
        
        elif c == '=': 
            tokenType = 'ASSIGNMENT_OPERATOR'
            current = c
            tokens.append('<' + tokenType + ', ' + current + '>')
            i += 1
        
        elif c.isalpha():
            current = c
            i += 1
            while i < len(input) and (input[i].isalpha() or input[i].isdigit()):
                c = input[i]
                current += c
                i += 1
            if current in keywords:
                tokenType = 'KEYWORD'

            elif c in equality_operators: 
                tokenType = 'EQUALITY_OPERATOR'

            elif c in bool: 
                tokenType = 'BOOL'

            else:
                tokenType = 'IDENTIFIER'
            tokens.append('<' + tokenType + ', ' + current + '>')
        
        else:
            errormessage.append('Error at position ' + str(i) + ': ' + c + ' is an invalid character')
            state = 's_err'
            i += 1

    if open_brackets != 0:
        errormessage.append('Unmatched bracket or parenthesis')
        state = 's_err'

    if state != 's_err':
        return tokens
    else:
        return str(errormessage)

