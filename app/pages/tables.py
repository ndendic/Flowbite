from fasthtml.common import *
from fastbite.all import *
from utils import component_showcase

headers = ['Product name', 'Color', 'Category', 'Price']
rows = [
    ['Apple MacBook Pro 17"', 'Silver', 'Laptop', '$2999'],
    ['Microsoft Surface Pro', 'White', 'Laptop PC', '$1999'],
    ['Magic Mouse 2', 'Black', 'Accessories', '$99'],
    ['Dell XPS 13', 'Silver', 'Laptop', '$1499'],
    ['HP Spectre x360', 'Black', 'Laptop', '$1599'],
    ['Logitech MX Master 3', 'Gray', 'Accessories', '$99'],
    ['Samsung Galaxy S21', 'Phantom Gray', 'Smartphone', '$799'],
    ['Sony WH-1000XM4', 'Black', 'Headphones', '$349'],
    ['Google Pixel 5', 'Just Black', 'Smartphone', '$699'],
    ['Amazon Echo Dot', 'Charcoal', 'Smart Home', '$49'],
    ['Apple iPad Pro', 'Space Gray', 'Tablet', '$999'],
    ['Asus ROG Strix', 'Black', 'Gaming Laptop', '$1999'],
    ['Bose QuietComfort 35', 'Silver', 'Headphones', '$299'],
    ['Apple iPhone 12', 'Black', 'Smartphone', '$799'],
    ['Sony A7 III', 'Black', 'Mirrorless Camera', '$1499'],
    ['Canon EOS R6', 'White', 'Mirrorless Camera', '$1999'],
    ['DJI Mavic Air 2', 'Silver', 'Drone', '$799'],
    ['DJI Mavic 3', 'Black', 'Drone', '$1299'],
    ['Panasonic Lumix G9', 'Black', 'Mirrorless Camera', '$1499'],
    ['DJI Osmo Action', 'Black', 'Action Camera', '$299'],
    ['DJI Osmo Pocket', 'White', 'Action Camera', '$399'],
    ['DJI Osmo Mobile 3', 'Black', 'Gimbal', '$199'],
]

def _basic_table_section():
    return Section(
        H2("Basic Tables", link=True, cls="mb-4 mt-10"),
        P("The basic table components provide a styled way to create tables using the Flowbite design system."),
        
        H3("Simple Table Structure", link=True, cls="mb-3"),
        P("Creating a table with basic structure using the ", Code("Table"), ", ", Code("Thead"), ", ", Code("Tbody"), ", ", Code("Tr"), ", ", Code("Th"), ", and ", Code("Td"), " components:"),
        
        component_showcase(
            Table(
                Thead(
                    TrHeader(
                        Th("Product"),
                        Th("Category"),
                        Th("Price"),
                        Th("Actions")
                    )
                ),
                Tbody(
                    Tr(
                        Td("Apple MacBook Pro"),
                        Td("Laptop"),
                        Td("$1999"),
                        Td("View details")
                    ),
                    Tr(
                        Td("Microsoft Surface Pro"),
                        Td("Laptop"),
                        Td("$1299"),
                        Td("View details")
                    ),
                    Tr(
                        Td("Google Pixel 6"),
                        Td("Smartphone"),
                        Td("$599"),
                        Td("View details")
                    )
                )
            ),
            code="""from fastbite.all import *

Table(
    Thead(
        TrHeader(
            Th("Product"),
            Th("Category"),
            Th("Price"),
            Th("Actions")
        )
    ),
    Tbody(
        Tr(
            Td("Apple MacBook Pro"),
            Td("Laptop"),
            Td("$1999"),
            Td("View details")
        ),
        Tr(
            Td("Microsoft Surface Pro"),
            Td("Laptop"),
            Td("$1299"),
            Td("View details")
        ),
        Tr(
            Td("Google Pixel 6"),
            Td("Smartphone"),
            Td("$599"),
            Td("View details")
        )
    )
)""",
            id="basic-table"
        ),
        
        Br(),
        
        H3("Table with Shadow", link=True, cls="mb-3"),
        P("Add a shadow effect to a table using the ", Code("with_shadow"), " parameter:"),
        
        component_showcase(
            Table(
                Thead(
                    TrHeader(
                        Th("Product"),
                        Th("Price")
                    )
                ),
                Tbody(
                    Tr(
                        Td("Apple MacBook Pro"),
                        Td("$1999")
                    ),
                    Tr(
                        Td("Google Pixel 6"),
                        Td("$599")
                    )
                ),
                with_shadow=True
            ),
            code="""from fastbite.all import *

Table(
    Thead(
        TrHeader(
            Th("Product"),
            Th("Price")
        )
    ),
    Tbody(
        Tr(
            Td("Apple MacBook Pro"),
            Td("$1999")
        ),
        Tr(
            Td("Google Pixel 6"),
            Td("$599")
        )
    ),
    with_shadow=True  # Adds shadow styling to the table
)""",
            id="table-with-shadow"
        ),
                    
    )

def _styled_table_section():
    return Section(
        H2("Styled Tables", link=True, cls="mb-4 mt-10"),
        P("Flowbite tables can be customized with different styling options."),
        
        H3("Striped Rows", link=True, cls="mb-3"),
        P("Apply alternating row colors using the ", Code("striped"), " parameter:"),
        
        component_showcase(
            Table(
                Thead(
                    TrHeader(
                        Th("Name"),
                        Th("Position"),
                        Th("Office")
                    )
                ),
                Tbody(
                    Tr(
                        Td("John Smith"),
                        Td("Developer"),
                        Td("New York")
                    ),
                    Tr(
                        Td("Jane Doe"),
                        Td("Designer"),
                        Td("London")
                    ),
                    Tr(
                        Td("Mike Johnson"),
                        Td("Manager"),
                        Td("Tokyo")
                    ),
                    Tr(
                        Td("Sarah Williams"),
                        Td("Marketing"),
                        Td("Berlin")
                    )
                ),
                cls=TableT.row_striped,
                with_shadow=True
            ),
            code="""from fastbite.all import *

Table(
    Thead(
        TrHeader(
            Th("Name"),
            Th("Position"),
            Th("Office")
        )
    ),
    Tbody(
        Tr(
            Td("John Smith"),
            Td("Developer"),
            Td("New York")
        ),
        Tr(
            Td("Jane Doe"),
            Td("Designer"),
            Td("London")
        ),
        Tr(
            Td("Mike Johnson"),
            Td("Manager"),
            Td("Tokyo")
        ),
        Tr(
            Td("Sarah Williams"),
            Td("Marketing"),
            Td("Berlin")
        )
    ),
    with_shadow=True
)""",
            id="striped-table"
        ),
        
        Br(),
        
        H3("Hover Effect", link=True, cls="mb-3"),
        P("Add hover effect to rows using the ", Code("hover"), " parameter:"),
        
        component_showcase(
            Table(
                Thead(
                    TrHeader(
                        Th("Name"),
                        Th("Email"),
                        Th("Status")
                    )
                ),
                Tbody(
                    hover=True,
                    children=[
                        Tr(
                            Td("John Smith"),
                            Td("john@example.com"),
                            Td("Active")
                        ),
                        Tr(
                            Td("Jane Doe"),
                            Td("jane@example.com"),
                            Td("Inactive")
                        ),
                        Tr(
                            Td("Mike Johnson"),
                            Td("mike@example.com"),
                            Td("Pending")
                        )
                    ]
                )
            ),
            code="""from fastbite.all import *

Table(
    Thead(
        TrHeader(
            Th("Name"),
            Th("Email"),
            Th("Status")
        )
    ),
    Tbody(
        hover=True,  # Adds hover effect to rows
        children=[
            Tr(
                Td("John Smith"),
                Td("john@example.com"),
                Td("Active")
            ),
            Tr(
                Td("Jane Doe"),
                Td("jane@example.com"),
                Td("Inactive")
            ),
            Tr(
                Td("Mike Johnson"),
                Td("mike@example.com"),
                Td("Pending")
            )
        ]
    )
)""",
            id="hover-table"
        ),
        
        Br(),
        
        H3("First Column as Header", link=True, cls="mb-3"),
        P("Style the first column of each row as a header:"),
        
        component_showcase(
            Table(
                Thead(
                    TrHeader(
                        Th("Employee"),
                        Th("Department"),
                        Th("Salary")
                    )
                ),
                Tbody(
                    [
                        Tr(
                            Th("John Smith", scope="row", cls=TableT.cell_first),
                            Td("Engineering"),
                            Td("$120,000")
                        ),
                        Tr(
                            Th("Jane Doe", scope="row", cls=TableT.cell_first),
                            Td("Design"),
                            Td("$95,000")
                        ),
                        Tr(
                            Th("Mike Johnson", scope="row", cls=TableT.cell_first),
                            Td("Management"),
                            Td("$150,000")
                        )
                    ]
                )
            ),
            code="""from fastbite.all import *

Table(
    Thead(
        TrHeader(
            Th("Employee"),
            Th("Department"),
            Th("Salary")
        )
    ),
    Tbody(
        [
            Tr(
                Th("John Smith", scope="row", cls=TableT.cell_first),  # First column as header
                Td("Engineering"),
                Td("$120,000")
            ),
            Tr(
                Th("Jane Doe", scope="row", cls=TableT.cell_first),  # First column as header
                Td("Design"),
                Td("$95,000")
            ),
            Tr(
                Th("Mike Johnson", scope="row", cls=TableT.cell_first),  # First column as header
                Td("Management"),
                Td("$150,000")
            )
        ]
    )
)""",
            id="first-col-header-table"
        ),
        
        Br(),
    )

def _datatable_section():

    return Section(
        H2("DataTable Component", link=True, cls="mb-4 mt-10"),
        P("The ", Code("DataTable"), " component provides a convenient way to create tables from data arrays."),
        
        H3("Basic DataTable", link=True, cls="mb-3"),
        P("Create a table from headers and rows data:"),
        
        component_showcase(
            DataTable(
                headers=headers,
                rows=rows[:5]
            ),
            code="""from fastbite.all import *

headers = ['Product name', 'Color', 'Category', 'Price']
rows = [
    ['Apple MacBook Pro 17"', 'Silver', 'Laptop', '$2999'],
    ['Microsoft Surface Pro', 'White', 'Laptop PC', '$1999'],
    ['Magic Mouse 2', 'Black', 'Accessories', '$99'],
    ['Dell XPS 13', 'Silver', 'Laptop', '$1499'],
    ['HP Spectre x360', 'Black', 'Laptop', '$1599'],
    ['Logitech MX Master 3', 'Gray', 'Accessories', '$99'],
    ['Samsung Galaxy S21', 'Phantom Gray', 'Smartphone', '$799'],
    ['Sony WH-1000XM4', 'Black', 'Headphones', '$349'],
    ['Google Pixel 5', 'Just Black', 'Smartphone', '$699'],
    ['Amazon Echo Dot', 'Charcoal', 'Smart Home', '$49'],
    ['Apple iPad Pro', 'Space Gray', 'Tablet', '$999'],
    ['Asus ROG Strix', 'Black', 'Gaming Laptop', '$1999'],
    ['Bose QuietComfort 35', 'Silver', 'Headphones', '$299'],
    ['Apple iPhone 12', 'Black', 'Smartphone', '$799'],
    ['Sony A7 III', 'Black', 'Mirrorless Camera', '$1499'],
    ['Canon EOS R6', 'White', 'Mirrorless Camera', '$1999'],
    ['DJI Mavic Air 2', 'Silver', 'Drone', '$799'],
    ['DJI Mavic 3', 'Black', 'Drone', '$1299'],
    ['Panasonic Lumix G9', 'Black', 'Mirrorless Camera', '$1499'],
    ['DJI Osmo Action', 'Black', 'Action Camera', '$299'],
    ['DJI Osmo Pocket', 'White', 'Action Camera', '$399'],
    ['DJI Osmo Mobile 3', 'Black', 'Gimbal', '$199'],
]

DataTable(headers=headers,rows=rows[:5])""",
            id="basic-datatable"
        ),
        
        Br(),
                
        
        H3("Styled DataTable", link=True, cls="mb-3"),
        P("Apply various styling options to a DataTable:"),
        
        component_showcase(
            DataTable(
                headers=headers,
                rows=rows[:5],
                first_col_header=True,
                striped=True,
                hover=True,
                with_shadow=True
            ),
            code="""from fastbite.all import *

headers = ['Product name', 'Color', 'Category', 'Price']
rows = [
    ['Apple MacBook Pro 17"', 'Silver', 'Laptop', '$2999'],
    ['Microsoft Surface Pro', 'White', 'Laptop PC', '$1999'],
    ['Magic Mouse 2', 'Black', 'Accessories', '$99'],
    ['Dell XPS 13', 'Silver', 'Laptop', '$1499'],
    ['HP Spectre x360', 'Black', 'Laptop', '$1599'],
    ['Logitech MX Master 3', 'Gray', 'Accessories', '$99'],
    ['Samsung Galaxy S21', 'Phantom Gray', 'Smartphone', '$799'],
    ['Sony WH-1000XM4', 'Black', 'Headphones', '$349'],
    ['Google Pixel 5', 'Just Black', 'Smartphone', '$699'],
    ['Amazon Echo Dot', 'Charcoal', 'Smart Home', '$49'],
    ['Apple iPad Pro', 'Space Gray', 'Tablet', '$999'],
    ['Asus ROG Strix', 'Black', 'Gaming Laptop', '$1999'],
    ['Bose QuietComfort 35', 'Silver', 'Headphones', '$299'],
    ['Apple iPhone 12', 'Black', 'Smartphone', '$799'],
    ['Sony A7 III', 'Black', 'Mirrorless Camera', '$1499'],
    ['Canon EOS R6', 'White', 'Mirrorless Camera', '$1999'],
    ['DJI Mavic Air 2', 'Silver', 'Drone', '$799'],
    ['DJI Mavic 3', 'Black', 'Drone', '$1299'],
    ['Panasonic Lumix G9', 'Black', 'Mirrorless Camera', '$1499'],
    ['DJI Osmo Action', 'Black', 'Action Camera', '$299'],
    ['DJI Osmo Pocket', 'White', 'Action Camera', '$399'],
    ['DJI Osmo Mobile 3', 'Black', 'Gimbal', '$199'],
]

DataTable(
    headers=headers,
    rows=rows[:5],    
    first_col_header=True,  # Style first column as header
    striped=True,           # Apply striped styling
    hover=True,             # Apply hover effect
    with_shadow=True        # Add shadow to table
)""",
            id="styled-datatable"
        ),
        
        Br(),
        
        H3("Sortable and Searchable DataTable", link=True, cls="mb-3"),
        P("Create an interactive table with sorting and searching capabilities:"),
        
        component_showcase(
            DataTable(
                headers=headers,
                rows=rows,
                id="sortable-search-example",
                first_col_header=True,
                sortable=True,
                searchable=True,
                with_shadow=True
            ),
            code="""from fastbite.all import *

headers = ['Product name', 'Color', 'Category', 'Price']
rows = [
    ['Apple MacBook Pro 17"', 'Silver', 'Laptop', '$2999'],
    ['Microsoft Surface Pro', 'White', 'Laptop PC', '$1999'],
    ['Magic Mouse 2', 'Black', 'Accessories', '$99'],
    ['Dell XPS 13', 'Silver', 'Laptop', '$1499'],
    ['HP Spectre x360', 'Black', 'Laptop', '$1599'],
    ['Logitech MX Master 3', 'Gray', 'Accessories', '$99'],
    ['Samsung Galaxy S21', 'Phantom Gray', 'Smartphone', '$799'],
    ['Sony WH-1000XM4', 'Black', 'Headphones', '$349'],
    ['Google Pixel 5', 'Just Black', 'Smartphone', '$699'],
    ['Amazon Echo Dot', 'Charcoal', 'Smart Home', '$49'],
    ['Apple iPad Pro', 'Space Gray', 'Tablet', '$999'],
    ['Asus ROG Strix', 'Black', 'Gaming Laptop', '$1999'],
    ['Bose QuietComfort 35', 'Silver', 'Headphones', '$299'],
    ['Apple iPhone 12', 'Black', 'Smartphone', '$799'],
    ['Sony A7 III', 'Black', 'Mirrorless Camera', '$1499'],
    ['Canon EOS R6', 'White', 'Mirrorless Camera', '$1999'],
    ['DJI Mavic Air 2', 'Silver', 'Drone', '$799'],
    ['DJI Mavic 3', 'Black', 'Drone', '$1299'],
    ['Panasonic Lumix G9', 'Black', 'Mirrorless Camera', '$1499'],
    ['DJI Osmo Action', 'Black', 'Action Camera', '$299'],
    ['DJI Osmo Pocket', 'White', 'Action Camera', '$399'],
    ['DJI Osmo Mobile 3', 'Black', 'Gimbal', '$199'],
]

DataTable(
    headers=headers,
    rows=rows,
    id="sortable-search-example",  # Required for interactive features
    first_col_header=True,
    sortable=True,                 # Enable sorting
    searchable=True,               # Enable searching
    with_shadow=True
)""",
            id="interactive-datatable"
        ),
        
        Br(),
    )

def _simpletable_section():
    return Section(
        H2("SimpleTable Component", link=True, cls="mb-4 mt-10"),
        P("The ", Code("SimpleTable"), " is a convenience function that creates a ", Code("DataTable"), " with predefined styling."),
        
        H3("SimpleTable Example", link=True, cls="mb-3"),
        P("Create a table with hover effect, striped rows, shadow, and first column header:"),
        
        component_showcase(
            SimpleTable(headers=headers,rows=rows),
            code="""from fastbite.all import *

headers = ['Product name', 'Color', 'Category', 'Price']
rows = [
    ['Apple MacBook Pro 17"', 'Silver', 'Laptop', '$2999'],
    ['Microsoft Surface Pro', 'White', 'Laptop PC', '$1999'],
    ['Magic Mouse 2', 'Black', 'Accessories', '$99'],
    ['Dell XPS 13', 'Silver', 'Laptop', '$1499'],
    ['HP Spectre x360', 'Black', 'Laptop', '$1599'],
    ['Logitech MX Master 3', 'Gray', 'Accessories', '$99'],
    ['Samsung Galaxy S21', 'Phantom Gray', 'Smartphone', '$799'],
    ['Sony WH-1000XM4', 'Black', 'Headphones', '$349'],
    ['Google Pixel 5', 'Just Black', 'Smartphone', '$699'],
    ['Amazon Echo Dot', 'Charcoal', 'Smart Home', '$49'],
    ['Apple iPad Pro', 'Space Gray', 'Tablet', '$999'],
    ['Asus ROG Strix', 'Black', 'Gaming Laptop', '$1999'],
    ['Bose QuietComfort 35', 'Silver', 'Headphones', '$299'],
    ['Apple iPhone 12', 'Black', 'Smartphone', '$799'],
    ['Sony A7 III', 'Black', 'Mirrorless Camera', '$1499'],
    ['Canon EOS R6', 'White', 'Mirrorless Camera', '$1999'],
    ['DJI Mavic Air 2', 'Silver', 'Drone', '$799'],
    ['DJI Mavic 3', 'Black', 'Drone', '$1299'],
    ['Panasonic Lumix G9', 'Black', 'Mirrorless Camera', '$1499'],
    ['DJI Osmo Action', 'Black', 'Action Camera', '$299'],
    ['DJI Osmo Pocket', 'White', 'Action Camera', '$399'],
    ['DJI Osmo Mobile 3', 'Black', 'Gimbal', '$199'],
]

SimpleTable(headers=headers,rows=rows),

# SimpleTable is a convenience function that applies:
# - with_shadow=True
# - first_col_header=True
# and other styling defaults
""",
            id="simple-table"
        ),
        
        Br(),
        
        H3("SimpleTable with Additional Options", link=True, cls="mb-3"),
        P("SimpleTable with additional customization:"),
        
        component_showcase(
            SimpleTable(headers=headers,rows=rows,sortable=True,searchable=True,id="project-tracker"),            
            code="""from fastbite.all import *

headers = ['Product name', 'Color', 'Category', 'Price']
rows = [
    ['Apple MacBook Pro 17"', 'Silver', 'Laptop', '$2999'],
    ['Microsoft Surface Pro', 'White', 'Laptop PC', '$1999'],
    ['Magic Mouse 2', 'Black', 'Accessories', '$99'],
    ['Dell XPS 13', 'Silver', 'Laptop', '$1499'],
    ['HP Spectre x360', 'Black', 'Laptop', '$1599'],
    ['Logitech MX Master 3', 'Gray', 'Accessories', '$99'],
    ['Samsung Galaxy S21', 'Phantom Gray', 'Smartphone', '$799'],
    ['Sony WH-1000XM4', 'Black', 'Headphones', '$349'],
    ['Google Pixel 5', 'Just Black', 'Smartphone', '$699'],
    ['Amazon Echo Dot', 'Charcoal', 'Smart Home', '$49'],
    ['Apple iPad Pro', 'Space Gray', 'Tablet', '$999'],
    ['Asus ROG Strix', 'Black', 'Gaming Laptop', '$1999'],
    ['Bose QuietComfort 35', 'Silver', 'Headphones', '$299'],
    ['Apple iPhone 12', 'Black', 'Smartphone', '$799'],
    ['Sony A7 III', 'Black', 'Mirrorless Camera', '$1499'],
    ['Canon EOS R6', 'White', 'Mirrorless Camera', '$1999'],
    ['DJI Mavic Air 2', 'Silver', 'Drone', '$799'],
    ['DJI Mavic 3', 'Black', 'Drone', '$1299'],
    ['Panasonic Lumix G9', 'Black', 'Mirrorless Camera', '$1499'],
    ['DJI Osmo Action', 'Black', 'Action Camera', '$299'],
    ['DJI Osmo Pocket', 'White', 'Action Camera', '$399'],
    ['DJI Osmo Mobile 3', 'Black', 'Gimbal', '$199'],
]

SimpleTable(headers=headers,rows=rows)
""",
            id="simple-table-options"
        ),
        
        Br(),
    )

def tables_showcase():
    """Page showcasing table components"""
    return Container(
        H1("Table Components", link=True, cls="mb-8 mt-6"),
        P(
            "Fastbite provides table components styled with Tailwind CSS following the Flowbite design system. These components make it easy to create responsive, well-styled tables.",
            cls="mb-6 text-lg"
        ),
        
        # Call section functions
        _basic_table_section(),
        # _styled_table_section(),
        _datatable_section(),
        _simpletable_section(),
    )

# Make the showcase available to the app
tables_components = tables_showcase() 