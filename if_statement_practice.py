#!/usr/bin/env python3
import sys

#assign value to my variable and make it an integer
mynumber = int(sys.argv[1])

#assess the number
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

