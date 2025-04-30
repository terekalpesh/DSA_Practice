# Implement a queue using two stacks.

class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []    # Used for 'push'
        self.stack2 = []    # Used for 'pop'

    def enqueue(self, item):
        self.stack1.append(item)    # Pust item to stack1

    def dequeue(self):
        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, queue is empty
        if not self.stack2:
            raise IndexError('dequeue from empty queue')
        
        return self.stack2.pop()
    
        
queue = QueueUsingTwoStacks()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())