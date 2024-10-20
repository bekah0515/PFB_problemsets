#!/usr/bin/env python3

make_gc_rn = subprocess.run(['ls','-l'], stderr=errormessage.txt)
dna_seq = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'

if make_gc_rn.returncode !=0
  print("Failed")
  exit(5) #denote 5 as error code for wrong type of seq

def gc_count(dna):
  c_count = dna.count('C')
  g_count = dna.count('G')
  dna_len = len(dna)
  gc_content = (c_count + g_count) / dna_len
  return gc_content

def reverse_complement(dna):
  compdna = dna.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
  revcompdna = compdna[::-1]
  return revcompdna.upper()

dna_gc = gc_count(dna_seq)
print(f'The GC content is {dna_gc:.2%} GC.')

revcomp = reverse_complement(dna_seq)
print(f"The reverse complement is 5' {revcomp} 3'.")