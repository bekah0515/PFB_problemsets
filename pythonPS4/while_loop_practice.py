#!/usr/bin/env python3

#this while loop will print out numbers 1 to 100
count = 1
while count<101:
  print(count)
  count+=1

#this while loop will calcalate 1000!

n = 1
product = 1
while n < 1000:
  product *= n
  n += 1

print(f'factorial is {product}')
print('Done!')

