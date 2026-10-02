# To pass multiple values with ,meaning
# Mention 2 Asterisk symbols before parameter name in function definition
# Values and meaning stored in Dictinory Format
# Use for loop on dict.items() to Itearte data 
def emp(**data):
    for key,val in data.items():
        print(key,':',val)
emp(id=101, name='Harshal',salary=50000,dept='IT')
print('----------------------')
emp(id=102,name='ABD', salary=40000, dept='ECE')