import textwrap                     # Allows for use of textwrap.dedent
import re                           # Allows for use of regex
from enum import Enum               # Allows for use of Enum-type variables
from htmlnode import HTMLNode, ParentNode       # Imports the HTMLNode class from htmlnode.py
from markdowns import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):               # Establishes the standard types of blocks for this site
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"    
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

# Function for block-level markdowns
def markdown_to_blocks(markdown):
    lines = textwrap.dedent(markdown)   
    blocks = lines.split("\n\n")
    current_block = []
    for block in blocks:
        if block.strip() == "":
            continue
        is_code_block = block.lstrip().startswith("```")    # Check if the block is a code block to preserve newlines
        if is_code_block:
            processed_block = block.strip(" ")            # Remove leading and trailing spaces
            if not processed_block.endswith("```"):         # Check if the block ends with "```"
                processed_block = processed_block + "\n```"         
        else:
            processed_block = block.strip("\n ")        # Remove leading and trailing spaces
        current_block.append(processed_block)
    return current_block

# Function to change blocks to BlockType
def block_to_blocktype(block):
    if not isinstance(block, str):
        raise TypeError("block must be a string")    
    if bool(re.match(r"^#{1,6} .+", block)):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    else:   
        lines = block.split("\n")
        if all(line.startswith('>') for line in lines):
            return BlockType.QUOTE
        elif all(line.startswith("- ") for line in lines):
            return BlockType.UNORDERED_LIST
        else:
            line_number = 1
            for line in lines:
                if not line.startswith(f"{line_number}. "):
                    return BlockType.PARAGRAPH
                line_number += 1
            return BlockType.ORDERED_LIST    

# Function to change markdown to a ParentNode with HTMLNode children
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)   
        children.append(html_node)
    return ParentNode("div", children, None)

# Functions to ID block type and convert to HTMLNode
def block_to_html_node(block):
    block_type = block_to_blocktype(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    raise ValueError(f"Unknown block type: {block_type}")

def heading_to_html_node(block):
    heading_level = block.count("#")
    tag = f"h{heading_level}"
    content = block[heading_level:].strip()
    return HTMLNode(tag, content)

def code_to_html_node(block):
    content = block[3:-3].strip()
    inner_code = HTMLNode("code", content)
    return HTMLNode("pre", None, [inner_code])

def quote_to_html_node(block):
    lines = block.split("\n")
    the_quote = ""
    for i, line in enumerate(lines):
        content = line[1:].strip()
        if i < len(lines) - 1:
            content += "\n"
        the_quote += content
    return HTMLNode("blockquote", the_quote)

def unordered_list_to_html_node(block):
    items = [item[2:].strip() for item in block.split("\n") if item]
    children = [HTMLNode("li", item) for item in items]
    return HTMLNode("ul", None, children)

def ordered_list_to_html_node(block):
    items = block.split("\n")
    content = []
    for item in items:
        match = re.search(r"\d+\.\s", item)
        if match:
            content.append(item[match.end():].strip())
        else:
            raise ValueError("Invalid ordered list item format")
    children = [HTMLNode("li", item) for item in content]
    return HTMLNode("ol", None, children)

def paragraph_to_html_node(block):
    content = block.strip("\n")
    paragraph = content.replace("\n", " ")
    children = text_to_children(paragraph)
    return HTMLNode("p", None, children)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children