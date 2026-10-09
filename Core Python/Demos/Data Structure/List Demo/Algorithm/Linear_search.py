# Linear search Algorithm
def linearSearch(li,ele_search):
    for ind in range(0,len(li)):
        if(ele_search == li[ind]):
            return ind
    else:
        return -1 
# we -1 for giving output in int format . we dont use negative  indexing here so that we can use -1
#---------------Whatever changes require into display of result , done by below code not above one.------------------

li = [10,45,23,1,2,367,89,34]
ele = int(input('Enter a element to Search in List: '))
res = linearSearch(li,ele)
if(res != -1):
    print(f'Elment {ele} is present in the List at index {res}.')
else:
     print(f'Elment {ele} is not  present in the List.')


'''
Time Complexcity
   # Best case : O(1)
   # Worst case : O(n)
   # Average case : O(n)

   The reason behind of worstv and average is same is that there avrage is close to worstv do it by ypurself u will know





'''
