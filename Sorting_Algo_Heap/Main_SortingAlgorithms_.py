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


sorting = SortingAlgorithms()
myList = [1, -1, 7, 4, 5, 9, 15, 74, 45]
print(sorting.bubbleSort(myList))

print(sorting.selectionSort(myList))
