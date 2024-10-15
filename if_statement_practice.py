#!/usr/bin/env python3

#assign value to my variable
mynumber = 605

#Test if my number is positive or negative
if mynumber < 0:
  print(mynumber, 'is negative')
elif mynumber > 0:
  print(mynumber, 'is positive')
  if mynumber < 50:
    print(mynumber,'is smaller than 50')
  if mynumber > 50:
    if mynumber%3 == 0:
      print(mynumber, 'is greater than 50 and divisible by 3')
  if mynumber%2 == 0:
    print(mynumber, 'is even')
  if mynumber%2 != 0:
    print(mynumber, 'is odd')
else:
  print('my number is 0')

