# Sum of 3 digit number

num = int(input('Enter 3 digit number:'))

d1 = num%10
num = num//10
d2 = num%10
num = num//10

sum = d1+d2+num
print(f'The sum of 3 digits of nmumber is {sum}')
