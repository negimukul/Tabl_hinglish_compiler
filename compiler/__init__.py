# __init__.py

from .lexer import tokenize
from .parser import parse
from .semantic import check_ast
from .interpreter import execute

__all__ = ["tokenize", "parse", "check_ast", "execute"]
