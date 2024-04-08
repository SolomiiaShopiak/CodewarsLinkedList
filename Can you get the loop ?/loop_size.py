def loop_size(node):
    slow = node
    fast = node

    while True:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            length = 1
            fast = fast.next
            while slow != fast:
                fast = fast.next
                length += 1
            return length
