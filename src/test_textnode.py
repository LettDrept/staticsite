import unittest                                                     # Imports for testing
                                                                    # "test_" function name necessary for unittest to find
from textnode import TextNode, TextType, text_node_to_html_node                             # Functions needed for testing


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
        node2 = TextNode("Text me", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_equal_url(self):
        node = TextNode("Test me", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("Test me", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

# Test Text to HTML

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)     
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">This is a link node</a>')
        
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)     
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.to_html(), '<img src="https://www.google.com" alt="This is an image node">')



if __name__ == "__main__":
    unittest.main()