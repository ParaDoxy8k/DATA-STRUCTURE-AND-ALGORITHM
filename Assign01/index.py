# Assign 1: Linked
# List

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
    
    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    
    def insert(self, item, pos):
        if pos < 0:
            raise ValueError("Position cannot be negative")
        
        current = self.head
        previous = None
        i = 0
        
        # Special case: insert at position 0
        if pos == 0:
            self.add(item)
            return
        
        # Traverse to the position
        while current is not None and i < pos:
            previous = current
            current = current.get_next()
            i += 1
        
        # If position is beyond list length
        if i < pos:
            raise ValueError("Position out of range")
        
        temp = Node(item)
        temp.set_next(current)
        previous.set_next(temp)

# Example usage
mylist = LinkedList()
mylist.add(6)
mylist.add(1)
mylist.add(1)
mylist.add(0)
mylist.add(9) # then we’ve the result 0, 0, 1, 1, 6, 9 but?    

# The next input is
# 3. Can we use method add() again?

# Yes we can.