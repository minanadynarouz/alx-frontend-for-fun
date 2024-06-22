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


def list_type_start(ordered=False):
    """Return a function to parse a list item"""
    if (ordered):
        return '<ol>\n'
    else:
        return '<ul>\n'


def list_type_end(ordered=False):
    """Return a function to parse a list item"""
    if (ordered):
        return '</ol>\n'
    else:
        return '<ul>\n'


def convert_to_html(in_file, out_file):
    '''
    Convert markdown to HTML
    '''
    html = []
    inside_list = False  # State variable to track if we are inside a list
    with open(in_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            if line.startswith('#'):
                if inside_list:
                    html.append('</ul>\n')
                    inside_list = False
                level = len(line.split(' ')[0])
                header_content = line[level:].strip()
                html.append(f"<h{level}>{header_content}</h{level}>\n")
            elif line.startswith('-'):
                if not inside_list:
                    html.append('<ul>\n')
                    inside_list = True
                item_content = line[1:].strip()
                html.append(f'\t<li>{item_content}</li>\n')
            elif line.startswith('*'):
                if not inside_list:
                    html.append('<ol>\n')
                    inside_list = True
                item_content = line[1:].strip()
                html.append(f'\t<li>{item_content}</li>\n')
            else:
                if inside_list and line.startswith('-'):
                    html.append('</ol>\n')
                    inside_list = False
                elif inside_list:
                    html.append('</ul>\n')
                    inside_list = False
                html.append(f'{line}\n')

    if inside_list:
        html.append('</ol>\n')

    with open(out_file, "w") as f:
        f.write(''.join(html))


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html')
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
