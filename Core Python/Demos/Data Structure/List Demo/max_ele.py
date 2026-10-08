# Find Largest element in List

li = [10,40,5,90,100,165,30,180,40]

max = li[0] #Assign 0th element to max for comparing withb others

for ind in range(1, len(li)):
    if(li[ind] > max):   # we check each element from list and compare it with next element ifit is max then we stored in max if not move towords next element
        max = li[ind]
print('Largest element in List is',max)