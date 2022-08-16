import os

#print(os.getcwd())
os.mkdir("taskdir")
os.chdir("taskdir")

text = "line1\nline2\nline3"
f = open("task1.txt", "w")
f.writelines(text)

f = open("task1.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)

print("\n\n")
#-------------------------------
for i in range(len(lines)):
    if(i!=0):
        print(lines[i])

f.close()

