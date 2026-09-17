# Write a program to input any alphabet and check whether it is vowel or consonant. 
var = input('Enter Alphabet Only :')
if(var == 'a' or var == 'e' or var == 'i' or var == 'o' or var == 'u'):
    print(f'Given Alphabet {var} is a Vowel.')
else:
    print(f'Given Alphabet {var} is a Consonant. ')