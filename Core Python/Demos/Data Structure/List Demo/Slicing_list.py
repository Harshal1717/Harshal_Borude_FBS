li =[10,20,30,40,50,60,70,80,90,100]
res = li[1:6] # It is nothing but slicing . It is similar to range() function
res= li[3:9] # li[start,stop,step] here step is by default +1
res = li[1:8:2]  # here we are giving step +2 this is we get list within eange 1,8 with difference of 2 elements
res = li[1:8:3]  # +3
res = li[8:1:-1] # here we are printing list reverse side . thats why we are giving -1
res = li[0:6] # start from 0 th index
res = li[:6] # print similar result to above one i.e 0:6
res = li[4:20] # Here end 20 is not exist still we get list till end. Slicing never give error
res = li[4:] # Similar result as above one
res= li[::] # print full list from start to end
res= li[:] # same as above
res = li[::-1]# Reverse the list. -1 will reverse the list.

print(res)