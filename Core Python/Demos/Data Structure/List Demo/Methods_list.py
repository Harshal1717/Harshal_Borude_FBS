li = [10,20,30,40,50,60]
li.append(70) # it is used to add elemnts in list
#li.clear() # It is used to clear all the elemnts form list means give empty list
#Deepcopy and ShallowCopy (nested list)
li2 = li.copy()
# li[5][0] = 80
print(li)
print(li2)
print(li.count(10)) # It will give count of how many times that elements appear in given list
li.extend([70,80,90]) # it is used to add multiple elements in list.
print(li)