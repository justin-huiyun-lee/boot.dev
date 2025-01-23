class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        str_to_return = ""
        if self.props:
            for i in self.props:
                str_to_return += f'{i}="{self.props[i]}" '

        return str_to_return

    def __repr__(self):
        return f"{self.tag}"