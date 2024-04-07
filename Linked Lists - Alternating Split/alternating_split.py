class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError
    head_odd, cur_odd, cur_even = head.next, head.next, head
    try:
        cur = head.next.next
    except AttributeError:
        cur = None
    i = 2
    while True:
        if i % 2:
            cur_odd.next = cur
            cur_odd = cur
        else:
            cur_even.next = cur
            cur_even = cur
        try:
            cur = cur.next
        except AttributeError:
            break
        i += 1
    return Context(head, head_odd)
