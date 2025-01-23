import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode(
            "This is a text node", TextType.BOLD, url="https://www.boot.dev"
        )
        node2 = TextNode(
            "This is a text node", TextType.BOLD, url="https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("I LOVE MY WIFE!!!!", TextType.CODE)
        node2 = TextNode("I LOVE MY WIFE!!!!", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_yahoo(self):
        node = TextNode("I WILL HUG MY WIFE", TextType.ITALIC)
        node2 = TextNode("I really like my wife", TextType.ITALIC)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
