# Print like 1 2 3 4 and 1 1 1 1 1 
for i in range(1, 6):  # for similar values in each row we print i
    for j in range(1, 6): # for different values in each row we print j
        print(i, end=' ') # i u can change it to j and see
    print() # it will print like  
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5