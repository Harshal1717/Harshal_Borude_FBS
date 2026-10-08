# Find 2nd Largest elementv present in list

li = [10,30,5,60,20,90,100,150,480]

max = li[0]

smax = 0

for ind in range(1,len(li)):
    if(li[ind]> max):
        smax = max
        max = li[ind]
    elif(li[ind]> smax):
        smax = li[ind]
print('Largest element is',max)
print('2nd Largest elkement is', smax)

    

