# Reverse a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data    # Element 
        self.next = None    # Pointer to the next node  # Address of the next header    # Stores next node 

class Linked_list:
    def __init__(self):
        self.head = None    # Node/Head of the list

    def append(self, data):
        new_node = Node(data)   # Created new node with new element
        
        if not self.head:   # If self.head None, head will assign to new node
            self.head = new_node
            return
        
        last = self.head    # Starts from first node
        
        while last.next:   # While 'self.head' is not None, It'll traverse next to last
            last = last.next
            # print(last)
        
        last.next = new_node
        # print(self.head)
        
    def display(self):
        """Print the linked list."""
        temp = self.head    # Variable that stores first head or node
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next    # Move pointer to next head
        print("None")

    def reverse(self):
        prev = None     # Set previous node to None
        current = self.head     # Head of the linked list

        while current:
            next = current.next 
            current.next = prev
            prev = current
            current = next

        self.head = prev


linked_list = Linked_list()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.display()
linked_list.reverse()
linked_list.display()