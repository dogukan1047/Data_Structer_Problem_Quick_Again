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

    def BFS(self):
        currentNode = self.root
        myQueue = list()
        values = list()
        myQueue.append(currentNode)

        while len(myQueue) > 0:
            currentNode = myQueue.pop(0)
            values.append(currentNode.value)
            if currentNode.leftchild is not None:
                myQueue.append(currentNode.leftchild)
            if currentNode.rightchild is not None:
                myQueue.append(currentNode.rightchild)

        return values

    def DFSPreOrder(self):

        values = list()

        def travers(currentNode):
            values.append(currentNode.value)

            if currentNode.leftchild is not None:
                travers(currentNode.leftchild)
            if currentNode.rightchild is not None:
                travers(currentNode.rightchild)

        travers(self.root)
        return values

    def DFSPostOrder(self):

        values = list()

        def travers(currentNode):

            if currentNode.leftchild is not None:
                travers(currentNode.leftchild)
            if currentNode.rightchild is not None:
                travers(currentNode.rightchild)
            values.append(currentNode.value)

        travers(self.root)
        return values

    def DFSInOrder(self):

        values = list()

        def travers(currentNode):

            if currentNode.leftchild is not None:
                travers(currentNode.leftchild)

            values.append(currentNode.value)

            if currentNode.rightchild is not None:
                travers(currentNode.rightchild)

        travers(self.root)
        return values


myTree = BinarySearchTree()
myTree.insert_(38)
myTree.insert_(19)
myTree.insert_(69)
myTree.insert_(12)
myTree.insert_(24)
myTree.insert_(59)
myTree.insert_(95)

print(myTree.BFS())

print(myTree.DFSPreOrder())

print(myTree.DFSPostOrder())

print(myTree.DFSInOrder())
