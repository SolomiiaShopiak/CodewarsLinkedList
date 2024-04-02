from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    v = 0
    while node:
        if v == index:
            return node
        node = node.next
        v += 1
    raise ValueError
