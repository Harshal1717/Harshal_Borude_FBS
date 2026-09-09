p = int(input('Enter Principal amount:'))
t = int(input('Enter Time period for amount invested:'))
r = int(input('Enter Rate of Interest:'))

A = p*((1 + r/100)**t)

CI = A - p
print(f'The Compound Intrest on Initial Amount is {CI}')
