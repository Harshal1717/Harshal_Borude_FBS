# no of notes for given certain amount
'''for example 2000,500,200,100,50,20,10,5,2,1'''

a = int(input('Enter amount:'))
#cheking 1st for 2000
a1 = a//2000
a = a%2000
a2 = a//500
a = a%500
a3 = a//200
a = a%200
a4 = a//100
a = a%100
a5 = a//50
a = a%50
a6 = a//20
a = a%20
a7 = a//10
a= a%10
a8= a//5
a = a%5
a9 = a//2
a = a%2
a0 = a//1
a = a%1
t = a1+a2+a3+a4+a5+a6+a7+a8+a9+a0


print(f'Amount Rs.{a} contains notes {a1} of 2000, {a2} of 500, {a3} of 200,  {a4} of 100, {a5} of 50, {a6} of 20,{a7} of 10, {a8} of 5, {a9} of 2,  {a0} of 1')
print(f'Amount comtains total {t} notes')