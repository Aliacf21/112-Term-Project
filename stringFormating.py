import copy
import storingList
# import stringToList
# import writeTo
#import thorughFare

def findMostCommonNumber(myList):
    maxNum = None
    maxCount = 0
    #print(myList)
    temp = []
    for elem in myList:
        temp.append(int(elem))
    myList = temp
    #print(myList)
    for i in range(11):
        if myList.count(i)>maxCount:
            maxNum = i
            maxCount = myList.count(i)
    return maxNum
        
#whereIAt(inputValue, megaList=storingList.read()):
def whereIAt(inputValue, megaList=storingList.read()):
    #print(inputValue)
    myList = findClose(inputValue, megaList)
    count = findMostCommonNumber(myList)
    inputfile = open("num.txt", "r")
    #print("This is count:", count)
    for line in inputfile:
        a=line
    megaList.append(addNum(inputValue, a))
    #print(addNum(inputValue, a))
    storingList.write(megaList)
    return count
    
    
def distance(a,b):
    sumTotal=0
    for index1 in range(len(b)):
        for index2 in range(len(b[0])-1):
            sumTotal+=(a[index1][index2]-b[index1][index2])**2
    return sumTotal**(.5)
        
def findClose(inputValue, existingData):
    myList = []
    copyList = copy.deepcopy(existingData)
    for i in range(5):
        mini, index = findSmallest(inputValue, copyList)
        myList.append(copyList[index][-1][-1])
        copyList.pop(index)
    return myList
        
def findSmallest(inputValue, copyList):
    smallest = []
    for i in range(len(copyList)):
        #for j in range(len(copyList[i])):
        myDistance = distance(copyList[i], inputValue)
        smallest.append(myDistance)
    #print(smallest)
    mini = min(smallest)
    myIndex = smallest.index(mini)
    return mini,myIndex

def addNum(a, num):
    for row in range(len(a)):
        a[row].append(num)
    return a
