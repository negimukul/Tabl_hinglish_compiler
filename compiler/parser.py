# compiler/parser.py

# Each command structure is represented as a dictionary (AST node)
def parse(tokens):
    if not tokens:
        raise ValueError("No tokens to parse.")

    token_index = 0

    def match(expected_type):
        nonlocal token_index
        if token_index < len(tokens) and tokens[token_index][0] == expected_type:
            token = tokens[token_index]
            token_index += 1
            return token[1]
        else:
            raise SyntaxError(f"Expected {expected_type}, got {tokens[token_index] if token_index < len(tokens) else 'EOF'}")

    command_type = tokens[0][0]

    if command_type == "CREATE":
        # bana table students
        match("CREATE")
        match("TABLE")
        table_name = match("IDENTIFIER")
        return {"type": "CREATE", "table": table_name}

    elif command_type == "INSERT":
        # daal mein students value 'Shobhit'
        match("INSERT")
        match("INTO")
        table_name = match("IDENTIFIER")
        match("VALUES")
        value = match("STRING")
        return {"type": "INSERT", "table": table_name, "value": value.strip("'")}

    elif command_type == "SELECT":
        # nikal se students
        match("SELECT")
        match("FROM")
        table_name = match("IDENTIFIER")
        return {"type": "SELECT", "table": table_name}

    else:
        raise SyntaxError(f"Unknown command type: {command_type}")
