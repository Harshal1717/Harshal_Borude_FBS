#With passing Parameter and with Returning Value
# Remember num1 n num2 in funtion parameter and num1 n num2 in assigning are two different u can change n still got right result
def addition(num1,num2):
    sum = num1+num2
    return sum
num1= int(input('Enter number1: '))
num2=int(input('Enter number2: '))
res = addition(num1,num2)

print('Addition',res)

