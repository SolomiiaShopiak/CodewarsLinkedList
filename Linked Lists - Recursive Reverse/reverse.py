class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def reverse_recursive(cur, prev):
        if not cur:
            return prev
        next_node = cur.next
        cur.next = prev
        return reverse_recursive(next_node, cur)

    return reverse_recursive(head, None)
