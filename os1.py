from microbit import *
import os

#write to the file
with open('myname.txt', 'w') as myFile:
    myFile.write("My name is SNRU.")

#a listing of the file directory
print(os.listdir())

#read the file and  print the content
with open('myname.txt', 'r') as myFile:
    a = myFile.read()
    print(a)
    display.scroll(a)
