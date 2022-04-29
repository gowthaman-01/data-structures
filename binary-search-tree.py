# To be added:
#   1) Successor/Predecessor
#   2) Remove
#   3) Balance

class TreeNode: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.frequency = 1

    def insert(self, newValue):
        if newValue > self.value:
            if self.right == None:
                self.right = TreeNode(newValue)
            else:
                self.right.insert(newValue)

        elif newValue == self.value:
            self.frequency += 1

        else:
            if self.left == None:
                self.left = TreeNode(newValue)
            else:
                self.left.insert(newValue)
        
    def search(self, searchValue):
        if searchValue == self.value:
            return True

        elif searchValue > self.value:
            if self.right == None:
                return False
            else:
                self.right.search(searchValue)
        
        else: 
            if self.left == None:
                return False
            else:
                self.left.search(searchValue)

    def inorder(self):
        if self.left != None:
            self.left.inorder()

        while self.frequency != 0:
            print(self.value)
            self.frequency -= 1

        if self.right != None:
            self.right.inorder()
    
    def preorder(self):
        while(self.frequency > 0):
            print(self.value)
            self.frequency -= 1

        if self.left != None:
            self.left.preorder()

        if self.right != None:
            self.right.preorder()

    def postorder(self):
        if self.left != None:
            self.left.postorder()

        if self.right != None:
            self.right.postorder()
            
        while(self.frequency != 0):
            print(self.value)
            self.frequency -= 1