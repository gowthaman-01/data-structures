class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.size = 1

    # Insert at the back
    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1
    
    # Insert at the front
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    # Remove front element
    def pop(self):
        first = self.head
        self.head = self.head.next
        self.size -= 1
        return first
    
    # Insert value at a certain index
    def insert(self, index, value): 
        if index >= self.size: 
            return -1
        newNode = Node(value)
        currentIndex = 0
        current = self.head
    
        while(currentIndex < index - 1):
            current = current.next
            currentIndex += 1
        
        temp = current.next
        current.next = newNode
        newNode.next = temp
        return 0