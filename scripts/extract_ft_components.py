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

def extract_and_mark_code_examples(content):
    """Extract code examples and replace them with placeholder markers.
    
    Returns modified content and a list of tuples with extracted code examples.
    """
    # Find all elements with class "code-example"
    code_examples = content.find_all(class_="code-example")
    extracted_examples = []
    
    for i, code_example in enumerate(code_examples):
        # Find the div with class="hidden" and data-clipboard-content-html attribute
        hidden_div = code_example.find('div', class_="hidden", attrs={"data-clipboard-content-html": True})
        
        if hidden_div:
            # Get the HTML content directly from the attribute
            html_content = hidden_div.get('data-clipboard-content-html')
            
            if not html_content:
                # Fallback: Try to get inner HTML directly
                inner_html = ''.join(str(c) for c in hidden_div.contents)
                html_content = inner_html
            
            # Create a placeholder with a unique ID
            placeholder = BeautifulSoup(f'<div id="code_example_placeholder_{i}"></div>', "html.parser").div
            
            # Replace the code example with the placeholder
            code_example.replace_with(placeholder)
            
            # Store the original HTML content
            extracted_examples.append((i, html_content))
    
    return content, extracted_examples

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

def inject_component_showcases(ft_output, extracted_examples):
    """Inject component_showcase elements into the FT output."""
    from fasthtml.components import html2ft
    
    result = ft_output
    
    for i, html_content in extracted_examples:
        try:
            # Convert the HTML content to an FT component
            component = html2ft(f"<div>{html_content}</div>")
            
            # Create the component_showcase call with keyword arguments
            showcase_call = f"component_showcase({component}, code=\"\"\"{component}\"\"\", id=\"example_{i}\",cls='mt-2 mb-6')"
            
            # Look for different possible patterns of the placeholder in FT output
            placeholder_patterns = [
                f'Div(id="code_example_placeholder_{i}")',
                f"Div(id='code_example_placeholder_{i}')",
                f'Div(id = "code_example_placeholder_{i}")',
                f"Div(id = 'code_example_placeholder_{i}')",
                f'Div(cls="", id="code_example_placeholder_{i}")',
                f"Div(cls='', id='code_example_placeholder_{i}')"
            ]
            
            # Try each pattern
            replaced = False
            for pattern in placeholder_patterns:
                if pattern in result:
                    result = result.replace(pattern, showcase_call)
                    print(f"Replaced placeholder {i} using pattern: {pattern}")
                    replaced = True
                    break
            
            # If no exact pattern matched, try a more flexible approach with regex
            if not replaced:
                print(f"Could not find exact placeholder for example {i}, trying regex...")
                # Use regex to find variations of the placeholder pattern
                placeholder_regex = re.compile(r'Div\(\s*(?:[^,]*,\s*)?id\s*=\s*[\'"]code_example_placeholder_{i}[\'"](?:,\s*[^)]*)?(?:,\s*)?\)'.format(i=i))
                if placeholder_regex.search(result):
                    result = placeholder_regex.sub(showcase_call, result)
                    print(f"Replaced placeholder {i} using regex")
                else:
                    print(f"WARNING: Could not find placeholder for example {i} in FT output")
                    # As a last resort, print a chunk of the FT output to help debug
                    print(f"FT output sample: {result[:200]}...")
        
        except Exception as e:
            print(f"Error injecting component showcase {i}: {e}")
    
    return result

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
from fastbite.components import *
from utils import component_showcase

component = {ft_components}
"""
    
    file_path = os.path.join('app/extracted', filename)
    with open(file_path, 'w') as f:
        f.write(file_content)
    
    return file_path

def replace_colors(ft_components):
    """Replace color names in the FT components."""
    # Replace all occurrences of 'blue' with 'primary'
    return ft_components.replace('blue', 'primary')

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
    
    print("Extracting and marking code examples...")
    content_with_placeholders, extracted_examples = extract_and_mark_code_examples(cleaned_content)
    
    print("Converting to FT components...")
    ft_components = convert_to_ft(content_with_placeholders)
    
    print("Injecting component showcases...")
    final_ft_components = inject_component_showcases(ft_components, extracted_examples)
    
    # Verify component_showcase calls are present in the output
    showcase_count = final_ft_components.count("component_showcase(")
    expected_count = len(extracted_examples)
    print(f"Verification: Found {showcase_count} component_showcase calls (expected {expected_count})")
    
    if showcase_count < expected_count:
        print("WARNING: Some component_showcase calls may not have been injected properly")
        placeholder_count = len(re.findall(r'Div\([^)]*id\s*=\s*[\'"]code_example_placeholder_\d+[\'"]', final_ft_components))
        if placeholder_count > 0:
            print(f"Found {placeholder_count} remaining placeholder divs in the output")
    
    print("Replacing color names (blue → primary)...")
    final_ft_components = replace_colors(final_ft_components)
    
    print("Creating Python file...")
    filename = get_filename_from_url(url)
    file_path = create_python_file(final_ft_components, filename)
    
    print(f"Done! FT components saved to {file_path}")

if __name__ == "__main__":
    main() 