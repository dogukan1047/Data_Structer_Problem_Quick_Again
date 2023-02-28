def twoNumberSum(array, targetSum):
    myList = list()
    for i, x in enumerate(array):
        for k, t in enumerate(array):
            if i == k:
                print(i,k)
                continue
            if x + t == targetSum:
                print(x,t)
                if myList not in x:
                    myList.append(x)
                if myList not in t:
                    myList.append(t)

    return myList

print(twoNumberSum([1,-1,5,4,7,9,10,1,9],10))