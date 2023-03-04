class Node:
    def __init__(self, value):
        self.value = value  # değeri tuttuk
        self.nextNode = None  # bir sonraki node'un adresini tuttuk


class DoublyNode():
    def __init__(self, value):
        self.value = value
        self.nextNOde = None
        self.prevNode = None


class LinkedList():
    def __init__(self):
        self.head = None

    def InsetAtBeginning(self, new_value):
        new_Node = Node(new_value)
        new_Node.nextNode = self.head
        self.head = new_Node

    def InsetAfter(self, prev_Node, new_Value):

        if prev_Node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_Value)
        new_node.nextNode = prev_Node.nextNode
        prev_Node.next = new_node

        # Insert at the end

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)  # Yeni node olşturduk

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.nextNode

        last.nextNode = new_node

        # Deleting a node

    def deleteNode(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.nextNode
            temp = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp = temp.nextNode
            if temp is None:
                break

        # If the key is not present
        if temp is None:
            return

        if temp.nextNode is None:
            return

        next = temp.nextNode.nextNode

        temp.nextNode = None

        temp.nextNode = next

    def search(self, key):

        current = self.head

        while current is not None:
            if current.value == key:
                return True

            current = current.nextNode

        return False

    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.value) + " ", end="")
            temp = temp.nextNode