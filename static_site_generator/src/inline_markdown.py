
import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_list = []
    if len(old_nodes) == 1 and old_nodes[0].text_type != TextType.TEXT:
        split_list.extend(old_nodes)
        return split_list
    
    counter = 0
    for i in old_nodes:
        for j in i.text:
            if j == delimiter:
                counter += 1

    if counter % 2 == 1:
        raise Exception ("invalid markdown syntax")
    
    backup = ""
    for i in old_nodes:
        backup += i.text
    
    length = 0
    prev_found = False
    for i in old_nodes:
        if i.text_type == TextType.TEXT:
            new_string = i.text.split(delimiter)
            for j in new_string:
                length += len(j)
                found = backup.find(j)

                if delimiter in backup[found - len(delimiter):found] and delimiter in backup[found + len(j):found + len(j) + len(delimiter)]:
                    if not prev_found:
                        split_list.extend([TextNode(j, text_type)])
                        prev_found = True
                    else:
                        prev_found = False
                        if j != "" and j != " ":
                            split_list.extend([ TextNode(j, i.text_type) ])
                else:
                    if j != "" and j != " ":
                        split_list.extend([ TextNode(j, i.text_type) ])
        else:
            split_list.extend([i])
        

    return split_list


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    pass






