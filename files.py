
f = open("file.txt","a")

f.write("There is this file")

f = open("file.txt")
print(f.read())

f.close()