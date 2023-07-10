# swap program
myList = [1, 7, 3, 90, 23, 4]
print("Initial List : ", myList)
length = len(myList)
temp = myList[0]
myList[0] = myList[length - 1]
myList[length - 1] = temp
print("List after Swapping : ", myList)
