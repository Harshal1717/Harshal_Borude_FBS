#Write a program to check if given number is Armstrong number or not. 
n = int(input('Enter a number:'))
temp = n
sum =0
l = len(str(n))

while(0<n):
    d = n%10
    print(d)
    n = n//10
    arm = 0
    for i in range(1, d+1):
        arm = i**l   
    sum +=arm    
print(sum)
if(temp == sum):
    print(f'{temp} is an Armstrong Number.')
else:
    print(f'{temp} is not an Armstrong Number.')
        
        
    
    

    


