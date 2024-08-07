def average_of_list(linked_list):
    if not linked_list.head:
        raise ValueError("List is empty")
    total = 0
    count = 0
    current = linked_list.head
    while current:
        total += current.value
        count += 1
        current = current.next
    return total / count
