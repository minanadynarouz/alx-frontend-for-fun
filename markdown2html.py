#!/usr/bin/python3
''' Markdown to HTML '''


import sys
import os.path as path


def convert_to_html(in_file, out_file):
    '''
    Convert markdown to HTML
    '''
    html = []
    with open(in_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if (line.startswith('#')):
                level = line.count('#')
                hash_index = line.rindex("#")
                line = line[hash_index + 1:].strip()
                html.append(f"<h{level}>{line}</h{level}>\n")
                with open(out_file, "w") as f:
                    f.write(''.join(html))


def main():
    ''' Check if the number of arguments is correct '''
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    convert_to_html(input_file, output_file)

    sys.exit(0)


if __name__ == "__main__":
    main()
