# Simple extendable note taking application

import sys
import subprocess

def peek(file):
    position = file.tell()
    c = file.read(1)
    file.seek(position)

    return c

def takewhile(fn, file):
    c = file.read(1)

    while fn(c) and c != '':
        yield c
        c = file.read(1)

def parse_chr(out, file):
    c = file.read(1)

    match c:
        case '\\':          # Start of escapse sequence
            return parse_esc(out, file)
        case '#':           # Start of some type of expression
            return parse_expr_path(out, file)
        case '':            # Ending condition
            return out

    return parse_chr(out + c, file)


def parse_esc(out, file):
    return parse_chr(out + file.read(1), file) 


def parse_expr_path(out, file):
    expr_type = parse_multi_line_expr if peek(file) == '#' else parse_expr

    # Consuming trailing whitespace and extra #'s
    c = file.read(1)

    while c.isspace() or c == '#':  
        c = file.read(1)

    # Determining ending character of path (is it a space or quote)
    endchrs = [' ', '\t', '\n']

    if   c == '"':      endchrs = '"'
    elif c == '\'':     endchrs = '\''

    # Take until the end character is reached
    path = [p for p in takewhile( lambda x: x not in endchrs, file ) ]
    path_str = c + "".join(path)

    # Call the appropriate expression type
    return expr_type(out, file, path_str)


def parse_expr(out, file, path):
    content = [ c for c in takewhile( lambda x: x != '\n', file ) ]
    content_str = "".join(content)

    output = subprocess.check_output(path, input=content_str.encode("utf-8"), shell=True).decode("utf-8")

    return parse_chr(out + output, file) 


def parse_multi_line_expr(out, file, path):
    content = []

    # Append to content until the next '#'
    while True:
        content += [ c for c in takewhile( lambda x: x != '#', file ) ]
        
        # If the next character is '#' then it's '##', the end of a multi line expression
        n = peek(file)

        if n == '#' or n == '':
            file.read(1)
            break

    content_str = "".join(content)

    output = subprocess.check_output(path, input=content_str.encode("utf-8"), shell=True).decode("utf-8")

    return parse_chr(out + output, file) 


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect arguments parsed...\nUsage:\n\texdoc <input path> <output path>")
        exit(1)

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    with open(in_path, "r") as in_file:
        with open(out_path, "w") as out_file:
            out_file.write( parse_chr("", in_file) )

