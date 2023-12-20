class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value):
        if value <= self.data:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if self.data == value:
            return True
        elif self.data > value:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)
    def printInOrder(self):
        if (self.data == None):
            return
        print(self.data)
        self.left.printInOrder()

        self.right.printInOrder()
        
        
    


tree1 = Node(2)
tree1.insert(6)
tree1.insert(1)
print(tree1.data)
print(tree1.left)

print(tree1.contains(1))
print(tree1.contains(6))
print(tree1.contains(7))

print(tree1.printInOrder())