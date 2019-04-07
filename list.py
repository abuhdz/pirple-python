"""
Course      : Python Is Easy       | Homework    : #4
Lecture     : Lists                | Student Name: Abu Hdz  | Date : 07 Apr 2019
"""

myUniqueList = []
myLefOver = []

def add2List(val):
    if(isExist(val)):
        myLefOver.append(val)
    else:
        myUniqueList.append(val)

def isExist(val):
    for i in range(len(myUniqueList)):
        if(myUniqueList[i] == val):
            return True 
    return False 

add2List(2)
add2List(5)
add2List(2)
add2List(20)
add2List(2)
add2List(5)
add2List(2)
add2List(5)
add2List(5)
add2List("Pirple")
add2List("Columbus")
add2List("Pirple")
add2List("Columbus")
add2List("Pirple")
add2List("Pirple")
print("myUnique List    : " + str(myUniqueList))
print("MyLefOver List   : " + str(myLefOver))