tokens = [ token('KEYWORD', 'castSpell'),
    token('IDENTIFIER', 'princess'),
    token('PUNCTUATION', '('),
    token('PUNCTUATION', ')'),
    token('PUNCTUATION', ':'),
    token('KEYWORD', 'paint'),
    token('PUNCTUATION', '('),
    token('STRING', 'hello princess'),
    token('PUNCTUATION', ')') ]

# expected output: 
# FUNCTION (castSpell)
# ├──   IDENTIFIER (princess)
# └──   STATEMENT_BLOCK
#   └──     FUNCTION (paint)
#     └──       STRING (hello princess)