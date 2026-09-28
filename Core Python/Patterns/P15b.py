'''
        *   
      *   *   
    *   *   *   
  *   *   *   *   
*   *   *   *   * 

'''




for i in range(1,6):
    for j in range(1, 6-i): 
        print(' ' , end=' ')
    for j in range(1, i+1):
        print('*  ', end=' ') # here we add spaces after star 
    print()