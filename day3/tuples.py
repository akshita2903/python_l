#tuple
t1=(1,2,3,4)
print(t1)
# t[0]=5 -> updation not allowed ,tuples are immutable

t2=(1,) #tuple with only one element is declare as "(a,)" otherwise it will be like normal assignment to varibale such as (a)


x=t1.count(2)
print(x)

search=t1.index(4) #return first index of this value