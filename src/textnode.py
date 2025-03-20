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


def text_node_to_html_node(text_node):          # Converts a single TextNode to an HTMLNode(LeafNode)
    if text_node.text_type not in TextType:
        raise Exception("Text type is not a valid type")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})


def split_nodes_delimiter(old_nodes, delimiter, text_type):     # Converts raw markdown to a list of TextNode(s)
    if delimiter != "**" and delimiter != "_" and delimiter != "`":
        raise Exception("invalid Markdown syntax")
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue                                # Means to go to next iterable in old_nodes
        
        temp_nodes = []
        temp_list = node.text.split(delimiter)
        if len(temp_list) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")  # Means with simple 1-markdown there should be an odd number
        
        for i in range(len(temp_list)):
            if temp_list[i] == "":
                continue
            if i % 2 == 0:
                temp_nodes.append(TextNode(temp_list[i], TextType.TEXT))
            else:
                temp_nodes.append(TextNode(temp_list[i], text_type))
        new_nodes.extend(temp_nodes)       
    
    return new_nodes