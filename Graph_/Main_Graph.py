class Graph:
    def __init__(self):
        self.adjDict = {}# graph

    def addVertex(self, vertex):# Bir vertex(Node) eklenmesi
        if vertex not in self.adjDict.keys():
            self.adjDict[vertex] = []
            return True
        return False

    def addEdge(self, v1, v2):# Bağlantı ekledik
        if v1 in self.adjDict.keys() and v2 in self.adjDict.keys():
            self.adjDict[v1].append(v2)
            self.adjDict[v2].append(v1)
            return True
        return False


    def removeEdge(self,v1,v2):
        if v1 in self.adjDict.keys() and v2 in self.adjDict.keys():
            try:
                self.adjDict[v1].remove(v2)
                self.adjDict[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def removeVertex(self,vertex):
        if vertex in self.adjDict.keys():

            for relatedVertex in self.adjDict[vertex]:
                self.adjDict[relatedVertex].remove(vertex)
            del self.adjDict[vertex]
            return True
        return False

    def printGraph(self):
         for vertex in self.adjDict:
             print(vertex,"-->",self.adjDict[vertex])


myGrapg=Graph()
myGrapg.addVertex("Ist")
myGrapg.addVertex("Roma")
myGrapg.addVertex("Paris")
myGrapg.addVertex("Ankara")
myGrapg.addVertex("Londra")

myGrapg.addEdge("Ist","Paris")
myGrapg.addEdge("Ist","Ankara")
myGrapg.addEdge("Londra","Paris")
myGrapg.addEdge("Roma","Ankara")

myGrapg.printGraph()


