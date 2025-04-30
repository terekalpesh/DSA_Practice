# Design a circular queue with basic operations like enqueue, dequeue, and isFull.

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1  # Points to the front of the queue
        self.rear = -1   # Points to the rear of the queue

    def isFull(self):
        # The queue is full if the next position after rear is front
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        # The queue is empty if front is -1
        return self.front == -1

    def enqueue(self, data):
        if self.isFull():
            print("Queue is full! Cannot enqueue.")
        else:
            if self.front == -1:  # If the queue is empty, initialize front to 0
                self.front = 0
            self.rear = (self.rear + 1) % self.size  # Circular increment of rear
            self.queue[self.rear] = data
            print(f"Enqueued {data} to the queue.")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty! Cannot dequeue.")
        else:
            dequeued_value = self.queue[self.front]
            if self.front == self.rear:  # Only one element is present, reset the queue
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size  # Circular increment of front
            print(f"Dequeued {dequeued_value} from the queue.")
            return dequeued_value

    def peek(self):
        # Return the front element
        if self.isEmpty():
            print("Queue is empty! Nothing to peek.")
            return None
        return self.queue[self.front]

    def display(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            elements = []
            i = self.front
            while i != self.rear:
                elements.append(self.queue[i])
                i = (i + 1) % self.size
            elements.append(self.queue[self.rear])
            print("Queue elements:", elements)


cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

cq.display()

cq.dequeue()

cq.display()

cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)
cq.enqueue(70)  # This will fail since the queue is full

cq.display()

