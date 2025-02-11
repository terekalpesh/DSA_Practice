# Implement a stack using an array and handle overflow/underflow conditions.

class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size


    def push(self, item):
        """Adds an item to the stack (Handles Overflow)"""
        if len(self.stack) >= self.max_size:
            print("Stack Overflow! Cannot push", item)
        else:
            self.stack.append(item)     # Add item to the stack
            print(f'Pushed {item} onto the stack')


    def pop(self):
        """Removes and returns the top item from the stack (Handles Underflow)"""
        if len(self.stack) == 0:
            print("Stack Underflow! Cannot pop from an empty stack")
        else:
            self.stack.pop()
            # print('Stack is empty.')


    def peek(self):     # Return the last item without removing it
        """Returns the top item without removing it"""
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return 'Stack is empty.'
        
stack1 = Stack(6)

# stack1.pop()    # Stack Underflow, stack is empty

# Stack Overflow, where max size of the stack is 6, and we added 7th item
list = [1, 3, 4, 5, 6, 7, 8]
for i in list:
    stack1.push(i)

print(stack1.peek())

for i in range(stack1.max_size+1):
    stack1.pop()


print(stack1.max_size)
