"""
Course      : Python Is Easy       | Homework    : #5
Home Assignment : Basic Loop       | Student Name: Abu Hdz  | Date : 17 Apr 2019
Requirement:
* write program that print the number 1-100
* multiple 3 print Fizz    * multiple 5 print Buzz   * multiple both print FizzBuzz   * print Prime is prime
"""
for i in range(1, 100):
    if(i%3 == 0): print(str(i) + " is Fizz (mod 3)")
    elif(i%5 ==0): print(str(i) + " is Buzz (mod 5)")
    elif(i%3 ==0 and i%5 == 0): print(str(i) + " is FizzBuzz (mod 3 and 5)")
    
    prime = False 
    if i>=2 :
        prime = True
        for j in range(2, i):
            if (i % j) == 0:
                prime = False
    
    if(prime): print(str(i) + " is Prime! ")