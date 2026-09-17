# Write a program to input electricity unit charges and calculate total electricity bill 
#according to the given condition: 
#For first 50 units Rs. 0.50/unit 
#For next 100 units Rs. 0.75/unit 
#For next 100 units Rs. 1.20/unit 
#For unit above 250 Rs. 1.50/unit 
#An additional surcharge of 20% is added to the bill 
u = int(input('Enter units of Electricity used:'))
if(u <= 50):
    u50 = (u*0.50)
    sur50 = u50 + (u50*(20/100))
    print(f'For {u} units your Electricity Bill will be Rs {sur50}')
elif(u>50 and u<=150):
    u1 = u-50
    u2 = u - u1
    u50 = u2*0.50
    u100 = u1*0.75
    uf100 = u50 + u100
    sur100 = uf100 + (uf100*(20/100))
    print(f'For {u} units your Electricity Bill will be Rs {sur100}')

elif(u>150 and u <=250):
    u1 = u - 150
    u2 = u - u1
    u3 = u2 - 50
    u4 = u2 - 100
    u50 = u4*0.50
    u100 = u3*0.75
    u250 = u1*1.20
    uf250 = u50 + u100 +u250
    sur250 = uf250 + (uf250*(20/100)) 
    print(f'For {u} units your Electricity Bill will be Rs {sur250}')
else:
    u251= u*1.50
    uf251= u251 + (u251*(20/100))
    print(f'For {u} units your Electricity Bill will be Rs {uf251}')



    



