# wap to check given nuber is storng or not strong number mean example 145 so that 1! + 4!+ 5! == 145

num = int(input('Enter a number:')) # take input
temp = num # we need to compare it further so that we declare a temprory variable
sum = 0 

while(num>0):
    d = num%10
    num = num // 10 # this program we used for separate digit
    fact = 1
    for i in range(1, d+1): # for factorial
        fact *= i
    sum += fact # we need to add faco
if(sum == temp):
    print(f'{temp} is a Strong Number.')
else:
    print(f'{temp} is not a Strong Number.')
    
    

    












    

    

