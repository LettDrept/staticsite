class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):          # defaults to None if nothing is passed in
        self.tag = tag                          # String of the HTML tag
        self.value = value                      # String of the tag's contents
        self.children = children                # list of objects representing the node's children
        self.props = props                      # dict of key-value attributes of the HTML tag

    def to_html(self):
        if self.tag is None:
            return self.value or ""
        content_string = self.props_to_html()
        if self.children:
            children_html = ""
            for child in self.children:                         # Should recurse through all levels 
                children_html += child.to_html()        
            return f"<{self.tag}{content_string}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}{content_string}>{self.value or ""}</{self.tag}>"



    def props_to_html(self):
        if self.props is None:                                  # Needed to prevent a None Type error
            return ""
        props_html = ""                                         # Create blank string variable to return
        for prop in self.props:                                 # Cycle through props dict
            props_html += f' {prop}="{self.props[prop]}"'       # To append to end of string
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):                      # Returns HTML string
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value     
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children == None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:                         # Should recurse through all levels
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"        
        
        