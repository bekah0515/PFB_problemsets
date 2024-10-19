#!/usr/bin/env python3

seq_dict={}

#open file and split id with sequence and store in dictionary
with open('Python_06.seq.txt','r') as seq_read:
  for line in seq_read:
    line=line.rstrip()
    gene_id,seq = line.split()
    seq_dict[gene_id]=seq
  #reverse complement each line
  for gene_id in seq_dict:
    sequence = seq_dict[gene_id]
    complement = sequence.replace('A','t').replace('C','g').replace('G','c').replace('T','a')
    complement = complement.upper()
    revcomplement = complement [::-1]
    print(f"{gene_id}\t5' {revcomplement} 3'\n")

print('This is the reverse complement of every sequence.') 
