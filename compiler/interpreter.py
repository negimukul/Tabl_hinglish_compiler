# compiler/interpreter.py

from .lexer import tokenize
from .parser import parse
from .semantic import check_ast

# Simple in-memory "database"
DATABASE = {}

# compiler/interpreter.py

def execute(ast, db):
    if ast["type"] == "CREATE":
        table_name = ast["table"]
        if table_name in db:
            return f"Table '{table_name}' already exists."
        db[table_name] = []
        return f"Table '{table_name}' created."

    elif ast["type"] == "INSERT":
        table_name = ast["table"]
        if table_name not in db:
            return f"Table '{table_name}' does not exist."
        value = ast["value"]
        db[table_name].append(value)
        return f"Value '{value}' inserted into table '{table_name}'."

    elif ast["type"] == "SELECT":
        table_name = ast["table"]
        if table_name not in db:
            return f"Table '{table_name}' does not exist."
        return db[table_name]

    else:
        return "Unknown command."
