
import ply.lex as lex

# List of token names.   This is always required

reserved = {
    'if': 'IF',
    'else': 'ELSE'
}

tokens = (
'ID',
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'RPAREN',
) + tuple(reserved.values())


# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_ID(t):
    r'\w+'
    t.type = reserved.get(t.value, 'ID')
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
var if 2var
'''

# Give the lexer some input
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)


inmode = 2
            #in
def in_mode(var):
    print(var)
    a = var * 5
    print(a)

def out_mode():
    return 'pendejada'

         # 0  #0    # 11  #array[0]
def nombre(i, start, end, array):

    for new_idx in range(start + 1, end):
        print(array)
        i = new_idx

a = [1,2,3,4,5,6,7,8,9,9]
i = 0

nombre(i, 0, len(a), a[i])