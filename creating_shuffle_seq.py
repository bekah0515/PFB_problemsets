#!/usr/bin/env python3
import random

#assign variables
numbers = '254698'
numbers_list = list(numbers)
numbers_index = [numbers.index(number) for number in numbers]
n = len(numbers)
shuffle = 0
print(numbers_list, numbers_index, n)

#generate a random index within my sequence
for every shuffle < n:
  random_indexA = random.randrange(n)
    print(f'A: {random_indexA}')
  random_indexB = random.randrange(n)
    print(f'B: {random_indexB}')
  shuffle +=1


