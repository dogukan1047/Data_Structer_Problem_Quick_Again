class Deque():

    def __init__(self):
        self.liste = list()

    def addRight(self, item):
        return self.liste.append(item)

    def addLeft(self, item):
        return self.liste.insert(0, item)

    def removeRight(self):
        return self.liste.pop()

    def removeLeft(self):
        return self.liste.pop(0)

    def isEmpty(self):
        return self.liste == []

    def size(self):
        return len(self.liste)

    def __str__(self):
        return str(self.liste)


myDeque=Deque()

myDeque.addRight(10)
myDeque.addRight(20)
myDeque.addRight(30)

# [10,20,30]

myDeque.addLeft(40)
myDeque.addLeft(50)
myDeque.addLeft(60)

# [60,50,40,10,20,30]

myDeque.removeLeft()

# [50,40,10,20,30]

myDeque.removeRight()

# [50,40,10,20]

print(myDeque)






