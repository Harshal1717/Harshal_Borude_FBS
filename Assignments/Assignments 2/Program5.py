#Calculate the total salary of Emplyoee based of da,hra,ta of Basic salary

b = int(input('Enter the Basic Salary of an Employee:'))

da = b*0.1
ta = b*(12/100)
hra = b*(15/100)

salary= da+hra+ta+b
print(f'The Total Salary of an Employee is {salary}')
