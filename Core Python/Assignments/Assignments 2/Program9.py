n = int(input('Enter 3 digit number :'))
u = n%10
t = (n//10)%10
h = n//100

r = (u*100)+(t*10)+(h)
print(f'The revesre of {n} is {r}')