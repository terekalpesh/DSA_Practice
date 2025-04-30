# Merge two sorted linked lists into one sorted linked list.

class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

def merge_sorted_lists(l1, l2):
    dummy = Node()  # Dummy node to simplify code
    current = dummy  # Pointer to track the merged list
    
    while l1 and l2:  # Traverse both lists
        if l1.data < l2.data:  # Choose the smaller node
            current.next = l1
            l1 = l1.next  # Move ahead in list1
        else:
            current.next = l2
            l2 = l2.next  # Move ahead in list2
        current = current.next  # Move merged list pointer
    
    # If any list remains, append it
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next  # Return merged list (skip dummy node)

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Creating two sorted lists
l1 = create_linked_list([1, 3, 5])
l2 = create_linked_list([2, 4, 6])

# Merging lists
merged_head = merge_sorted_lists(l1, l2)

# Print merged list
print_list(merged_head)

    