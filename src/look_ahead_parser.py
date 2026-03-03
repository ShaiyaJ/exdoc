from itertools import takewhile
import sys
import subprocess

def parse_exdoc(s, ext=".txt"):
    ret = ""

    while s != '':
        c = s[0]

        if c == '\\': 
            ret += s[1]
            s = s[2:]
        elif s.startswith("##*"):
            s = s[3:]
            path, s = parse_program_path(s)
            content, s = parse_multi_line_prog_content(s)

            ret += parse_exdoc(run_program(path, content, ext))
        elif s.startswith("##"):
            s = s[2:]
            path, s = parse_program_path(s)
            content, s = parse_multi_line_prog_content(s)

            ret += run_program(path, content, ext)
        elif s.startswith("#*"):
            s = s[2:]
            path, s = parse_program_path(s)
            content, s = parse_inline_prog_content(s)

            ret += parse_exdoc(run_program(path, content, ext))
        elif s.startswith("#"):
            s = s[1:]
            path, s = parse_program_path(s)
            content, s = parse_inline_prog_content(s)

            ret += run_program(path, content, ext)
        else:
            ret += c 
            s = s[1:]

    return ret

def parse_program_path(s):        
    # Remove trailing whitespace to find the first character
    c = s[0]

    while c.isspace():
        c = s[0]
        s = s[1:]
        #print(s)
        #print("--")

    first_chr = c

    # Find which character will "end" the path from the first nonspace char
    end_chr = ' '

    if first_chr == '\'' or first_chr == '"':
        end_chr = first_chr

    # Take up until the end_chr to extract the path
    #prepend = '' if end_chr == '\'' or end_chr == '"' else first_chr

    #ret = prepend + "".join( [c for c in takewhile(lambda x: x != end_chr, s)] )
    ret = "".join( [c for c in takewhile(lambda x: x != end_chr, s)] )
    s_without_path = s[ (len(ret) + len(end_chr) + 1): ]

    return (ret, s_without_path)

def run_program(program_path, inp, ext):
    full_inp = (ext + "\n" + inp).encode("utf-8")
    out = subprocess.check_output(program_path, input=full_inp, shell=True)

    return out.decode("utf-8")

def parse_inline_prog_content(s):
    ret = "".join( [c for c in takewhile(lambda x: x != '\n', s)] )
    s_without_content = s[ len(ret): ]

    return (ret, s_without_content)

def parse_multi_line_prog_content(s):
    ret = ""

    while not s.startswith("##"):
        ret += s[0]
        s = s[1:]

    s_without_delim = s[2:]

    return (ret, s_without_delim)

if __name__ == "__main__":
    ext = ".txt" if len(sys.argv) == 1 else sys.argv[-1]

    inp = sys.stdin.read()
    out = parse_exdoc(inp, ext)
    sys.stdout.write(out)
