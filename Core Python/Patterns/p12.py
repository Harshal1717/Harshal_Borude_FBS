for i in range(1,6):
    for j in range(1,6):
        if(i==1):
            print(6-j, end=' ')
        elif(i+j==6):
            print(1, end=' ')
        elif(j==1):
            print(6-i, end=' ')
        else:
            print(' ' ,end=' ')
    print()
    