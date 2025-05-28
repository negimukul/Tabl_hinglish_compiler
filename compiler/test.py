from lexer import tokenize
from parser import parse

code = "bana table students"
tokens = tokenize(code)
ast = parse(tokens)
print(ast)
