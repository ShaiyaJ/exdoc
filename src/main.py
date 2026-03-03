# CLI wrapper for the parser
import os.path
import sys
from look_ahead_parser import parse_exdoc 

if __name__ == "__main__":
    # Check arguments and assign arguments to find input and output paths
    if len(sys.argv) != 3:
        print("Incorrect arguments parsed...\nUsage:\n\texdoc <input path> <output path>")
        exit(1)

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    # Open the file and read the raw contents
    with open(in_path, "r") as in_file:
        raw = in_file.read()

    # Get the output file extension 
    _, filetype =  os.path.splitext(out_path)
    out = parse_exdoc(raw, filetype or ".txt")

    # Write the output to the target output file
    with open(out_path, "w") as out_file:
        out_file.write(out)
