#!/usr/bin/env python3
import sys

min_num = int(sys.argv[1])
max_num = int(sys.argv[2])

#use list comprehension to print out only the odd numbers
odd_numbers = [print(value) for value in range(min_num,max_num+1) if value%2 == 1]


