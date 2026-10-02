# To pass multiple paramteres in function
# Mention 1 Asterisk befire parameter name in function definition
# Values are stored in tuple
# Use for loop to iterate values individually from tuple  
def add(*data):
    sum=0
    for val in data:
        sum+=val
    return sum
    
res= add(10,20,22,304,45,67,54,32,13,56,)
print(res)