# Traversing the List i.e Accesing the each element present in list
li = [10,20,30,40,50,60]

#method 1
# for ele in li:
#     print(ele)

# Method 2

for ind in range(0, len(li)): # Here we will not do like len()-1 because in for loop by default give len()-1 value
    
    print(ind,'=',li[ind])
