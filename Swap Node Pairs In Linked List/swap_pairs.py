from preloaded import Node

def swap_pairs(head):
    if head is None:
        return None
    
    before_head = Node(head)
    prev = before_head
    
    while prev.next is not None and prev.next.next is not None:
        first = prev.next
        second = first.next
        prev.next, second.next, first.next = second, first, second.next
        prev = first
        
    return before_head.next
