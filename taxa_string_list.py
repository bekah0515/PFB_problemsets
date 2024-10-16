#!/usr/bin/env python3

#create variable with string
taxa_string = 'sapiens : erectus : neanderthalensis'
print(taxa_string)
print(type(taxa_string))

#convert string into list
taxa_list = taxa_string.split(' : ')
print(taxa_list)
print(type(taxa_list))
print(taxa_list[1])

#sort my list alphabetically
print(f'my list sorted alphabetically: {sorted(taxa_list, key=None, reverse=False)}')

#sort my list by length
print(f'my list sorted by length: {sorted(taxa_list, key=len)}')

