import ply.lex as lex
import sys

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'then': 'THEN',
    'endif' : 'ENDIF',
    'print' : 'PRINT',
}

tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'NUMBER_INT',
    'NUMBER_FLOAT',
    'IDENTIFIER',
    'TRUE',
    'FALSE',

    'EQ',
    'NE',
    'GT',
    'LT'
) + tuple(reserved.values())


t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'


# t_PRINT = r'print'

def t_NUMBER_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_IDENTIFIER(t): # names for variables
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_TRUE(t):
    'true'
    t.value = True
    return t

def t_FALSE(t):
    'false'
    t.value = False
    return t

t_EQ = r'=='
t_NE = r'!='
t_GT = r'>'
t_LT = r'<'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore_comment = r'\#.*'


t_ignore = ' \t'  # ignore spaces and tabs

lexer = lex.lex()

def main():
    # lexer = lex.lex()
    data = sys.argv[1]
    lexer.input(data)
    for tok in lexer:
        print(tok)


if __name__ == '__main__':
    main()