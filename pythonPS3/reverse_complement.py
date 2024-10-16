#!/usr/bin/env python3

#set dna variable
dna = 'ATGCAGGGGAAACATGATTCAGGAC'

#complement my seq
complement_dna = dna.replace('A','t').replace('C','g').replace('G','c').replace('T','a')

#uppercase my seq and reverse it. 
complement_dna = complement_dna.upper()
print(f"Original sequence:  5' {dna} 3'")
print(f"Complement:         5' {complement_dna} 3'")
print(f"Reverse Complement: 5' {complement_dna[::-1]} 3'")

