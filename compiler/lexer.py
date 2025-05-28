# compiler/lexer.py

import re

# Define token types
TOKENS = [
    ("CREATE", r"\bbana\b"),                  # bana table students
    ("INSERT", r"\bdaal\b"),                  # daal mein students value 'Shobhit'
    ("INTO", r"\bmein\b"),
    ("VALUES", r"\bvalue\b"),
    ("SELECT", r"\bnikal\b"),
    ("FROM", r"\bse\b"),
    ("TABLE", r"\btable\b"),
    ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"), # table name, column name
    ("STRING", r"'[^']*'"),                   # 'Shobhit'
    ("COMMA", r","),
    ("SKIP", r"[ \t\n]+"),                    # Whitespace
    ("MISMATCH", r"."),                       # Anything else (error)
]

# Lexer function: converts source code (Hinglish command) into list of tokens
def tokenize(code):
    tokens = []
    index = 0

    while index < len(code):
        matched = False
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code, index)
            if match:
                value = match.group(0)
                if token_type == "SKIP":
                    pass  # ignore whitespace
                elif token_type == "MISMATCH":
                    raise SyntaxError(f"Unexpected token: {value}")
                else:
                    tokens.append((token_type, value))
                index = match.end()
                matched = True
                break
        if not matched:
            raise SyntaxError(f"Illegal character at index {index}: {code[index]}")
    return tokens

# input = "daal mein students value 'Shobhit'"
# print(tokenize(input))
