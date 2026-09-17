# Check given 3 digit number is palindrome or not

num = int(input("Enter 3 digit number:"))
u = num%10
h = num//100

if(num >=100 and num <=999):
    if(u==h):
        print(f'Number {num} is Palindrome Number.')
    else:
        print(f'Number {num} is nOt Palindrome Number.')
else:
    print(f'Number {num} is Invalid!!')
    


   