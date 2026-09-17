#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle. 
s1 = int(input('Enter 1st Side of Trianle:'))
s2 = int(input('Enter 2nd Side of Trianle:'))
s3 = int(input('Enter 3rd Side of Trianle:'))

if(s1 == s2 == s3):
    print('Given Traingle is an Equilateral Triangle.')
elif(s1 == s2 or s1 == s3 or s2 == s3):
    print('Given Triangle is an Isosceles Trianle.')
else:
    print('Given Triangle is Scalene Triangle.')