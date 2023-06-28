a="Parrot's" # single within double
b='Totta"s' #double quotes witin single
c=''' Your name "asd'
       s" '''
# print(a,b,c)
# print(a[3])
# a[3]="g" ->string are immutable
x="Parrot"
#print(x[0:4]," ")
#print(      x[0:],x[-6: ]) #both are same

#skipppping in Slice
y="youareGood"
#print(y[0::2]) #x[start_index:end_index:kitne charcater skip krwane hai(by defaut 0)]

#STring functions
z="About you is ready to go"
# print(len(z)) #count spaces also
# print(z.endswith("goes")," ",z.endswith("go"))
# print(z.count('o'))
# print(z.capitalize()) #capitilize first letter
print(z.find("you")," ",z.find("yours")) #giv first index of occurence ,if it doesnot exist it gives -1
print(z.replace("o","s")) # replace(old,new
