# Calculate discounted price of book

cp = int(input('Enter the Cost Price of Book:'))
d = int(input('Enter the Discount on Book:'))

dp = (cp*d)/100

sp = cp - dp
print(f'The Selling Price of Book after Dicount of {d}% is {sp}rs')
