import unittest                                                     # Imports for testing
                                                                    # "test_" necessary for unittest to find
from textnode import TextNode, TextType                             # Needed for testing


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_equal(self, other):
        pass

    def test_link(self):
        self.assertNotEqual(self.url, None)
    
    def test_formatting(self, other):
        self.assertEqual(self.text_type, other.text_type)