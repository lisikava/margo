# Intro
Presented to you is *margo*, a compiler for a simple toy language. 

So far, the first two stages of a compiler, the lexer and the parser, 
have been implemented. The plans for this project include adding code optimization and 
generation into an IR. However, the compiler already works as a simple interpreter,
as presented in the attached example files. 

The compiler supports:
- simple arithmetic operations (+, -, *, /) on ints and floats: `5 * (3 + 4)`
- variable declarations: `a = 5.5`
- print statements: `print(a)`
- logical statements: `print(a > b)`
- conditional statements: `if a < b then print(a) endif`
# Running
- [ ] Clone the repository into your location of choice
- [ ]  Create a virtual environment:
`python -m venv venv`
- [ ] Activate the virtual environment:
`source venv/bin/activate`
- [ ] Install the required package(s):
`pip install -r requirements.txt`
- [ ] Run main:

`python main.py` to enter *margo* console; 

`python main.py example1.mar` to translate program inside file `example1.mar`

- [ ] If you want, you may run the lexer or parser individually to see the results of the respective compiler stage
  (_note: the parser's output is the same as main's output_):
`python lexer.py "a = 5"` or `python parser.py "5 + 3"`
