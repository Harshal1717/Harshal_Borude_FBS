#WAP to check if given number is Perfect Number.  
n = int(input('Enter a number:'))
sum = 0

for i in range(1, n//2 + 1):
    if(n%i==0):
        sum += i
  
if(sum==n):
    print(f'{n} is a Perfect number.')
else:
    print(f'{n} is not a Perfect Number.')

    

