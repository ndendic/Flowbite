from fasthtml.common import *
from fastbite.all import *
from utils import component_showcase

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
            code="""from fastbite.all import Table, Thead, TrHeader, Th, Tbody, Tr, Td

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
            code="""from fastbite.all import Table, Thead, TrHeader, Th, Tbody, Tr, Td

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
        
        Br(),
        
        H3("Table with Footer", link=True, cls="mb-3"),
        P("Tables can include a footer section using the ", Code("Tfoot"), " and ", Code("Tf"), " components:"),
        
        component_showcase(
            Table(
                Thead(
                    TrHeader(
                        Th("Item"),
                        Th("Quantity"),
                        Th("Price")
                    )
                ),
                Tbody(
                    Tr(
                        Td("Widget A"),
                        Td("5"),
                        Td("$10.00")
                    ),
                    Tr(
                        Td("Widget B"),
                        Td("3"),
                        Td("$8.00")
                    )
                ),
                Tfoot(
                    Tr(
                        Tf("Total"),
                        Tf("8"),
                        Tf("$18.00")
                    )
                )
            ),
            code="""from fastbite.all import Table, Thead, TrHeader, Th, Tbody, Tr, Td, Tfoot, Tf

Table(
    Thead(
        TrHeader(
            Th("Item"),
            Th("Quantity"),
            Th("Price")
        )
    ),
    Tbody(
        Tr(
            Td("Widget A"),
            Td("5"),
            Td("$10.00")
        ),
        Tr(
            Td("Widget B"),
            Td("3"),
            Td("$8.00")
        )
    ),
    Tfoot(
        Tr(
            Tf("Total"),  # Tf is used for footer cells
            Tf("8"),
            Tf("$18.00")
        )
    )
)""",
            id="table-with-footer"
        ),
        
        Br(),
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
                with_shadow=True
            ),
            code="""from fastbite.all import Table, Thead, TrHeader, Th, Tbody, Tr, Td

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
            code="""from fastbite.all import Table, Thead, TrHeader, Th, Tbody, Tr, Td

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
            code="""from fastbite.all import Table, Thead, TrHeader, Th, Tbody, Tr, Td, TableT

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
                headers=["Product", "Category", "Price"],
                rows=[
                    ["Apple MacBook Pro", "Laptop", "$1999"],
                    ["Microsoft Surface Pro", "Laptop", "$1299"],
                    ["Google Pixel 6", "Smartphone", "$599"]
                ]
            ),
            code="""from fastbite.all import DataTable

DataTable(
    headers=["Product", "Category", "Price"],
    rows=[
        ["Apple MacBook Pro", "Laptop", "$1999"],
        ["Microsoft Surface Pro", "Laptop", "$1299"],
        ["Google Pixel 6", "Smartphone", "$599"]
    ]
)""",
            id="basic-datatable"
        ),
        
        Br(),
        
        H3("DataTable with Footer", link=True, cls="mb-3"),
        P("Add a footer row to a DataTable:"),
        
        component_showcase(
            DataTable(
                headers=["Item", "Quantity", "Price"],
                rows=[
                    ["Widget A", "5", "$10.00"],
                    ["Widget B", "3", "$8.00"]
                ],
                footer=["Total", "8", "$18.00"],
                with_shadow=True
            ),
            code="""from fastbite.all import DataTable

DataTable(
    headers=["Item", "Quantity", "Price"],
    rows=[
        ["Widget A", "5", "$10.00"],
        ["Widget B", "3", "$8.00"]
    ],
    footer=["Total", "8", "$18.00"],  # Footer row data
    with_shadow=True
)""",
            id="datatable-with-footer"
        ),
        
        Br(),
        
        H3("Styled DataTable", link=True, cls="mb-3"),
        P("Apply various styling options to a DataTable:"),
        
        component_showcase(
            DataTable(
                headers=["Name", "Position", "Office", "Age", "Start Date", "Salary"],
                rows=[
                    ["Tiger Nixon", "System Architect", "Edinburgh", "61", "2011/04/25", "$320,800"],
                    ["Garrett Winters", "Accountant", "Tokyo", "63", "2011/07/25", "$170,750"],
                    ["Ashton Cox", "Junior Technical Author", "San Francisco", "66", "2009/01/12", "$86,000"],
                    ["Cedric Kelly", "Senior Javascript Developer", "Edinburgh", "22", "2012/03/29", "$433,060"]
                ],
                first_col_header=True,
                striped=True,
                hover=True,
                with_shadow=True
            ),
            code="""from fastbite.all import DataTable

DataTable(
    headers=["Name", "Position", "Office", "Age", "Start Date", "Salary"],
    rows=[
        ["Tiger Nixon", "System Architect", "Edinburgh", "61", "2011/04/25", "$320,800"],
        ["Garrett Winters", "Accountant", "Tokyo", "63", "2011/07/25", "$170,750"],
        ["Ashton Cox", "Junior Technical Author", "San Francisco", "66", "2009/01/12", "$86,000"],
        ["Cedric Kelly", "Senior Javascript Developer", "Edinburgh", "22", "2012/03/29", "$433,060"]
    ],
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
                headers=["Name", "Position", "Office", "Age", "Start Date", "Salary"],
                rows=[
                    ["Tiger Nixon", "System Architect", "Edinburgh", "61", "2011/04/25", "$320,800"],
                    ["Garrett Winters", "Accountant", "Tokyo", "63", "2011/07/25", "$170,750"],
                    ["Ashton Cox", "Junior Technical Author", "San Francisco", "66", "2009/01/12", "$86,000"],
                    ["Cedric Kelly", "Senior Javascript Developer", "Edinburgh", "22", "2012/03/29", "$433,060"],
                    ["Airi Satou", "Accountant", "Tokyo", "33", "2008/11/28", "$162,700"],
                    ["Brielle Williamson", "Integration Specialist", "New York", "61", "2012/12/02", "$372,000"]
                ],
                id="sortable-search-example",
                first_col_header=True,
                sortable=True,
                searchable=True,
                with_shadow=True
            ),
            code="""from fastbite.all import DataTable

DataTable(
    headers=["Name", "Position", "Office", "Age", "Start Date", "Salary"],
    rows=[
        ["Tiger Nixon", "System Architect", "Edinburgh", "61", "2011/04/25", "$320,800"],
        ["Garrett Winters", "Accountant", "Tokyo", "63", "2011/07/25", "$170,750"],
        ["Ashton Cox", "Junior Technical Author", "San Francisco", "66", "2009/01/12", "$86,000"],
        ["Cedric Kelly", "Senior Javascript Developer", "Edinburgh", "22", "2012/03/29", "$433,060"],
        ["Airi Satou", "Accountant", "Tokyo", "33", "2008/11/28", "$162,700"],
        ["Brielle Williamson", "Integration Specialist", "New York", "61", "2012/12/02", "$372,000"]
    ],
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
            SimpleTable(
                headers=["Product", "Category", "Price", "Stock"],
                rows=[
                    ["Apple MacBook Pro", "Laptop", "$1999", "In Stock"],
                    ["Microsoft Surface Pro", "Laptop", "$1299", "Limited"],
                    ["Google Pixel 6", "Smartphone", "$599", "Out of Stock"],
                    ["Samsung Galaxy S21", "Smartphone", "$799", "In Stock"]
                ]
            ),
            code="""from fastbite.all import SimpleTable

SimpleTable(
    headers=["Product", "Category", "Price", "Stock"],
    rows=[
        ["Apple MacBook Pro", "Laptop", "$1999", "In Stock"],
        ["Microsoft Surface Pro", "Laptop", "$1299", "Limited"],
        ["Google Pixel 6", "Smartphone", "$599", "Out of Stock"],
        ["Samsung Galaxy S21", "Smartphone", "$799", "In Stock"]
    ]
)

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
            SimpleTable(
                headers=["Project", "Status", "Deadline", "Progress"],
                rows=[
                    ["Website Redesign", "In Progress", "2023-06-30", "75%"],
                    ["Mobile App", "Planning", "2023-08-15", "20%"],
                    ["CRM Integration", "Completed", "2023-04-10", "100%"]
                ],
                sortable=True,
                searchable=True,
                id="project-tracker"
            ),
            code="""from fastbite.all import SimpleTable

SimpleTable(
    headers=["Project", "Status", "Deadline", "Progress"],
    rows=[
        ["Website Redesign", "In Progress", "2023-06-30", "75%"],
        ["Mobile App", "Planning", "2023-08-15", "20%"],
        ["CRM Integration", "Completed", "2023-04-10", "100%"]
    ],
    sortable=True,       # Enable sorting
    searchable=True,     # Enable searching
    id="project-tracker" # Required for interactive features
)""",
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
        _styled_table_section(),
        _datatable_section(),
        _simpletable_section(),
    )

# Make the showcase available to the app
tables_components = tables_showcase() 