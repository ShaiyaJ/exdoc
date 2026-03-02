from . import parse_exdoc

# CLI wrapper for the parser

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
