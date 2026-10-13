def selectionSort(li):
    size = len(li)
    for i in range(0,size-1):  # In Selection sort we select 1 elememt i.e 0th insdex elemet treat as min index too then compare it with rmaining elemenst if we find less that that at thatvindex we swap it
        min_ind = i
        for j in range(i+1,size):
            if(li[j]< li[min_ind]):
                min_ind = j
        li[i],li[min_ind]=li[min_ind],li[i]

li=[30,20,10,40,50,20,40,30]
print('Before Selection Sort:',li)
selectionSort(li)
print('After Selection Sort',li)