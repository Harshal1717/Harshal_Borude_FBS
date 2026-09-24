#WAP to print all numbers in a range divisible by a given number.
n = int(input('Enter a number:'))
r = int(input('Enter a Range till you want check:'))
for i in range(1,r+1):
    if(i%n==0):
        print(i, end=' ')
    else:
        pass


 