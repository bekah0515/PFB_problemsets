#!/usr/bin/env python3
import sys

#assign command line parameters
myname = sys.argv[1]
myfavcolor = sys.argv[2]
myfavactivity = sys.argv[3]
myfavanimal = sys.argv[4]

#print a message to the screen
print(f"My name is {myname}, my favorite color is {myfavcolor}, my favorite activity is {myfavactivity}, and my favorite animal is {myfavanimal}")

#print a list of messages to the screen
print("My name:", myname)
print("My favorite color:", myfavcolor)
print("My favorite activity:", myfavactivity)
print("My favorite animal:", myfavanimal)

#print a string of messages to the screen
print("My name:" + myname + " My favorite color:" + myfavcolor + " My favorite activity:" + myfavactivity + " My favorite animal:" + myfavanimal)

#print a string of messages to the screen using commas
print("My name:", myname, " My favorite color:", myfavcolor, " My favorite activity:", myfavactivity, " My favorite animal:", myfavanimal)

