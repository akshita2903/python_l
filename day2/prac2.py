#print name with good,name is input
# name=input("Enter name")
# print("Good "+name)

letter=''' Dear <|Name|>,
You are selected!

Date: <|DATE|>
'''
print("Initial Letter",letter,"\n")
name=input("Enter name\n")
date=input("Enter date")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|DATE|>",date)
print("\nLetter for you\n",letter)

