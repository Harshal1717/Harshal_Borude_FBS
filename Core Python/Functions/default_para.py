# To make parameter optional
# Assign value to parameter in function definition
# If we pass value to default parameter , ut takes passed value
# If we dont pass value to default para,it takes default value
# Flow of assigning  default value in function definition is right to left instead of left to right

def emp(id,name,sal,dept='Computer'): #ithe jr default value assign krychi asel tr right to left krne due to positional parameter
    print('ID:', id)
    print('NAME:', name)
    print('SALARY:',sal)
    print('DEPARTMENT', dept)
    print('---------------------')
emp(101,'Harshal',50000)
emp(102,'Swapnil',50000,'Information Technology')
