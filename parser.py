
class Token:
    def __init__(self, token_type, value):
        self.type = token_type 
        self.value = value 

    
tokens = [
    Token(type='CASTSPELL', value='castSpell'),
    Token(type='IDENTIFIER', value='awaken'),
    Token(type='IDENTIFIER', value='princess'),
    Token(type='PAINT', value='paint'),
    Token(type='IDENTIFIER', value='crown'),
    Token(type='STRING', value='shining')
]



