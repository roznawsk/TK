import sys
from itertools import count
from scanner import lexer, find_column  # noqa
from Mparser import parser
from TreePrinter import TreePrinter  # noqa
from TypeChecker import TypeChecker
from Interpreter import Interpreter

if __name__ == '__main__':
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()

    # lexer.input(text)
    # for token in lexer:
    #     # column = find_column(text, token)
    #     # print('(%d,%d): %s(%s)' % (token.lineno, column, token.type, token.value))
    #     print('(%d): %s(%s)' % (token.lineno, token.type, token.value))

    ast = parser.parse(text, lexer=lexer)
    if not parser.errorok:
        raise SystemExit

    # ast.printTree()

    typeChecker = TypeChecker()
    typeChecker.visit(ast)
    if not typeChecker.errorok:
        raise SystemExit

    ast.accept(Interpreter())
