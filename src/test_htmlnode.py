import unittest                                         # Imports for testing
                                                        # "test_" function name necessary for unittest to find
from htmlnode import HTMLNode                           # Needed for testing


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



if __name__ == "__main__":              # Needed to run tests
    unittest.main()