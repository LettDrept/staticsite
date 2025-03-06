import unittest                                                     # Imports for testing
                                                                    # "test_" function name necessary for unittest to find
from textnode import TextNode, TextType                             # Needed for testing


class TestTextNode(unittest.TestCase):
    def test_equal(self):
        node = TextNode("Test me", TextType.ITALIC)
        node2 = TextNode("Test me", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_unequal_format(self):
        node = TextNode("Test me", TextType.ITALIC)
        node2 = TextNode("Test me", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_unequal_text(self):
        node = TextNode("Test me", TextType.TEXT)
        node2 = TextNode("Test me", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_equal_url(self):
        node = TextNode("Test me", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("Text me", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()