"""
Course      : Python Is Easy       | Homework    : #3
Lecture     : If Statement         | Student Name: Abu Hdz  | Date : 07 Apr 2019

Requirement
Employee 
    Employee Name | Status | Grade | Salary      | Allowance      | Tax    |  Take home pay  |
                    M/S      1-5     M-10M, S-8M   5,10,15,20,25%   12%       Salary + Allowance - Tax
                    M/S      6-10    M-15M, S-12M  5,10,15,20,25%   13%       Salary + Allowance - Tax
"""

def salary(employeeName, status, grade):
    if(status == "Married"): 
        status = "M" 
    else: 
        status ="S"

    if(status == "M" and (grade >=1 and grade <=5)):
        salary = 10000000
    elif(status == "S" and (grade >=1 and grade <=5)):
        salary = 8000000
    elif(status == "M" and (grade >=6 and grade <=10)):
        salary = 15000000
    elif(status == "S" and (grade >=6 and grade <=10)):
        salary = 12000000
    else:
        salary = 0
    
    if(grade == 1):
        allowance = 0.05
    elif(grade == 2):
        allowance = 0.10  
    elif(grade == 3):
        allowance = 0.15  
    elif(grade == 4):
        allowance = 0.20  
    elif(grade == 5):
        allowance = 0.25  
    else:
        allowance = 0 

    allowance *= salary

    gradeTaxLvl1="1"
    gradeTaxLvl5="5"
    gradeTaxLvl6="6"
    gradeTaxLvl10="10"

    if(grade >= int(gradeTaxLvl1) and grade <= int(gradeTaxLvl5)):
        tax = 0.12
    elif(grade >= int(gradeTaxLvl6) and grade <= int(gradeTaxLvl10)):
        tax = 0.13
    else:
        tax = 0 

    tax *= salary
    
    takeHomePay = salary + allowance - tax

    print (employeeName, salary, allowance, tax, takeHomePay)

print("-------------------------------------------------------------------------")
print("Employee Name   | Salary    | Allowance    | Tax         | Take Home Pay")
print("-------------------------------------------------------------------------")
salary("Abu Hdz", "Married", 3)
salary("Yusril Halim", "Single", 1)
salary("Riani", "Married", 7)
print("-------------------------------------------------------------------------")