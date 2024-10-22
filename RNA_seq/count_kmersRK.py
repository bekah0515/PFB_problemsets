#!/usr/bin/env python3

import os, sys

from sequence_to_kmer_list import *
from fastq_file_to_sequence_list import *

kmer_list= ['GTGACA','GTGACA','GTGACA','GTGACA', 'TGACAA', 'TGACAA', 'GACAAT', 'ACAATG', 'CAATGT', 'AATGTG', 'ATGTGC', 'TGTGCC', 'GTGCCC', 'TGCCCT', 'GCCCTG', 'CCCTGT', 'CCTGTT', 'CTGTTG','CTGTTG','CTGTTG', 'TGTTGT', 'GTTGTT']
kmer_count_dict = {}
for kmer in kmer_list:
    if kmer not in kmer_count_dict:
        kmer_count_dict[kmer] = 1
    else:
        kmer_count_dict[kmer] += 1

#print(kmer_count_dict)
#def sort_func(x):
#    return kmer_count_dict[x]

#print out tuples
#sort_func = lambda x : x[1]
#sorted_dict = sorted(kmer_count_dict.items(), key=sort_func, reverse = True)
#print(sorted_dict)

#print out list of key sorted
sort_func = lambda x: kmer_count_dict[x]
sorted_dict = sorted(kmer_count_dict, key=sort_func, reverse = True)
