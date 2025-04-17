# Card Component Implementation Guide

This document provides a detailed guide for implementing the Card component from Flowbite in FastHTML.

## Card Component in Flowbite

Flowbite offers several card variants:
- Default card
- Card with image
- Horizontal card
- Card with dismiss button
- Card with action buttons
- Interactive cards

## Implementation Approach

### 1. Create Card Type Enumeration

First, we need to define a `CardT` enumeration to capture the various card styles available in Flowbite:

```python
class CardT(VEnum):
    """Card utility types for Flowbite components"""
    def _generate_next_value_(name, start, count, last_values): 
        return str2cls('card', name)
    
    # Card types
    default = "block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700"
    horizontal = "flex flex-col items-center bg-white border rounded-lg shadow md:flex-row md:max-w-xl dark:border-gray-700 dark:bg-gray-800"
    
    # Card with CTA (Call to Action)
    cta = "max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
    
    # Card with image
    image = "max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
    
    # Card with list
    list = "max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
    
    # Card sizes (can be combined with types)
    sm = "p-4"
    md = "p-6"
    lg = "p-8"
```

### 2. Create Card Components

Next, we'll create the component functions for different parts of a card:

```python
def CardHeader(*c, 
               cls=(), 
               **kwargs) -> FT:
    """Card header component for Flowbite card"""
    return Div(*c, cls=stringify(('mb-2', cls)), **kwargs)

def CardTitle(*c, 
              cls=stringify((TextT.text_2xl, TextT.bold)), 
              **kwargs) -> FT:
    """Card title component for Flowbite card"""
    return H5(*c, cls=stringify((cls)), **kwargs)

def CardText(*c, 
             cls=stringify((TextT.normal, TextT.gray)), 
             **kwargs) -> FT:
    """Card text/body component for Flowbite card"""
    return P(*c, cls=stringify((cls)), **kwargs)

def CardFooter(*c, 
               cls=(), 
               **kwargs) -> FT:
    """Card footer component for Flowbite card"""
    return Div(*c, cls=stringify(('mt-4', cls)), **kwargs)
```

### 3. Create Main Card Component

Now, we'll create the main Card component that combines all the parts:

```python
def Card(*c, 
         cls=CardT.default, 
         header=None,
         title=None,
         footer=None,
         img_src=None,
         img_alt="",
         img_position="top",  # "top" or "left" for horizontal card
         **kwargs) -> FT:
    """
    Create a Flowbite card component
    
    Parameters:
    -----------
    c : Content for the card body
    cls : CSS classes for the card
    header : Optional header content
    title : Optional title content
    footer : Optional footer content
    img_src : Optional image source
    img_alt : Image alt text
    img_position : Image position - "top" (default) or "left" (for horizontal card)
    """
    card_content = []
    
    # Add image if provided
    if img_src:
        if img_position == "left":
            # For horizontal card with left image
            cls = stringify((CardT.horizontal, cls)) if CardT.horizontal not in cls else cls
            img = Img(src=img_src, alt=img_alt, cls="object-cover w-full h-96 rounded-t-lg md:h-auto md:w-48 md:rounded-none md:rounded-l-lg")
            card_content.append(img)
        else:
            # For card with top image
            cls = stringify((CardT.image, cls)) if CardT.image not in cls else cls
            img = Img(src=img_src, alt=img_alt, cls="rounded-t-lg")
            card_content.append(img)
    
    # Create content container
    content_container = []
    
    # Add header if provided
    if header:
        if isinstance(header, (list, tuple)):
            content_container.append(CardHeader(*header))
        else:
            content_container.append(CardHeader(header))
    
    # Add title if provided
    if title:
        content_container.append(CardTitle(title))
    
    # Add main content
    content_container.extend(c)
    
    # Add footer if provided
    if footer:
        if isinstance(footer, (list, tuple)):
            content_container.append(CardFooter(*footer))
        else:
            content_container.append(CardFooter(footer))
    
    # For horizontal card or card with top image, wrap content in a div
    if img_src and img_position == "left":
        card_content.append(Div(*content_container, cls="flex flex-col justify-between p-4 leading-normal"))
    else:
        # Regular card, add content directly or in a div if it has an image
        if img_src:
            card_content.append(Div(*content_container, cls="p-5"))
        else:
            card_content.extend(content_container)
    
    # Return the final card
    return Div(*card_content, cls=stringify((cls)), **kwargs)
```

## Example Usage

```python
# Basic card with title and text
basic_card = Card(
    title="Basic Card",
    CardText("This is a basic card component from Flowbite.")
)

# Card with image
image_card = Card(
    title="Card with Image",
    CardText("This card includes an image above the content."),
    img_src="https://flowbite.com/docs/images/blog/image-1.jpg",
    img_alt="Card image"
)

# Horizontal card with image on the left
horizontal_card = Card(
    title="Horizontal Card",
    CardText("This card uses a horizontal layout with the image on the left."),
    img_src="https://flowbite.com/docs/images/blog/image-4.jpg",
    img_alt="Card image",
    img_position="left"
)

# Card with footer actions
action_card = Card(
    title="Card with Actions",
    CardText("This card has action buttons in the footer."),
    footer=[
        Button("Read more", cls=ButtonT.default),
        Button("Save", cls=ButtonT.alternative, cls_add="ml-2")
    ]
)
```

## Additional Variations

### Interactive Card

To create an interactive card with hover effects and a link:

```python
def InteractiveCard(*c,
                    href="#",
                    cls=CardT.default,
                    **kwargs) -> FT:
    """
    Create an interactive card that acts as a link
    """
    # Add hover effects to the card
    hover_cls = "cursor-pointer transition-transform duration-200 hover:-translate-y-1"
    
    return A(
        href=href,
        cls=stringify((hover_cls)),
        **kwargs
    )(
        Card(*c, cls=cls)
    )
```

### Dismissible Card

For a card with a dismiss button:

```python
def DismissibleCard(*c,
                   cls=CardT.default,
                   dismiss_id=None,
                   **kwargs) -> FT:
    """
    Create a card with a dismiss button
    """
    dismiss_button = Button(
        UkIcon("x", width=16, height=16),
        cls="absolute top-3 right-3 ml-auto inline-flex items-center p-1 text-sm text-gray-400 bg-transparent rounded-sm hover:bg-gray-200 hover:text-gray-900 dark:hover:bg-gray-600 dark:hover:text-white",
        **{"data-dismiss-target": f"#{dismiss_id}" if dismiss_id else None}
    )
    
    return Div(
        Card(*c, cls=cls, **kwargs),
        dismiss_button,
        cls="relative",
        id=dismiss_id
    )
```

## Integration with JavaScript

For interactive cards that require JavaScript (like dismissible cards), ensure the Flowbite JavaScript is properly initialized:

```python
def get_flowbite_init_js():
    """Return the JavaScript needed to initialize Flowbite components"""
    return """
    <script>
        // Initialize the Flowbite library components
        document.addEventListener('DOMContentLoaded', function() {
            if (typeof flowbite !== 'undefined') {
                flowbite.initDismisses();
            }
        });
    </script>
    """
``` 