# Remove duplicates from a sorted linked list.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None  # Initially the linked list is empty
    
    def append(self, value):
        new_node = ListNode(value)  # Create a new node with the given value
        if not self.head:  # If the list is empty, set the new node as the head
            self.head = new_node
            return
        
        current = self.head
        # Traverse to the last node
        while current.next:
            current = current.next
        
        current.next = new_node  # Add the new node to the end
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> " if current.next else "")
            current = current.next
        print()  # To add a newline at the end of the list

    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next  # Remove the duplicate
            else:
                current = current.next  # Move to the next node
    
    

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(3)

# Linked list with duplicates
linked_list.print_list()

linked_list.remove_duplicates()

# Linked list by reomoving duplicates
linked_list.print_list()

