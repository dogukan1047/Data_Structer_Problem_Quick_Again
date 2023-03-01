class HashTable():
    def __init__(self, size=13):
        self.dataMap = [None] * size

    def hashFunction(self, key):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 19) % len(self.dataMap)

        return myHash

    def setItem(self, key, value):
        index = self.hashFunction(key)
        if self.dataMap[index] == None:
            self.dataMap[index] = []
            self.dataMap[index].append([key, value])

    def getItem(self, key):
        index = self.hashFunction(key)

        if self.dataMap[index] is not None:
            for i in range(len(self.dataMap[index])):

                if self.dataMap[index][i][0] == key:
                    return self.dataMap[index][i][1]

    def getKeys(self):
        keys = list()

        for i in range(len(self.dataMap)):
            if self.dataMap[i] is not None:
                for j in range(len(self.dataMap[i])):
                    keys.append(self.dataMap[i][j][0])
        return keys

    def printTable(self):
        for index, value in enumerate(self.dataMap):
            print(index, "-->", value)


myHashTable = HashTable()

myHashTable.setItem('apple', 100)
myHashTable.setItem('muz', 150)
myHashTable.setItem('armut', 300)
myHashTable.setItem('portakal', 500)


print(myHashTable.getKeys())
print(myHashTable.printTable())
