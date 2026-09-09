#swap 2 numbers without using temprory variable
a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd number:'))

a = a+b
b = a-b
a = a-b
print(f'Now the 1st number is {a} and 2nd number is {b}')