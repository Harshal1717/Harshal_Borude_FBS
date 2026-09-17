# Printing 2 * 1 = 2 till 2 * 10 = 20 for any number given by user
n = int(input('Enter a Number :'))
i = 1
while(i<=10):
    a = n * i;
    print(f'{n} * {i} = {a}')
    i+=1