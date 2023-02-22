from Node import Node,DoublyNode

firstNode = Node(10)
secondNode = Node(15)
thirdNode = Node(20)

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode
thirdNode.nextNode = None

print(firstNode.nextNode.value)  # Second Node değeri

firstNode = DoublyNode(10)
secondNode = DoublyNode(20)
thirdNode = DoublyNode(30)

firstNode.nextNode=secondNode
secondNode.prevNode=firstNode
secondNode.nextNode=thirdNode
thirdNode.prevNode=secondNode

print(thirdNode.prevNode.prevNode.value)