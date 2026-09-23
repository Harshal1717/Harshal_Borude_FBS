#WAP to check if a given number is prime number or not. 
n = int(input('Enter a Number:'))

if(n>1):

    for i in range(1,n//2+1):
        if(n%i==0):
            print(f'{n} number is Prime number.')
            break
    else:
         print(f'{n} number is Not a Prime number.')
else:
    print('Invalid Input!!')