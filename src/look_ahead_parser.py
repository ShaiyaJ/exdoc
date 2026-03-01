from itertools import takewhile
import sys
import subprocess

def parse_exdoc(s):
    ret = ""

    while s != '':
        target = s[1:]
        c = s[0]

        if c == '\\': 
            res += target[1]
            s = s[2:]
        elif target.startswith("##*"):
            pass
        elif target.startswith("##"):
            s = s[2:]
            path, s = parse_program_path(s)
            content, s = parse_inline_prog_content(s)

            ret += run_program(path, content)
        elif target.startswith("#*"):
            pass
        elif target.startswith("#"):
            s = s[1:]
            path, s = parse_program_path(s)
            content, s = parse_inline_prog_content(s)

            ret += run_program(path, content)
        else:
            ret += c 
            s = s[1:]

    return ret

def parse_program_path(s):        
    # Remove trailing whitespace to find the first character
    c = ' '

    while c.isspace():
        c = s[0]
        s = s[1:]

    first_chr = c

    # Find which character will "end" the path from the first nonspace char
    end_chr = ' '

    if first_chr == '\'' or first_chr == '"':
        end_chr = first_chr

    # Take up until the end_chr to extract the path
    prepend = '' if end_chr == '\'' or end_chr == '"' else first_chr

    ret = prepend + "".join( [c for c in takewhile(lambda x: x != end_chr, s)] )
    s_without_path = s[ len(ret): ]

    return (ret, s_without_path)

def run_program(program_path, inp):
    return subprocess.check_output(program_path, input=inp.encode("utf-8"), shell=True).decode("utf-8")

def parse_inline_prog_content(s):
    ret = "".join( [c for c in takewhile(lambda x: x != '\n', s)] )
    s_without_content = s[ len(ret): ]

    return (ret, s_without_content)

def parse_multi_line_prog_content(s):
    ret = ""

    while not s.startswith("##"):
        ret += s[0]
        s = s[1:]

    return (ret, s)

if __name__ == "__main__":
    inp = sys.stdin.read()
    out = parse_exdoc(inp)
    sys.stdout.write(out)

"""
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect arguments parsed...\nUsage:\n\texdoc <input path> <output path>")
        exit(1)

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    with open(in_path, "r") as in_file:
        raw = in_file.read()
    out = parse_exdoc(raw)

    with open(out_path, "w") as out_file:
        out_file.write(out)
"""
