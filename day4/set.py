set1={1,2,2,3,4}
print(type(set1))
print() #yaha pe two time 2 aaya hai but print me o/p is {1,2,3,4}=>ignores repetitve item

empty_set=set()

#add items to set
# empty_set.add(set1) #can not add set
empty_set.add(2)
empty_set.add(8)
empty_set.add(9)
empty_set.add(10)
empty_set.add(15)
empty_set.add("Apple")
empty_set.add("Banana")
empty_set.add("hleo")

#list can not be added
# empty_set.add([5,6,7]) 
empty_set.add((2,3,4))

#dictionary can not be added
# empty_set.add({"key1":"value2"})

print("Before removal ", empty_set)
#remove a specific value(provided by user)
empty_set.remove(9)
# print("After removal ",empty_set)

#remove a random value
empty_set.pop()
print("After removal ",empty_set)
