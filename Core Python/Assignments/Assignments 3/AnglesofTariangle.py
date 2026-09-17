#Write a program to input angles of a triangle and check whether triangle is valid or not.
a1 = int(input('Enter 1st angle of a Triangle: ')) 
a2 = int(input('Enter 2nd angle of a Triangle: ')) 
a3 = int(input('Enter 3rd angle of a Triangle: ')) 

sum = a1+a2+a3
if(sum == 180):
    print(f'Given angles {a1},{a2},{a3} state that the Triangle is Valid.')
else:
    print(f'Given angles {a1},{a2},{a3} state that the Triangle is Invalid.')