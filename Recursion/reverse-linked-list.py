class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def reverseIterative(self):
        prev, cur = None, self.head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev

    def recursiveHelper(self, node):
        if not node or not node.next:
            return node
        newHead = self.recursiveHelper(node.next)
        node.next.next = node
        node.next = None
        return newHead

    def reverseRecursive(self):
        self.head = self.recursiveHelper(self.head)

    def display(self):
        cur = self.head
        output = []
        while cur:
            output.append(cur.val)
            cur = cur.next
        return output


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

ll = LinkedList(node1)
ll.reverseRecursive()
print(ll.display())
