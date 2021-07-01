import os
from os import listdir

text = []
location = input("choose dir: ")
os.chdir(location)

print("dir: " + os.getcwd())
for item in listdir(os.path.join(location)):
    print(" - " + item)
f = input("Enter document that you want to scan: ")

with open(f, "r", encoding="utf-8") as file:
    try:
        text = file.read()
        text = text.split(" ")
        text = list(filter(None, text))
    except Exception as e:
        print(str(e))

    print("\n\nword count = " + str(len(text)))