"""
Course      : Python Is Easy       | Homework    : #6
Home Assignment : Advance Loop     | Student Name: Abu Hdz  | Date : 17 Apr 2019
Requirement:
playing board
"""

def pb(row, col):
    if(row >= 24 or col >= 80):
        print("Max Row is 24 and Max Column is 80!")
        return False
    
    for r in range(row):
        if r % 2 == 0:
            for c in range(1,col):
                if c %2 == 1:
                    if c !=5:
                        print(" ", end = "")
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            print("-----")
    return True

pb(5,5)