import unittest                                         # Imports for testing
                                                        # "test_" function name necessary for unittest to find
from htmlnode import HTMLNode, LeafNode, ParentNode     # Needed for testing


class TestHTMLNode(unittest.TestCase):                  # Keep tested nodes simple!

    def test_to_html(self):
        node = HTMLNode("p", "Test prop text.", None, {"href": "https://www.google.com", "target": "_blank",})  # Create node to test props_to_html
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )      # Runs props_to_html and only its specific output, rest of node is fluff 

    def test_repr(self):
        node = HTMLNode("p", "Paragraph here.", None, { "target": "_blank",})           # Create node to test __repr__
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, Paragraph here., children: None, {'target': '_blank'})",
        )       # Runs __repr__, note syntax of commas and parentheses. Last comma needed due to multiline use of function

    def test_values(self):
        node = HTMLNode("p", "Test text.", None, None)     # Keep it simple for easy testing
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Test text.")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

# Test LeafNode:

    def test_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_None(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, lambda: node.to_html())     # lambda allows for assertRaises to run and verify error w/o raising the error

    def test_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')

# Test ParentNode:

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )




if __name__ == "__main__":              # Needed to run tests
    unittest.main()