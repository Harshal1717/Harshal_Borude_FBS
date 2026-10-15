# TUPLE #
#1. Tuple Structure  In tuple the ',' is important.
tu = (10,20,30,40)
tu1=(10,) # With help of ' , 'we cand convert type int to tuple
tu2 = 10, 20 , 30, 40 # This is also we can get tuple .
print(tu)
print(type(tu))
print(type(tu1))
print(type(tu2))

# 2 Type of Data Tuple Conmtains : Heterogenous
tu3 = (10,20,30,3.145,'abc','abcdef')
print(tu3)

# 3 Sequence : Ordered

tu4 = (10,20,30,50,'abc')
print(tu4)

# 4 Immutrable
# tu[0] = 30 # It will give Error

# 5  Duplication is Allowed
tu5 = (10,10,10,30,20,50,'abc','abc')
print(tu5)
