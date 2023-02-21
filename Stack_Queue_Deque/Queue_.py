

class Queue():

    def __init__(self):
        self.liste=list()


    def enqueu(self,element):
        return self.liste.insert(0,element)

    def denqueue(self):
       return self.liste.pop()

    def isEmpty(self):
        return self.liste == []

    def size(self):
        return len(self.liste)

    def __str__(self):
       return str(self.liste)




myQueue=Queue()

myQueue.enqueu(15)
myQueue.enqueu(20)
myQueue.enqueu(30)

print(myQueue)

print(myQueue.denqueue())




