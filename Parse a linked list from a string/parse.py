def linked_list_from_string(s):
    if s == 'None':
        return None
    data = s.split(" -> ")
    head = Node(int(data[0]))
    current = head
    for n in data[1:-1]:
        current.next = Node(int(n))
        current = current.next
    return head
