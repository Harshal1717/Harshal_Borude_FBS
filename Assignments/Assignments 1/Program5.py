#Simple Intrest Calculation

p = int(input('Enter Principal amount:'))
t = int(input('Enter Time period for amount invested:'))
r = int(input('Enter Rate of Interest:'))

SI = (p*t*r)/100
print(f'The Simple Intrest of given Amount is Rs. {SI}')