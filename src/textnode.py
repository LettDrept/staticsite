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
    
    def text_node_to_html_node(self):
        if self.text_type not in TextType:
            raise Exception("Text type is not a valid type")
        if self.text_type == "text":
                node = LeafNode(None, self.text)
                return node
     #       case BOLD:
      #          node = LeafNode("b", text_node.text)
       #         return node
        #    case ITALIC:
         #       node = LeafNode("i", text_node.text)
          #      return node
           # case CODE:
            #    node = LeafNode("code", text_node.text)
             #   return node
      #      case LINK:
       #         node = LeafNode("a", text_node.text, {"href": text_node.url})
        #        return node
         #   case IMAGE:
          #      node = LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
           #     return node