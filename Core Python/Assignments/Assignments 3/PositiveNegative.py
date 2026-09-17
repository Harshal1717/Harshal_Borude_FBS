# WAP to check given number is postive or negative
n = int(input('Enter a Number: '))
if(n > 0):
    print(f'Your Number {n} is Positive.')
elif(n == 0):
    print(f'Your Number {n} is Zero.')
else:
    print(f'Your Number {n} is Negative.')