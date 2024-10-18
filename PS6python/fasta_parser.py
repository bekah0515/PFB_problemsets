#!/usr/bin/env python3

fasta_dict={}
#gene_id=""

#open file and split id with sequence and store in dictionary 
with open('Python_06.fasta','r') as seq_read:
  for line in seq_read:
    #get rid of new lines
    line=line.rstrip()
    if line.startswith(">"):
      gene_id=line.lstrip(">")    
      fasta_dict[gene_id]='' 
    else:
      fasta_dict[gene_id] += line 
print(fasta_dict)
  
