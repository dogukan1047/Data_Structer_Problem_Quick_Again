class SortingAlgorithms:

    def bubbleSort(self, arr):

        for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selectionSort(self, arr):

        for i in range(len(arr) - 1):
            minIndex = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            if i != minIndex:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr

    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            while temp < arr[j] and j > -1:
                arr[j + 1] = arr[j]
                arr[j] = temp
                j -= 1
        return arr

    def merge(self, arr1, arr2):
        firstPointer = 0
        secondPointer = 0
        mergeList = list()

        while firstPointer < len(arr1) and secondPointer < len(arr2):

            if arr1[firstPointer] < arr2[secondPointer]:
                mergeList.append(arr1[firstPointer])
                firstPointer += 1
            else:
                mergeList.append(arr2[secondPointer])
                secondPointer += 1

        while firstPointer < len(arr1):
            mergeList.append(arr1[firstPointer])
            firstPointer += 1

        while secondPointer < len(arr2):
            mergeList.append(arr2[secondPointer])
            secondPointer += 1
        return mergeList

    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr
        midPoint = len(arr) // 2
        leftpart=arr[:midPoint]
        rightPart=arr[midPoint:]
        return self.merge(self.mergeSort(leftpart),self.mergeSort(rightPart))


sorting = SortingAlgorithms()
myList = [1, -1, 7, 4, 5, 9, 15, 74, 45]
print(sorting.bubbleSort(myList))

print(sorting.selectionSort(myList))

print(sorting.insertionSort(myList))

print(sorting.mergeSort(myList))
