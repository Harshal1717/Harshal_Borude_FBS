#Swap two numbers
a = int(input('Enter the 1st number:'))
b = int(input('Enter the 2nd number:'))

temp = a
a = b
b = temp

print(f'Now 1st number is {a} and 2nd number is {b}')
