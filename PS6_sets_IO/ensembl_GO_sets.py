#!/usr/bin/env python3

genes={}
with open('ferret_all_genes.tsv','r') as all_genes, open('ferret_stemcellproliferation_genes.tsv','r') as stemcellprolif_genes, open('ferret_pigmentation_genes.tsv','r') as pigment_genes:
  for line in all_genes:
    line = line.rstrip()
    all_genes = set(line)
    print(all_genes)

