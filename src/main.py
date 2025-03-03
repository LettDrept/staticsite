from textnode import TextNode, TextType         # Imports textnode classes

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

main()      # need to call main to execute