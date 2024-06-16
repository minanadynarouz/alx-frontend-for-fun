#!/usr/bin/python3

"""
A script to convert a Markdown file to an HTML file.
"""

import sys
import os
import markdown


def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    html_content = markdown.markdown(markdown_content)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    sys.exit(0)


if __name__ == "__main__":
    main()
