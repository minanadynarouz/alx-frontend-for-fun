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
    inside_list = False  # State variable to track if we are inside a list
    previous_line = ''
    inside_para = False

    def close_paragraph():
        nonlocal inside_para
        if inside_para:
            html.append("</p>\n")
            inside_para = False

    with open(in_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            if line.startswith('#'):
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
                if (previous_line.startswith('-') and inside_list):
                    html.append('</ul>\n')
                    inside_list = False
                elif inside_list:
                    html.append('</ol>\n')
                    inside_list = False

                if line.strip():
                    if not inside_para:
                        html.append('<p>\n')
                        inside_para = True
                    else:
                        html.append("<br/>\n")
                    html.append(f"{line}\n")
                else:
                    close_paragraph()
            previous_line = line

    close_paragraph()

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
