from queue import LifoQueue,Queue
from collections import deque

myList = list()


myList.append(1)  # en başa ekler stack mantıgı ile çalışır
myList.append(2)
myList.append(3)

print(myList)

print(myList.pop())  # en baştaki elemanı çıkarır
print()

# --------------------------------------------------------------

lifo_Queue=LifoQueue()

lifo_Queue.put(1)
lifo_Queue.put(10)
lifo_Queue.put(12)
lifo_Queue.put(15)

print("LifoQueue get:",lifo_Queue.get()) # son eklenen veriyi yani en baştaki veriyi çıakrır


print(lifo_Queue)
print()

# -----------------------------------------------------------------------------------

myQueue=Queue()

myQueue.put(1)
myQueue.put(2)
myQueue.put(3)
myQueue.put(4)


print("Queue get:",myQueue.get()) # Queue veri yapısı gibi en ilk giren veriyi çıkarır
print("Max ",myQueue.maxsize)

#---------------------------------------------------------------------------

mydeque=deque()

mydeque.append(1)
mydeque.append(2)
mydeque.append(3)

mydeque.appendleft(4)
mydeque.appendleft(5)

print("max len", len(mydeque))
for i in range(len(mydeque)):
    print(mydeque.pop())
    mydeque.popleft()
    mydeque.po
