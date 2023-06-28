list1=[2,5,8,1,9,10]
list2=["Ak","py","bag","jsh","qjd","qje"] #get sorted alphabetically

#  1:-Sorting
list1.sort() #in ascending order
print(list1)
list2.sort()
print(list2)

#reverse
list1.reverse()
print(list1)

#append- adding at the last+1 index
list2.append("jalebi")
print(list2)

#insert(index,value) -add value at index 'index' and shifts the remaining to right
list1.insert(2,67)
print(list1)

#list.pop(index) : by default index is set t -1 instead of list.len-1
list1.pop()
print(list1,len(list1))

#list.remove(element) removes element and not from index

