
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    h = head
    if h is None:
        return Node(data)
    while h.data < data:
        if h.next is None or data < h.next.data:
            break
        h = h.next
    if h.data > data:
        head = Node(data, head)
    else:
        h.next = Node(data, h.next)
    return head
