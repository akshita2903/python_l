text="Appended text"

# with open("file1.txt","w") as f:
#      f.write(text)
#OR

fp=open("file1.txt","w") #removes all content from file and add goven text
# fp.writelines(text)
# fp.write("Hello")
fp.close()

f=open("file1.txt","r")
files=f.read()
print(files)

fp=open("file1.txt","a") #original content + text
fp.write(text)

