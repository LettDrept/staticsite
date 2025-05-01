import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        images = extract_markdown_images(text)  # Extract images from the text
        
        if not images:
            new_nodes.append(old_node)
            continue
        
        # Start with the original text
        remaining_text = text
        for alt, url in images:
            # Find where this image appears in the CURRENT remaining text
            image_markdown = f"![{alt}]({url})"
            sections = remaining_text.split(image_markdown, 1)
            
            # Add the text before the image
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))   # Add the image node
            
            # Update the remaining text for the next iteration
            if len(sections) > 1:
                remaining_text = sections[1]
            else:
                remaining_text = ""
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))    

    return new_nodes

def split_nodes_link(old_nodes):        # Identical to split_nodes_image, but for links
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        links = extract_markdown_links(text)  # Extract links from the text

        if not links:
            new_nodes.append(old_node)
            continue
        
        remaining_text = text
        
        for alt, url in links:
            link_markdown = f"[{alt}]({url})"
            sections = remaining_text.split(link_markdown, 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url))   # Add the link node
            if len(sections) > 1:
                remaining_text = sections[1]
            else:
                remaining_text = ""
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))    
    
    return new_nodes


# Function to consolidate the splitting functions

def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    node = split_nodes_delimiter(node, "`", TextType.CODE)
    node = split_nodes_image(node)
    node = split_nodes_link(node)
    node = split_nodes_delimiter(node, "**", TextType.BOLD)
    node = split_nodes_delimiter(node, "_", TextType.ITALIC)
    return node