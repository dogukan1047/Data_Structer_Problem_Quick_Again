class Stack():
    def __init__(self):
        self.liste = list()

    def push(self, item):
        self.liste.append(item)

    def pop(self):
        return self.liste.pop()

    def isEmpty(self):
        if len(self.liste) == 0:
            return True
        return False

    def size(self):
        return len(self.liste)

    def showLast(self):
        return self.liste[-1]


myStack = Stack()

myStack.push(15)
myStack.push(20)
myStack.push(25)
myStack.push(30)

print(myStack.pop())

print(myStack.size())

print(myStack.isEmpty())

print(myStack.showLast())

# Stack veri yapısını ters çevirmek için pop edip onu listeye atmamız yeterli 
