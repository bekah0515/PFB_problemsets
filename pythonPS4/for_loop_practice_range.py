#!/usr/bin/env python3

# print out every number between 1 and 100.
for num in range(101):
  if num > 0:
    print(num)

#print out every number between 1 and 100 using list comprehension
numbers = [print(num) for num in range(101) if num > 0]


