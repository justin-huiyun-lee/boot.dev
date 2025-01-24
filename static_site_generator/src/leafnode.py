from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value, props=None):
        super().__init__(tag, value, None, props)
