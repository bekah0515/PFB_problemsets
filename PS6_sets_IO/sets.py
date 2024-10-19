#!/usr/bin/env python3

#make sets
set1 = {'3','14','15','9','26','5','35','9'}
set2 = {'60','22','14','0','9','9'}

print(set1)
print(set2)

#find intersection
intersection = set1 & set2
print(f'Interesection: {intersection}')

#find difference
difference = set1 - set2
print(f'Difference: {difference}')

#find union
union = set1 | set2
print(f'Union: {union}')

#find symetrical difference
symdiff = set1 ^ set2
print(f'Symmetrical difference: {symdiff}')

