import sys
import os
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

def get_html_content(url):
    """Fetch HTML content from a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        sys.exit(1)

def extract_main_content(html):
    """Extract the div with id="mainContent" and all its content."""
    soup = BeautifulSoup(html, 'html.parser')
    main_content = soup.find('div', id='mainContent')
    
    if not main_content:
        print("Error: Could not find <div id=\"mainContent\"> in the HTML.")
        sys.exit(1)
    
    return main_content

def remove_aside_elements(content):
    """Remove all <aside> elements from the content."""
    asides = content.find_all('aside')
    for aside in asides:
        aside.decompose()
    
    return content

def process_code_examples(content):
    """Process code example elements in the content.
    
    Find elements with class 'code-example', extract the div with class='hidden'
    and data-clipboard-content-html attribute, remove all attributes from this div,
    and replace the original code-example element with this cleaned div.
    """
    # Find all elements with class "code-example"
    code_examples = content.find_all(class_="code-example")
    
    for code_example in code_examples:
        # Find the div with class="hidden" and data-clipboard-content-html attribute
        hidden_div = code_example.find('div', class_="hidden", attrs={"data-clipboard-content-html": True})
        
        if hidden_div:
            # Get the HTML content directly from the attribute
            html_content = hidden_div.get('data-clipboard-content-html')
            
            if html_content:
                # Create a new div with this HTML content
                new_div = BeautifulSoup(f"<div>{html_content}</div>", "html.parser").div
                # print("\n\nCODE EXAMPLE FROM ATTRIBUTE:\n", new_div)
            else:
                # Fallback: Try to get inner HTML directly
                # print("\n\nFALLBACK METHOD - ATTRIBUTE EMPTY\n")
                # Create a new div
                new_div = BeautifulSoup("<div></div>", "html.parser").div
                # Get inner HTML as string and parse it
                inner_html = ''.join(str(c) for c in hidden_div.contents)
                if inner_html:
                    parsed = BeautifulSoup(inner_html, "html.parser")
                    for element in parsed.contents:
                        new_div.append(element)
                # print("\n\nFALLBACK CODE EXAMPLE:\n", new_div)
            
            # Replace the code-example element with the new div
            code_example.replace_with(new_div)
    
    return content

def convert_to_ft(html_content):
    """Convert HTML content to FT components using html2ft."""
    try:
        # Import html2ft here - you'll need to install this package
        from fasthtml.components import html2ft
        
        # Convert the HTML to FT components
        ft_components = html2ft(str(html_content))
        return ft_components
    except ImportError:
        print("Error: html2ft module not found. Please install it.")
        sys.exit(1)
    except Exception as e:
        print(f"Error converting HTML to FT components: {e}")
        sys.exit(1)

def get_filename_from_url(url):
    """Extract the last parameter of the URL and convert it to snake_case."""
    path = urlparse(url).path
    last_part = path.rstrip('/').split('/')[-1]
    
    # Convert to snake_case
    snake_case = re.sub(r'[^a-zA-Z0-9_-]', '', last_part).replace('-', '_')
    
    return f"{snake_case}.py"

def create_python_file(ft_components, filename):
    """Create a Python file with the specified format."""
    os.makedirs('app/extracted', exist_ok=True)
    
    file_content = f"""from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *

component = {ft_components}
"""
    
    file_path = os.path.join('app/extracted', filename)
    with open(file_path, 'w') as f:
        f.write(file_content)
    
    return file_path

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_ft_components.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    print(f"Fetching HTML from {url}...")
    html_content = get_html_content(url)
    
    print("Extracting main content...")
    main_content = extract_main_content(html_content)
    
    print("Removing aside elements...")
    cleaned_content = remove_aside_elements(main_content)
    
    print("Processing code examples...")
    processed_content = process_code_examples(cleaned_content)
    
    print("Converting to FT components...")
    ft_components = convert_to_ft(processed_content)
    
    print("Creating Python file...")
    filename = get_filename_from_url(url)
    file_path = create_python_file(ft_components, filename)
    
    print(f"Done! FT components saved to {file_path}")

if __name__ == "__main__":
    main() 