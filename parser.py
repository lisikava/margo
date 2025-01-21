import sys

import ply.yacc as yacc
from lexer import tokens

symbol_table = {}  # for variables

precedence = (
    ('left', 'EQ', 'NE', 'GT', 'LT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)
# grammar for first attempt:
# expression : expression + term
#            | expression - term
#            | term
#            | expression <eq> expression
#            | expression <ne> expression
#            | expression <gt> expression
#            | expression <lt> expression

# term : term * factor
#      | term / factor
#      | factor

# factor : <number>
#        | ( expression )

##################################
# statement : expression
#           | <identifier> = expression
#           | <print>(expression)
#           | if_statement
#
# if_statement : <if> expression then_statement else_statement <endif>

# then_statement : <then> expression
# else_statement : <else> statement

def p_program(p):
    'program : statement'
    p[0] = ('program', p[1])

def p_program_statement(p):
    'program : statement program'
    p[0] = ('program', p[1], p[2])

def p_statement_id(p):
    'statement : IDENTIFIER EQUALS expression'
    symbol_table[p[1]] = p[3]


# def p_statement_if_statement(p):
#     'statement : if_statement'
#     p[0] = p[1]

def p_statement_expression(p):
    'statement : expression'
    p[0] = p[1]
    print(p[1])


def p_print(p):
    'statement : PRINT LPAREN expression RPAREN'
    print(p[3])
    p[0] = ('print', p[3])


# def p_if_statement(p):
#     'if_statement : IF expression then_statement else_statement ENDIF'
#     if p[2]:
#         p[0] = p[3]
#     else:
#         p[0] = p[4]


# def p_then_statement(p):
#     'then_statement : THEN expression'
#     p[0] = p[2]


# def p_else_statement(p):
#     'else_statement : ELSE expression'
#     p[0] = p[2]


def p_statement_if(p):
    'statement : IF expression THEN statement ENDIF'
    if p[2]:
        p[0] = p[4]

def p_statement_if_else(p):
    'statement : IF expression THEN statement ELSE statement ENDIF'
    if p[2]:
        p[0] = p[4]
    else:
        p[0] = p[6]

def p_expression_eq(p):
    'boolean : expression EQ expression'
    p[0] = p[1] == p[3]


def p_expression_ne(p):
    'boolean : expression NE expression'
    p[0] = p[1] != p[3]


def p_expression_gt(p):
    'boolean : expression GT expression'
    p[0] = p[1] > p[3]


def p_expression_lt(p):
    'boolean : expression LT expression'
    p[0] = p[1] < p[3]

def p_expression_plus(p):
    'expression : expression PLUS expression'
    try:
        p[0] = p[1] + p[3]
    except TypeError:
        print("Type error")

def p_expression_minus(p):
    'expression : expression MINUS expression'
    try:
        p[0] = p[1] - p[3]
    except TypeError:
        print("Type error")

def p_expression_times(p):
    'expression : expression TIMES expression'
    try:
        p[0] = p[1] * p[3]
    except TypeError:
        print("Type error")

def p_expression_div(p):
    'expression : expression DIVIDE expression'
    try:
        p[0] = p[1] / p[3]
    except TypeError:
        print("Type error")

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_int(p):
    'expression : NUMBER_INT'
    p[0] = p[1]

def p_expression_float(p):
    'expression : NUMBER_FLOAT'
    p[0] = p[1]

def p_boolean(p):
    '''boolean : TRUE
               | FALSE'''
    p[0] = p[1]

def p_expression_boolean(p):
    'expression : boolean'
    p[0] = p[1]

def p_expression_id(p):
    'expression : IDENTIFIER'
    p[0] = symbol_table.get(p[1])

# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     p[0] = p[1] + p[3]
#
#
# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]
#
#
# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]
#
#
# def p_term_times(p):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]
#
#
# def p_term_div(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]
#
#
# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]
#
#
# def p_factor_int(p):
#     'factor : NUMBER_INT'
#     p[0] = p[1]
#
#
# def p_factor_float(p):
#     'factor : NUMBER_FLOAT'
#     p[0] = p[1]
#
#
# def p_factor_id(p):
#     'factor : IDENTIFIER'
#     p[0] = symbol_table.get(p[1])
#
#
# def p_factor_expression(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]


def p_error(p):
    print("Syntax error")
    # print("")

parser = yacc.yacc()


def main():
    data = sys.argv[1]

    print(parser.parse(data))


if __name__ == '__main__':
    main()
