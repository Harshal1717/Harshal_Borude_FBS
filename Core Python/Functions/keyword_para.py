#To neglect positional parameter concept.
#Assign value to parameter in function call.
#Name of parameter in function definition and function call should same
# Flow from right to left
def emp(id,name,sal,dept):
    return f'ID:{id}\nNAME:{name}\nSALARY:{sal}\nDEPARTMENT:{dept}'#we can use this technique too.
res = emp(name='Harshal',sal=50000,id=101,dept='Backend Engineering')#here we neglect Positional Parameter concept.
print(res)