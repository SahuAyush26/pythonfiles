file = open("file.txt", "r")
print(file.read())
file.close()

print("")

f = open("newfile.txt", "r")
# x = f.readlines()
# print(x, type(x))

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()
# line5 = f.readline()

# print(line1, line2, line3, line4, line5, type(line1))

line = f.readline()

while(line != ""):
    print(line, end = "")
    line = f.readline()

f.close()




