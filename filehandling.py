
f = open("demo.txt","a")
f.write("Will this line be added")
f.close()

f = open("demo.txt")

print( f.read())


