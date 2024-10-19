#!/usr/bin/env python3

numbers = [101,2,15,22,95,33,2,27,72,15,52]

#sort my list from smallest to greatest
numbers.sort()
print(numbers)
for number in numbers:
  print(number)
  
#sum of evens and sum of odds in my list
even=0
odd=0
for number in numbers:
  if number%2 == 0:   
    even += number
for number in numbers:
  if number%2 == 1:
    odd += number

print(f'sum of even numbers: {even}')
print(f'sum of odd numbers: {odd}')

