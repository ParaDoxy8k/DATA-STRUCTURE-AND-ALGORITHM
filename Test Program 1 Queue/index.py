# Name: John Doe
# Student ID: 123456

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item):
        if self.rear == self.size - 1:
            return "Queue is overflow"
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item
        return f"Enqueued {item}"
    
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            return "Queue is underflow"
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        if self.front > self.rear:
            self.front = self.rear = -1
        return f"Dequeued {item}"
    
    def printqueue(self):
        if self.front == -1:
            print("Queue is empty")
            return
        print("Queue:", end=" ")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()

# Test Case 1: Queue is full when enqueue
print("Test Case 1: Queue overflow")
q1 = Queue(5)
student_id = "610109"
print("Initial queue:")
q1.printqueue()

# Enqueue last 6 digits of student ID
for digit in student_id:
    print(q1.enqueue(int(digit)))
print("After enqueue:")
q1.printqueue()

# Try to enqueue one more item to cause overflow
print(q1.enqueue(7))

# Test Case 2: Queue is empty when dequeue
print("\nTest Case 2: Queue underflow")
q2 = Queue(6)
for digit in student_id:
    q2.enqueue(int(digit))
print("Initial queue:")
q2.printqueue()

# Dequeue all elements and one more to cause underflow
for _ in range(7):  # 6 dequeues + 1 extra to cause underflow
    print(q2.dequeue())
print("After dequeue:")
q2.printqueue()