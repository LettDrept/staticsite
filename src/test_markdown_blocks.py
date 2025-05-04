import unittest

from markdown_blocks import BlockType, markdown_to_blocks, block_to_blocktype


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

if __name__ == "__main__":
    unittest.main()