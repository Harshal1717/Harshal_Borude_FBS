def conquer(li,start,mid,end):
    left=start
    right=mid+1
    temp=[] # we are taking temprory list because we have store each element intoi somethinmg after comparing 
    while(left<=mid and right<=end): # giving conditions for divided lists that one is left list other is right list
        if(li[left]<li[right]):
            temp.append(li[left])
            left+=1
        else:
            temp.append(li[right])
            right+=1
    while(left<=mid):
            temp.append(li[left])
            left+=1
    while(right<=end):
         temp.append(li[right])
         right+=1
    for k in range(len(temp)):
         li[start+k]=temp[k]

def divide(li,start,end):
    if(start>=end):
        return
    mid=(start+end)//2
    divide(li,start,mid)
    divide(li,mid+1,end) # till this we divide list into halves 
    conquer(li,start,mid,end) # this is conquer function which are sorting and merging our list into one
li=[21,30,50,38,1,2,45]
print('Before Sorting:', li)
divide(li,0,len(li)-1)
print('After Sorting:',li)