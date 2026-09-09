# Variables are nothing but 
# * Identifier for values 
# Has ability to identify diff  values
# placeholder for memory location 
# Rules for Variables to declare
# Can contains alpha , digits, underscore
# Cant contains space
# cant contains symbol except underscore
#cant use keyword as variables as variables
# cant start with digit
num1 = 12
num_1 = 10
print(num1)
print(num_1)
#num 1 = 10 error
#1num = 10 error
# num@ = 28 error 
# if = 10 error

#KEYWORD TOKENS
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

## DATATYPES 
# numeric
var = 10 
var = 3.14


var = 10 + 5j
print(var)
#print(type(var))  ## here is garbage collection conept works

# TEXT 
#  string str
var = "Harshal borude" 
var  = 'Harshal Borude'
var = ''' Harshal '''
'''hi hello world here triple used for **multilinne comments but its not actually comments **''' 

# SEQUENTIAL DATATYPES
# LIST
var = [10, 20 ,30 ,40]

# TUPLE
var = (10, 20, 30, 40)

#range()
var = range(1, 41)

### SET type
#set
var = {10, 20, 30 ,40 }

#Frozenset
var = frozenset({10,20,30,40})

### Mapping 
#Dictinoary
var = {1:'java', 2: 'python', 3:'c++'} #it is nothing but key value pair 

###Other
#Boolean
var = True

#Nonetype

var = None

print(type(var));
    