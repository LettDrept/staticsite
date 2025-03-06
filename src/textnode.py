from enum import Enum               # Allows for use of Enum-type variables

class TextType(Enum):               # Establishes the standard types of text for this site
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode():
    def __init__(self, text, text_type, url=None):          # url defaults to None if nothing is passed in
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):                    # For comparing two TextNode objects
        return (                                # Returns True if all properties are alike
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return(f"TextNode({self.text}, {self.text_type.value}, {self.url})")