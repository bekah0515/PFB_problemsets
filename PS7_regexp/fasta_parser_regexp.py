#!/usr/bin/env python3

import re

fasta_dict={}
#gene_id=""

#open file and split id with sequence and store in dictionary
with open('Python_07.fasta','r') as fasta_file:
  for line in fasta_file:
    line=line.rstrip()
    if line.startswith(">"):
      for match in re.finditer(r"(^>\S+.*)",line):
        id= match.group(1)
        gene_id = id.lstrip(">")
        fasta_dict[gene_id]=''
    else:
      fasta_dict[gene_id] += line
print(fasta_dict)
