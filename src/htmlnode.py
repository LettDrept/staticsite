

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):          # defaults to None if nothing is passed in
        self.tag = tag                          # String of the HTML tag
        self.value = value                      # String of the tag's contents
        self.children = children                # list of objects representing the node's children
        self.props = props                      # dict of k-v attributes of the HTML tag

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:                                  # Needed to prevent a None Type error
            return ""
        props_html = ""                                         # Create blank string variable to return
        for prop in self.props:                                 # Cycle through props dict
            props_html += f' {prop}="{self.props[prop]}"'       # To append to end of string
        return props_html
        
        return str(self.props)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):                      # Returns HTML string
        if self.value == None:
            raise ValueError("No value in leaf")
        if self.tag == None:
            return str(self.value)
        
        link = super().props_to_html()        
        return f"<{self.tag}{link}>{self.value}</{self.tag}>"
