#Write a program to input all sides of a triangle and check whether triangle is valid or not.
s1 = int(input('Enter 1st Side of Trianle:'))
s2 = int(input('Enter 2nd Side of Trianle:'))
s3 = int(input('Enter 3rd Side of Trianle:'))
if(s1+s2 > s3 and s1+s3 > s2 and s2+s3 > s1):
    print(f'Given sides {s1},{s2},{s3} state that the Triangle is Valid.')
else:
    print(f'Given sides {s1},{s2},{s3} state that the Triangle is Invalid.')

    
 