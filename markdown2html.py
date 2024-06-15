from sys import argv
from os.path import exists

script, input_file, output_file = argv

if (len(argv) != 3):
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)
elif (input_file.endswith('.md') or not exists(input_file)):
    print("Missing <filename>")
