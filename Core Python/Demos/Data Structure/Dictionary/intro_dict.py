#1. Structure {}
dict = {1:'Python',2:'Java',3:'JavaScript'}
print(dict)
print(type(dict))
#2 Data is Hetereogenous .
dict =  {1:'Python',2:'Java',3:'JavaScript','year':2026,'age':22}
print(dict)
#3. Ordered

#4 key:Immutable and Value: Mutable , size:Mutable
dict['year'] = 2027 # Update the value
dict['age'] = 25 # Update the vealue
dict['Height'] = 160 # Is is not present in dictionary so it will add in the edne og dictionary
print(dict)

# Key : Unique and value : Duplication Allowed
dict2 =dict =  {1:'Python',2:'Java',3:'JavaScript','year':2026,1:'PHP'}
print(dict2)# It will print 1:PHP not Pyhton becase of Over riding