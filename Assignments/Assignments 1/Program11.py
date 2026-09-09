#Quadratic equations root

a = int(input('Enter value of a:'))
b = int(input('Enter value of b:'))
c = int(input('Enter value of c:'))

# calculate d i.e delta

d = (b**2)-( 4*a*c)




if d > 0:
    x1 = (-b + d**0.5)//(2*a)
    x2 = (-b - d**0.5)// (2*a)
    print(f'The roots of equation are {x1} and {x2} ')
elif d == 0:
    x= - b/(2*a)
    print(f'The root of equation is {x}')
else :
    print(f'The equation has no real roots.')




