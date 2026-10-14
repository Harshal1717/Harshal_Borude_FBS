li = [10,20,[30,[50,60,70,[80,90]],100],110,120] # This is nothing but nested list. i.e list udner list

print(len(li)) # it will give 5 . the reason is here it treated each list as single elemnt so 10,20,30to100,110,120
print(li[2][0]) # that is list 2nd is prsent at index 2 and index no 0 it will print 30
print(li[2][1][0]) # it will print 50 . that is in list no 2 there is another list at indedx 1 and element at index 0 is 50
print(li[2][1][3][1]) # it will print 90. that is at index 2 there is  a list then again in that at  index 1 there is another list at index 3 and in that at index 1 there is element 90.