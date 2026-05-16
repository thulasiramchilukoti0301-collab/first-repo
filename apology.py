import pyttsx3

engine = pyttsx3.init()

name = input("Enter name: ")
reason = input("What did you do? ")

message = f"{name}, I am sorry for {reason}. Please forgive me."

print(message)
engine.say(message)
engine.runAndWait()