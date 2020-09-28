# 1 - Countdown

def countDown(num):
    list = []
    for x in range(num,-1,-1):
        list.append(x)
    return list
print(countDown(5))
# [5,4,3,2,1,0]


# 2 - Print and Return

def printReturn(list):
    print(list[0])
    return(list[1])
printReturn([1,2])
# 1


# 3 - First Plus Length

def firstPlusLen(list):
    first = list[0]
    length = len(list)
    return first + length

print(firstPlusLen([1,2,3,4,5]))
# 6


# 4 - Values Greater than Second

def greatSec(list):
    newList = []
    count = 0
    for i in range(0,len(list),1):
        if list[i] > list[1]:
            newList.append(list[i])
            count+=1
    print(count)    
    if count < 2:
        return False
    else:
        return newList

print(greatSec([5,2,3,2,1,4]))


# 5 - This Length, That Value

def lenVal(size,value):
    list = []
    for i in range(0,size,1):
        list.append(value)
    return list
print(lenVal(4,7))
print(lenVal(6,2))