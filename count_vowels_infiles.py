f = open("file.txt", "r")

content = f.read()
count = 0

for ch in content:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)

f.close()