from compiler import tokenize, parse, check_ast

# Sample Hinglish SQL commands
commands = [
    "bana table students",
    "daal mein students value 'Shobhit'",
    "daal mein students value 'Rahul'",
    "nikal se students"
]

for cmd in commands:
    print(f"\nCommand: {cmd}")
    tokens = tokenize(cmd)
    print("Tokens:", tokens)
    ast = parse(tokens)
    print("AST:", ast)
    result = check_ast(ast)
    print("Result:", result)
