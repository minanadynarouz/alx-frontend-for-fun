#!/usr/bin/python3
'''Markdown to HTML'''

import sys
import os.path as path


if __name__ == "__main__":
    '''Check if the number of arguments is correct'''
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]

    if not path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)
