import sys
import Mparser, scanner

if __name__ == '__main__':

    filename = sys.argv[1] if len(sys.argv) > 1 else "example1.m"
    try:
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = Mparser.parser
    text = file.read()
    parser.parse(text, lexer=scanner.lexer)
