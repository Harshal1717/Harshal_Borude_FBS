#WAP to check given number is prime or not
num = int(input('Enter number:'))

if(num > 1):
    for i in range(2, num//2 + 1): # here we optimize our code . what we did here is we know that in tables min time is twice if 
        if(num%i == 0):# nummber's half it is sufficient to chek that it is divisible or not from others.
            print(f'{num} is not a Prime number.')
            break
    else:
        print(f'{num} is a Prime number.')
else:
    print('Input Invalid!!')
