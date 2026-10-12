def binarySearch(li,search_ele):
    
    beg = 0
    end = len(li)-1
    
    while(beg<=end):
        print('beg:',beg)
        print('end:',end)
        mid = (beg+end)//2
        print('mid:',mid)
        if(search_ele == li[mid]):
            return mid
           
        elif(search_ele < li[mid]):
            end = mid -1 
            
        else:
            beg = mid+1
    return -1

li = [10,20,30,40,50,60]
ele = int(input('Enter a element to search:'))
res = binarySearch(li,ele)
if(res!=-1):
    print(f'Element found at Index {res} in th List')
else:
    print(f'Element does not found in the List')


    

 
 
       