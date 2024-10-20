#!/usr/bin/env python3

import sys
import re

seq_file = sys.argv[1]
n = int(sys.argv[2])
fasta_dict = {}
def split_seq_every_n(seq):
    with open(sys.argv[1],"r") as ofh:
        for line in ofh:
            line = line.rstrip()
            if line.startswith(">"):
              geneid = line.lstrip(">")
              fasta_dict[geneid]=''
              seq_list = []
              sequence = ''
            if not line.startswith(">"):
              sequence += line
              #print(sequence)
              seq_list= [sequence[i:i+n] for i in range(0, len(sequence), n)]
              #print(seq_list)
              seq_output= ("\n".join(seq_list))
              fasta_dict[geneid]=seq_output
              #print(seq_output)
    return fasta_dict
print(split_seq_every_n(seq_file)) #this will print my dict
with open("sequence.fasta","w") as wfh:
  for geneid in fasta_dict:
    wfh.write(f'\n>{geneid}\n{fasta_dict[geneid]}')
    print(f'\n>{geneid}\n{fasta_dict[geneid]}')


#print('length:', len('CCGCAAAGTTCTGCGCGACAACATTCAGGGCATCACCAAGCCCGCCATCCGACGCCTGGC'))
