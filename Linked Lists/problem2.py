# Detect a cycle in a linked list and find the starting node of the cycle.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def detectCycle(head):

    # Checks list is empty or not or only has one node
    if not head or not head.next:
        return None
    
    slow = head
    fast = head

    # Check if there is cycle
    while fast and fast.next:
        slow = slow.next    # Move pointer by 1 step
        fast = fast.next.next   # Move pointer by 2 steps

        if slow == fast:    # Cycle detect if true
            break
    else:
        return None
    
    # Find start of the cycle
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Create the cycle
    
cycle_start = detectCycle(node1)

if cycle_start:
    print(f"The cycle starts at node with value: {cycle_start.value}")
else:
    print("No cycle detected")