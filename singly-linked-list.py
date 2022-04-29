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

ll = SinglyLinkedList(6)
ll.append(8)
ll.append(10)
ll.push(4)
ll.push(2)
ll.push(0)
# 0 2 4 6 8 10
print(ll.head.next.next.value)
print(ll.size)
print(ll.insert(6, 3))