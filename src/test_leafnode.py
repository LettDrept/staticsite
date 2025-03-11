import unittest                                         # Imports for testing
                                                        # "test_" function name necessary for unittest to find
from htmlnode import HTMLNode, LeafNode                 # Needed for testing


class TestHTMLNode(unittest.TestCase):                  # Keep tested nodes simple!

    def test_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_None(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, lambda: node.to_html())     # lambda allows for assertRaises to run and verify error w/o raising the error

    def test_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')



if __name__ == "__main__":              # Needed to run tests
    unittest.main()
