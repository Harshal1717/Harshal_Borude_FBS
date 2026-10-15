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
print(li.index(40))#Return index of element . If wrong then give error as value error
print(li)
li.insert(1,90) # li.insert(index,element) here we can insert elemnt at specific index 
print(li)
li.pop(3)# here we delete element at sepcific index . For pop() method we gibve index
print(li)
li.remove(50) # here we directily give elememnt whoch is need to be delete from list
print(li)
li.reverse()# it reverse the list
print(li)
li.sort() # It sorted the list in ascending order
print(li)
li.sort(reverse=True) #It sortef list in Descending order
print(li)