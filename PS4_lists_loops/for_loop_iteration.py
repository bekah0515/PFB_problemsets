#!/usr/bin/env python3

sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

#iterate my sequences
for seq in sequences:
  print(sequences.index(seq), len(seq), seq, sep='\t')
  
