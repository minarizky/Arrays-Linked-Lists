def pivot_around_value(linked_list, value):
    less_head = less_tail = Node(0)
    more_head = more_tail = Node(0)
    current = linked_list.head
    while current:
        if current.value < value:
            less_tail.next = current
            less_tail = less_tail.next
        else:
            more_tail.next = current
            more_tail = more_tail.next
        current = current.next
    less_tail.next = more_head.next
    more_tail.next = None
    linked_list.head = less_head.next
