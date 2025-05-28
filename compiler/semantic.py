# compiler/semantic.py

# This will simulate a simple in-memory database
DATABASE = {}

def check_ast(ast):
    """
    Perform semantic analysis and execution of the AST node.
    
    Parameters:
        ast (dict): The abstract syntax tree node from parser.
    
    Returns:
        str or list: Confirmation message or query results.
    """
    if not isinstance(ast, dict) or 'type' not in ast:
        raise ValueError("Invalid AST node.")

    command_type = ast["type"]

    if command_type == "CREATE":
        table_name = ast["table"]
        if table_name in DATABASE:
            return f"Error: Table '{table_name}' already exists."
        DATABASE[table_name] = []  # Initialize empty table
        return f"Table '{table_name}' created successfully."

    elif command_type == "INSERT":
        table_name = ast["table"]
        value = ast["value"]
        if table_name not in DATABASE:
            return f"Error: Table '{table_name}' does not exist."
        DATABASE[table_name].append(value)
        return f"Value '{value}' inserted into table '{table_name}'."

    elif command_type == "SELECT":
        table_name = ast["table"]
        if table_name not in DATABASE:
            return f"Error: Table '{table_name}' does not exist."
        return DATABASE[table_name]

    else:
        return f"Error: Unknown command type '{command_type}'."
