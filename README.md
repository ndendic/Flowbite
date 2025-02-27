# Flowbite FastHTML Components

A collection of FastHTML components based on Flowbite's UI components.

## Project Structure

```
flowbite-fasthtml/
├── components/           # Core components
│   ├── common/          # Shared component utilities
│   ├── layout/          # Layout components (navbar, footer, etc.)
│   ├── elements/        # Basic UI elements (buttons, inputs, etc.)
│   ├── forms/           # Form-related components
│   ├── navigation/      # Navigation components
│   └── feedback/        # Alerts, modals, toasts etc.
├── utils/              # Utility functions and helpers
├── themes/             # Theme configurations
├── assets/            # Static assets (images, icons)
├── examples/          # Example implementations
└── docs/              # Documentation
```

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python main.py
```

## Usage

Import components from their respective modules:

```python
from components.elements.buttons import Button
from components.layout.navbar import Navbar

# Use components in your FastHTML app
@rt("/")
def home():
    return Container(
        Navbar(...),
        Button("Click me", variant="primary")
    )
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
