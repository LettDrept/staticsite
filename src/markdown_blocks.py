import textwrap                     # Allows for use of textwrap.dedent
import re                           # Allows for use of regex
from enum import Enum               # Allows for use of Enum-type variables


class BlockType(Enum):               # Establishes the standard types of blocks for this site
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

# Function for block-level markdowns

def markdown_to_blocks(markdown):
    lines = textwrap.dedent(markdown)   
    blocks = lines.split("\n\n")
    current_block = []
    for block in blocks:
        block = block.strip("\n ")
        if block == "":
            continue
        else:
            current_block.append(block)
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
    return BlockType.PARAGRAPH

# Function to change markdown to HTML

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)


    html_nodes = []
    for block in blocks:
        block_type = block_to_blocktype(block)
        if block_type == BlockType.HEADING:
            level = block.count("#")
            tag = f"h{level}"
            content = block[level:].strip()
            html_nodes.append(HTMLNode(tag, content))
        elif block_type == BlockType.CODE:
            content = block[3:-3].strip()
            html_nodes.append(HTMLNode("pre", HTMLNode("code", content)))
        elif block_type == BlockType.QUOTE:
            content = block[1:].strip()
            html_nodes.append(HTMLNode("blockquote", content))
        elif block_type == BlockType.UNORDERED_LIST:
            items = [item[2:].strip() for item in block.split("\n") if item]
            children = [HTMLNode("li", item) for item in items]
            html_nodes.append(HTMLNode("ul", children))
        elif block_type == BlockType.ORDERED_LIST:
            items = [item[3:].strip() for item in block.split("\n") if item]
            children = [HTMLNode("li", item) for item in items]
            html_nodes.append(HTMLNode("ol", children))
        else:
            html_nodes.append(HTMLNode("p", block))
    return html_nodes
