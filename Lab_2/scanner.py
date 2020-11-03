import ply.lex as lex

literals = "+-*/=()[]{}:',;<>"

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

tokens = [
    'DOTPLUS',
    'DOTMINUS',
    'DOTTIMES',
    'DOTDIVIDE',
    'PLUSASSIGN',
    'MINUSASSIGN',
    'TIMESASSIGN',
    'DIVIDEASSIGN',
    'LESSTHANEQ',
    'GREATERTHANEQ',
    'NOTEQUAL',
    'EQUAL',
    'ID',
    'INTNUM',
    'FLOATNUM',
    'STRING' ] + list(reserved.values())

t_DOTPLUS = r'\.\+'
t_DOTMINUS = r'\.\-'
t_DOTTIMES = r'\.\*'
t_DOTDIVIDE = r'\.\/'
t_PLUSASSIGN = r'\+='
t_MINUSASSIGN = r'\-='
t_TIMESASSIGN = r'\*='
t_DIVIDEASSIGN = r'\/='
t_LESSTHANEQ = r'<='
t_GREATERTHANEQ = r'>='
t_NOTEQUAL = r'!='
t_EQUAL = r'=='
t_STRING = r'".*"'


def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value,'ID')
    return t


def t_FLOATNUM(t):
    r'(((\d*\.\d+)|(\d+\.\d*))(E(-)?\d+)?)|(\d+E(-)?\d+)'
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment(t):
    r'\#.*'

t_ignore = '    \t'


def t_error(t):
    print("Illegal character '%s' at (%d)" % (t.value[0], t.lineno))
    t.lexer.skip(1)


lexer = lex.lex()