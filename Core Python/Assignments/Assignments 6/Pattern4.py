'''
A 
A B 
A B C 
A B C D 
A B C D E
logic is so simple here, column 

'''
li = ['A','B','C','D','E']
for i in range(0,5):
    for j in range(0,i+1):
        print(li[j], end=' ')
    print()
