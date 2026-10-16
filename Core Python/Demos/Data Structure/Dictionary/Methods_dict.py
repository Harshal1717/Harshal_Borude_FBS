di = {1:'Python',2:'Java',3:'CPP'}
print(di)
#di.clear() # Delete all the items from dictionary
di2 = di.copy() # Copy all the items from di and add into di2
print(di2)
print(di.get(4)) #It will print none
print(di.get(4, 'key is not present')) # It will print key is not present
print(di.get(2))# It will print Java
print(di.items()) # It will print all the items from dictionary
print(di.keys()) # It will print all the keys present in dictinary
#di.pop(2)# It wwill delete key value pair pof key 2
di.popitem()#It will delete last key-value pair form dictinary
print(di)
di.update({3:'PHP',4:'Ruby',5:'R'})
print(di)