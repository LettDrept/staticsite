from enum import Enum               # Allows for use of Enum-type variables
from htmlnode import HTMLNode, LeafNode

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


def text_node_to_html_node(text_node):          # Converts a single TextNode to an HTMLNode
    if text_node.text_type not in TextType:
        raise ValueError("Text type is not a valid type")
    if text_node.text_type == TextType.TEXT:
        return HTMLNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return HTMLNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return HTMLNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return HTMLNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return HTMLNode("a", text_node.text, None, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return HTMLNode("img", "", None, {"src": text_node.url, "alt": text_node.text})

