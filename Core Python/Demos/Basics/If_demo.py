### IF syntax
#if(condition):
    #Block of code
    #line1
    #line
# If condition is true then and then only block of code will execute
# If condition is false then  block of code willl not execute

num = int(input('Enter a number:'))
if(num > 0):
    print(f'The number {num} is Positive')