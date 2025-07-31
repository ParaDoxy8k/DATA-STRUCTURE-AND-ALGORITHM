# Name: Thitiwat Phanparkhon
# Student ID: 6606021610109

class Queue:
    def __init__(self, limit=5):
        self.items = []
        self.limit = limit
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def enQueue(self, item):
        if self.size >= self.limit:
            return "Queue is overflow"
        self.items.append(item)
        self.rear += 1
        self.size += 1
        return f"Enqueued {item}"
    
    def deQueue(self):
        if self.isEmpty():
            return "Queue is underflow"
        item = self.items.pop(0)
        self.size -= 1
        self.rear = self.size - 1 if self.size > 0 else -1
        return f"Dequeued {item}"
    
    def printqueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Queue:", end=" ")
        for i in range(self.size):
            print(self.items[i], end=" ")
        print()

print("Name : Thitiwat Phanparkhon")
print("Student ID : 6606021610109")
# Test Case 1: Queue is full when enqueue
print("Test Case 1: Queue overflow")
q1 = Queue(5)
student_id = "610109"  # Last 6 digits of 6606021610109
print("Initial queue:")
q1.printqueue()

# Enqueue last 6 digits of student ID
for digit in student_id:
    print(q1.enQueue(int(digit)))
print("After enqueue:")
q1.printqueue()

print(q1.enQueue(7))

# Test Case 2: Queue is empty when dequeue
print("\nTest Case 2: Queue underflow")
q2 = Queue(6)
for digit in student_id:
    q2.enQueue(int(digit))
print("Initial queue:")
q2.printqueue()

# Dequeue all elements and one more to cause underflow
for _ in range(7):  # 6 dequeues + 1 extra to cause underflow
    print(q2.deQueue())
print("After dequeue:")
q2.printqueue()