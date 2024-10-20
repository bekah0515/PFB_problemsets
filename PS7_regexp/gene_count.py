#!/usr/bin/env python3
import re

fasta_dict = {}

#get fasta file and turn it into lines
with open('Python_08.fasta','r') as ofh:
    for line in ofh:
        line = line.rstrip()
        if line.startswith(">"): 
          geneid = re.search(r"(^>\S+)",line)
          geneid = geneid.group(1)
          geneid = geneid.lstrip(">")
          if geneid not in fasta_dict:
            fasta_dict[geneid] = {}
            sequence = ''
        else:
          sequence = sequence + line
          #print(sequence)   
          g_count = sequence.count("G")
          fasta_dict[geneid]["Gs"]=g_count
          a_count = sequence.count("A")
          fasta_dict[geneid]["As"]=a_count
          t_count = sequence.count("T")
          fasta_dict[geneid]["Ts"]=t_count
          c_count = sequence.count("C")
          fasta_dict[geneid]["Cs"]=c_count
    for geneid in fasta_dict:
      print(f'{geneid}\tGs:{fasta_dict[geneid]['Gs']}\tTs:{fasta_dict[geneid]['Ts']}\tCs:{fasta_dict[geneid]['Cs']}\tAs:{fasta_dict[geneid]['As']}')
