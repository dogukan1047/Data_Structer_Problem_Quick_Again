class Node():
    def __init__(self, value):
        self.value = value
        self.rightchild = None
        self.leftchild = None


class BinarySearchTree():

    def __init__(self):
        self.root = None

    def insert_(self, value):
        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return True
        tempNode = self.root
        while True:
            if newNode.value == tempNode.value:
                return False
            if newNode.value < tempNode.value:
                if tempNode.leftchild is None:
                    tempNode.leftchild = newNode
                    return True
                else:
                    tempNode = tempNode.leftchild
            else:
                if tempNode.rightchild is None:
                    tempNode.rightchild = newNode
                    return True
                tempNode = tempNode.rightchild

    def contains(self, item):
        tempNode1 = self.root

        while tempNode1:
            if item < tempNode1.value:
                tempNode1 = tempNode1.leftchild
            elif tempNode1.value > item:
                tempNode1 = tempNode1.rigthchild
            else:
                return True
            return False

    def minOfNode(self, currentNode):

        while currentNode.leftchild:
            currentNode = currentNode.leftchild
        return currentNode

    def maxOfNode(self, currentNode):

        while currentNode.rightchild:
            currentNode = currentNode.rightchild
        return currentNode


myTree = BinarySearchTree()

myTree.insert_(10)
myTree.insert_(8)
myTree.insert_(20)
myTree.insert_(15)
myTree.insert_(18)
myTree.insert_(32)


print(myTree.contains(32))



