def stringify(node):
    if node is None:
        return 'None'
    res = ''
    while node is not None:
        res += f'{node.data} -> '
        if node.next is None:
            res += 'None'
        node = node.next
    return res
