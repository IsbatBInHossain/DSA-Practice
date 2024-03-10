

def sortedInsert(llist, data):
    # Write your code here
    node = DoublyLinkedListNode(data)
    if llist is None:
        return node
    if llist.data > data:
        node.next = llist
        llist.prev = node
        return node
        
    current = llist
    while current.next is not None and current.next.data < data:
        current = current.next

    node.next = current.next
    if current.next is not None:
        current.next.prev = node
    current.next = node
    node.prev = current
    
    return llist
    

