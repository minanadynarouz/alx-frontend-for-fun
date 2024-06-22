#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import pathlib
import re
import sys
import string


def convert_to_html(in_file, out_file):
    '''
    Convert markdown to HTML
    '''
    html = []
    with open(in_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            if line.startswith('#'):
                level = len(line.split(' ')[0])
                header_content = line[level:].strip()
                html.append(f"<h{level}>{header_content}</h{level}>\n")
            elif line.startswith('-'):
                items = line.split('- ')[1:]
                html.append('<ul>\n\t')
                for item in items:
                    html.append(f'\t<li>{item}</li>')
                html.append('\n\t</ul>')
            else:
                html.append(f'{line}\n')

    with open(out_file, "w") as f:
        f.write(''.join(html))


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    input_path = pathlib.Path(input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    # Convert the markdown file to HTML
    convert_to_html(input_file, output_file)

