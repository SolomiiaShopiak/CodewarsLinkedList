class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return
    prev = Node(None)
    cur = head
    while cur is not None:
        if cur.data == prev.data:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return head
