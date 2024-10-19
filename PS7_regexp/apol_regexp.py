#!/usr/bin/env python3

import re

compiledseq = {}
#open file and find all ApoI cut sites
with open('Python_07_ApoI.fasta','r') as fasta_file:
  for line in fasta_file:
    line=line.rstrip()
    cut_site = re.sub(r"([AG])(AATT[CT])", r"\1^\2", line)
    if line.startswith(">"):
      seq = line.lstrip(">")
      compiledseq[seq] = ""
    else:
      compiledseq[seq] += cut_site
  print(compiledseq)
  
  #cut the sequence at cutsites 
  sequence = compiledseq[seq]
  fragment = sequence.split("^")
  sorted_fragment = sorted(fragment, key=len)+
  print(sorted_fragment)

