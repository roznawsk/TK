import ply.lex as lex

# Dict of keywords
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT',
}

# Tokens definition
tokens = [
             'INTNUM',
    #          'PLUS',
    # 'MINUS',
    # 'TIMES',
    # 'DIVIDE',
    # 'DOTPLUS',
    # 'DOTMINUS',
    # 'DOTTIMES',
    # 'DOTDIVIDE',
             'ADD',
             'DOTADD',
             'ADDASSIGN',
             'SUB',
             'DOTSUB',
             'SUBASSIGN',
             'MUL',
             'DOTMUL',
             'MULASSIGN',
             'DIV',
             'DOTADD',
             'ADDASSIGN',
             'SUB',
             'DOTSUB',
             'SUBASSIGN',
             'MUL',
             'DOTMUL',
             'MULASSIGN',
             'DIV',
             'DOTDIV',
             'DIVASSIGN',
             'ASSIGN',
             'LPAREN',
             'RPAREN',
             'LPARENSQUARE',
             'RPARENSQUARE',
             'LPARENCURLY',
             'RPARENCURLY',
             'COMMENT',
             'EQUALITY',
             'INEQUALITY',
             'GREATER',
             'GREATER_EQUAL',
             'LESS',
             'LESS_EQUAL',
             'RANGE',
             'TRANSPOSE',
             'COMMA',
             'SEMICOLON',
             'FLOATNUM',
             'STRING',
             'ID'
         ] + list(reserved.values())


t_ADD = r'\+'
t_DOTADD = r'\.\+'
t_ADDASSIGN = r'\+='
t_SUB = r'-'
t_DOTSUB = r'\.-'
t_SUBASSIGN = r'-='
t_MUL = r'\*'
t_DOTMUL = r'\.\*'
t_MULASSIGN = r'\*='
t_DIV = r'/'
t_DOTDIV = r'\./'
t_DIVASSIGN = r'/='
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LPARENSQUARE = r'\['
t_RPARENSQUARE = r'\]'
t_LPARENCURLY = r'\{'
t_RPARENCURLY = r'\}'
t_COMMENT = r'\#.*\n*'
t_EQUALITY = r'=='
t_INEQUALITY = r'!='
t_GREATER = r'>'
t_GREATER_EQUAL = r'>='
t_LESS = r'<'
t_LESS_EQUAL = r'<='
t_RANGE = r':'
t_TRANSPOSE = r'\''
t_COMMA = r','
t_SEMICOLON = r';'
t_STRING = r'".*"'


# def t_ID(t):
#     r'[a-zA-Z_]\w*'
#     return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    if t.value in reserved.keys():
        t.type = reserved[t.value]
    else:
        t.type = "ID"
    return t


def t_FLOATNUM(t):
    r'(((\d*\.\d+)|(\d+\.\d*))(E(-)?\d+)?)|(\d+E(-)?\d+)'  # 0.5, .5, 20., 20E2, 0.5E2, .5E2, 20.E2 etc
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

def t_newline(t):
    r'(\#.*\n*)|\n+'
    i = 0
    for c in t.value:
        if c == '\n':
            i = i + 1
    t.lexer.lineno += i


t_ignore = '    \t'


def t_error(t):
    print("\033[1;31;40mIllegal character '%s' at (%d,%d)" % (t.value[0], t.lineno))
    t.lexer.skip(1)


lexer = lex.lex()