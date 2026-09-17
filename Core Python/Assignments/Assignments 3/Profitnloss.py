#Write a program to calculate profit or loss.
sp = int(input('Enter Selling Price:'))
cp = int(input('Enter Cost Price:'))
if(sp > cp):
    print('!!Profit!!')
elif(sp == cp):
    print('No Loss No Profit')
else:
    print('!!Loss!!')