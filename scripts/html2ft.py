#!/usr/bin/env python3
"""
HTML to FT Converter CLI

A command-line utility that converts HTML strings to FT format using 
the html2ft function from fasthtml.components.
"""

import argparse
import sys
from fasthtml.components import html2ft

def main():
    parser = argparse.ArgumentParser(
        description='Convert HTML to FT format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  html2ft_cli.py "<div>Hello World</div>"
  echo "<div>Hello World</div>" | html2ft_cli.py
  html2ft_cli.py -f input.html
  html2ft_cli.py -f input.html -o output.py
  html2ft_cli.py "<div>Hello World</div>" --attr1st
"""
    )
    
    input_group = parser.add_argument_group('Input options (choose one)')
    input_mutex = input_group.add_mutually_exclusive_group()
    input_mutex.add_argument('html', nargs='?', help='HTML string to convert')
    input_mutex.add_argument('-f', '--file', help='Input file containing HTML')
    
    parser.add_argument('-o', '--output', help='Output file (default: stdout)')
    parser.add_argument('--attr1st', action='store_true', 
                      help='Put attributes before children in the output')
    
    args = parser.parse_args()

    # Get HTML input
    html_content = None
    
    if args.html:
        # HTML provided as command-line argument
        html_content = args.html
    elif args.file:
        # HTML from file
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                html_content = f.read()
        except Exception as e:
            print(f"Error reading file {args.file}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # HTML from stdin if available
        if not sys.stdin.isatty():
            html_content = sys.stdin.read()
        else:
            parser.print_help()
            sys.exit(1)
    
    if not html_content:
        print("No HTML content provided", file=sys.stderr)
        sys.exit(1)
    
    # Convert HTML to FT
    try:
        ft_output = html2ft(html_content, attr1st=args.attr1st)
    except Exception as e:
        print(f"Error converting HTML to FT: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Output result
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(ft_output)
        except Exception as e:
            print(f"Error writing to file {args.output}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(ft_output)

if __name__ == '__main__':
    main() 