# HTML to FT Converter CLI

A command-line utility that converts HTML strings to FT format using the `html2ft` function from `fasthtml.components`.

## Installation

The CLI tool is part of the Flowbite project. Make sure you have the project dependencies installed:

```bash
# From the project root
pip install -e .
```

## Usage

```
usage: html2ft_cli.py [-h] [-f FILE] [-o OUTPUT] [--attr1st] [html]

Convert HTML to FT format

positional arguments:
  html                  HTML string to convert

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file (default: stdout)
  --attr1st             Put attributes before children in the output

Input options (choose one):
  -f FILE, --file FILE  Input file containing HTML

Examples:
  html2ft_cli.py "<div>Hello World</div>"
  echo "<div>Hello World</div>" | html2ft_cli.py
  html2ft_cli.py -f input.html
  html2ft_cli.py -f input.html -o output.py
  html2ft_cli.py "<div>Hello World</div>" --attr1st
```

## Examples

### Converting HTML from a command-line argument

```bash
./html2ft_cli.py "<div class='container'>Hello World</div>"
```

Output:
```python
Div(
    'Hello World',
    cls='container'
)
```

### Converting HTML from a file

```bash
./html2ft_cli.py -f input.html
```

### Saving the output to a file

```bash
./html2ft_cli.py -f input.html -o output.py
```

### Using the --attr1st option

This option puts attributes before children in the output:

```bash
./html2ft_cli.py "<div class='container'>Hello World</div>" --attr1st
```

Output:
```python
Div(cls='container')(
    'Hello World'
)
```

### Piping HTML from another command

```bash
echo "<div>Hello World</div>" | ./html2ft_cli.py
```

## Note

This tool is designed to help you convert HTML to FT format, which is useful for creating FastHTML components programmatically. 