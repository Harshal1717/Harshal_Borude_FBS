# Return Function

def addition():
    num1 = int(input("Enter number 1: "))
    num2 = int(input('Enter  number 2:'))

    sum = num1 + num2
    return sum # return keywaord throws out from function.
res = addition() # Here first RHS execute first then LHS . Every time RHS first n then LHS
print('Addtion pf 2 bumbers are ', res)
