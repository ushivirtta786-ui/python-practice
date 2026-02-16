Mass=float(input('Entre a='))
Velocity=float(input('Entre b='))
Momentum = Mass*Velocity
print('Momentum is= ', Momentum)

a= float(input('A='))
b= float(input('B='))
print('add = ', a+b)
print('sub = ', a-b)
print('Div = ', a/b)
print('modulos =', a%b)

import math
c=float(input('c='))
if 0<c<9:
    print('C*C',c*c)

elif 0<c<99:
        print(c**(1/2))

elif 0<c<999:
            print(c*c*c)

num=int(input('A='))
reverse_num = int(str(num)[::-1])
print('A=', reverse_num)

from datetime import datetime

def age(dob):
    dob = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

def inr_to_usd(slalary):
    return salary / 74.85

dob = input("Birthdate (YYYY-MM-DD): ")
salary = float(input("Salary in INR: "))

print("Age:", age(dob))
print("Salary in USD:", round(inr_to_usd(salary), 2))
