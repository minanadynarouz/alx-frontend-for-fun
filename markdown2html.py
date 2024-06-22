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


def convert_md_to_html(input_file, output_file):
    '''
    Converts markdown file to HTML file
    '''
    # Read the contents of the input file
    with open(input_file, encoding='utf-8') as f:
        md_content = f.readlines()

    html_content = []
    for line in md_content:
        # Check if the line is a heading
        hashes = re.findall(r'#', line)
        h_content = re.findall(r'\w', line)
        if hashes:
            h_level = len(hashes)
            # Append the HTML equivalent of the heading
            html_content.append(f'<h{h_level}>{"".join(h_content)}</h{h_level}>\n')
        else:
            html_content.append(line)

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(html_content)


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    input_path = pathlib.Path(input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    # Convert the markdown file to HTML
    convert_md_to_html(input_file, output_file)

