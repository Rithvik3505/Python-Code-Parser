import ply.lex as l
tokens = (
    'Func', 'Id', 'Lpar', 'Rpar', 'Colon', 'Assignment', 'Number', 'if', 'else', 'while',
    'for', 'in', 'range', 'Minus', 'Divide', 'Add', 'Multiply', 'GT', 'LT', 'Comma', 'SLbrac', 'SRbrac', 'String'
)

t_ignore = ' \t'
t_Lpar = r'\('
t_Rpar = r'\)'
t_Colon = r':'
t_Assignment = r'='
t_Comma = r','
t_GT = r'>'
t_LT = r'<'
t_Minus = r'-'
t_Divide = r'/'
t_Add = r'\+'
t_Multiply = r'\*'
t_SLbrac = r'\['
t_SRbrac = r'\]'

def t_Func(t):
    r'def'
    return t

def t_if(t):
    r'if'
    return t

def t_else(t):
    r'else'
    return t

def t_while(t):
    r'while'
    return t

def t_for(t):
    r'for'
    return t

def t_in(t):
    r'in'
    return t

def t_range(t):
    r'range'
    return t

def t_Number(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_Id(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_Newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"'{t.value[0]}' Not Recognised by Lexer")
    t.lexer.skip(1)

lexer = l.lex()