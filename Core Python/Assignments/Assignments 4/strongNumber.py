#WAP to check if given number Strong Number.  145 -= 1!+4!+5!
n = int(input('Enter a number:'))
temp = n
sum = 0
while(0<n):
    d  = n%10
    n = n//10
    # print(d)
    fact = 1
    for i in range(1,d+1):
        fact *= i
    sum += fact 
if(sum == temp):
    print(f'{temp} is a Strong number.')
else:
    print(f'{temp} is not a Strong number')


        



