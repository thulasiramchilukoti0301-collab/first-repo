name = input("What's Your Name? ")
file = open("names.txt","a")  # open the file in append mode so that we don't overwrite existing names
file.write(name + "\n") 
file.close()