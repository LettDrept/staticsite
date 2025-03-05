from textnode import TextNode, TextType         # Imports textnode classes

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()      # need to call main to execute