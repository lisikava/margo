from lexer import lexer
from parser import parser
import sys

if len(sys.argv) >= 2:
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            data = file.read()
            # print(data)
    except FileNotFoundError:
        print('File not found')
else:
    while True:
        data = input('margo > ')
        if not data:
            continue
        parser.parse(data)

print(parser.parse(data))
