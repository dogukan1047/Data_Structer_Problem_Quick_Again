class SearchingAlgorithms:

    def sequantialSearchUnordered(self, unOrderderList, number):
        for numberSearch in unOrderderList:
            if numberSearch == number:
                return True
        return False

    def sequantialSearchOrdered(self, orderderList, number):
        for numberSearch in orderderList:
            if numberSearch == number:
                return True
            if numberSearch > number:
                return False
        return False

    def binarySearch(self, orderedList, number):
        firstPointer = 0
        secondPointer = len(orderedList)-1
        found=False

        while firstPointer<=secondPointer and not found:

            midPoint=(firstPointer+secondPointer)//2

            if orderedList[midPoint]==number:
                found =True
            else:
                if orderedList[midPoint]>number:

                    secondPointer=midPoint-1
                else:
                    firstPointer=midPoint+1

            return found













myList = [1, 2, 5, 7, 9, 10]
myClass = SearchingAlgorithms()
print(myClass.sequantialSearchUnordered(myList, 7))
print(myClass.sequantialSearchOrdered(myList, 8))
print(myClass.binarySearch(myList,5))
