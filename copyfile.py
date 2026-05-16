f1 = open("file.txt", "r")
f2 = open("copy.txt", "w")

data = f1.read()
f2.write(data)

f1.close()
f2.close()

print("File copied successfully")