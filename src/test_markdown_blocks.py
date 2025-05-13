import unittest

from markdown_blocks import BlockType, markdown_to_blocks, block_to_blocktype, markdown_to_html_node
from htmlnode import HTMLNode

class TestMarkdownBlocks(unittest.TestCase):

# Test Markdown to Blocks

    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            blocks,
        )
       
    def test_markdown_to_blocks_more_blank_lines(self):
        md = """
            This is **bolded** paragraph

            
            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            
            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            blocks,
        )

    def test_markdown_to_blocks_extra_whitespace(self):
        md = """
            
            This is **bolded** paragraph

            
            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            
            - This is a list
            - with items

            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            blocks,
        )

    def test_markdown_to_blocks_whitespace(self):
        md = """
            

            
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual([], blocks)

# Test Block to BlockType

    def test_block_not_string(self):
        block = 12345
        with self.assertRaises(TypeError):
            block_to_blocktype(block)

    def test_block_to_heading(self):
        block = "# This is a heading"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.HEADING, block_type)
    
    def test_block_to_heading_2(self):
        block = "##### This is a heading"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_block_to_heading_bad(self):
        block = "####### This is a bad heading"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_code(self):
        block = "```python\nprint('Hello, world!')\n```"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.CODE, block_type)

    def test_block_to_code_bad(self):
        block = "```python\nprint('Hello, world!')"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_code_bad_2(self):
        block = "``python\nprint('Hello, world!')\n```"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_quote(self):
        block = "> This is a quote"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_block_to_quote_2(self):
        block = ">This is a quote\n> This is another quote"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_block_to_quote_bad(self):
        block = "> This is a quote\nThis is not a quote"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_unordered_list(self):
        block = "- This is an unordered list\n- This is another item"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)

    def test_block_to_unordered_list_bad(self):
        block = "- This is an unordered list\nThis is not a list"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_ordered_list(self):
        block = "1. This is an ordered list\n2. This is another item"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)

    def test_block_to_ordered_list_bad(self):
        block = "1. This is an ordered list\nThis is not a list"
        block_type = block_to_blocktype(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

# Test Markdown to HTMLNode

    def test_markdown_to_html_node_heading(self):
        md = "# This is a heading"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual("<div><h1>This is a heading</h1></div>", html)

    def test_markdown_to_html_node_heading2(self):
        md = "## This is a heading"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual("<div><h2>This is a heading</h2></div>", html)

    def test_markdown_to_html_node_code(self):
        md = "```python\nprint('Hello, world!')\n```"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual("<div><pre><code>python\nprint('Hello, world!')</code></pre></div>", html)
 
    def test_markdown_to_html_node_quote(self):
        md = "> This is a quote"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        #print(html)
        self.assertEqual("<div><blockquote>This is a quote</blockquote></div>", html)

    def test_markdown_to_html_node_quote2(self):   
        md = "> This is a quote\n> This is another quote"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual("<div><blockquote>This is a quote\nThis is another quote</blockquote></div>", html)

    def test_markdown_to_html_node_unordered_list(self):
        md = "- This is an unordered list\n- This is another item"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual("<div><ul><li>This is an unordered list</li><li>This is another item</li></ul></div>", html)

    def test_markdown_to_html_node_ordered_list(self):
        md = "1. This is an ordered list\n2. This is another item"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual("<div><ol><li>This is an ordered list</li><li>This is another item</li></ol></div>", html)

    def test_markdown_to_html_node_paragraph(self):
        md = "This is a paragraph with **bold** and _italic_ text."
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        print(html)
        self.assertEqual("<div><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p></div>", html)

    def test_markdown_to_html_node_paragraph2(self):
        md = "This is a paragraph with **bold** and _italic_ text.\n\nThis is another paragraph."
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual("<div><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p><p>This is another paragraph.</p></div>", html)

    def test_markdown_to_html_node_paragraph3(self):
        md = """
        This is a paragraph with **bold** and _italic_ text.
        This is another paragraph.
        """
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual("<div><p>This is a paragraph with <b>bold</b> and <i>italic</i> text. This is another paragraph.</p></div>", html)

if __name__ == "__main__":
    unittest.main()