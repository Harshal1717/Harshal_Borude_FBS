# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input('Enter gender (M/F):')
age = int(input('Enter age: '))

if(gender == 'M'):
    if(age >= 21):
        print('Person is elgible for Marriage')
    else:
        print('Person is not eligible for Marriage')
else:
    if(age >=18):
        print('Girl is eligible for Marriage')
    else:
        print('Girl is not eligible for Marriage')