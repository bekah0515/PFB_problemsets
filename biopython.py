#!/usr/bin/env python3
import sys
from Bio import SeqIO
from Bio.Seq import Seq

#input file
fasta_file = sys.argv[1]

#make a list of all fasta seq
records_list = list(SeqIO.parse(fasta_file, 'fasta'))

#calculate total number of sequences/records in the fasta file
total_num_seq = len(records_list)
print(f'total number of sequences: {total_num_seq}')

#make a list of sequences
seq_list = []
seq_count = []
for seq_record in records_list:
    seq_list.append(str(seq_record.seq))
    #print(seq_list)

#count length of each sequence
for seq in seq_list:
    seq_count.append(len(seq))

#add length of each sequence to get total nt in the file
total_nt_count = sum(seq_count)
print(f'total number of nt: {total_nt_count}')

#calculate average length of records in the fasta file
average_length = total_nt_count/total_num_seq
print(f'average length: {average_length}')

#spit out shortest and longest sequence length
max_seq_len = max(seq_count)
min_seq_len = min(seq_count)
print(f'shortest length: {min_seq_len}')
print(f'longest length: {max_seq_len}')

#GC content 
gc_content_list = []
for seq in seq_list: 
    gc_count = seq.count("G") + seq.count("C")
    gc_content = gc_count/len(seq)*100
    gc_content_list.append(gc_content)

total_gc_content = sum(gc_content_list)
average_gc_content = total_gc_content/total_num_seq
print(f'average GC content: {average_gc_content:.3}%')
print(f'highest GC content: {max(gc_content_list):.3}%')
print(f'lowest GC content: {min(gc_content_list):.3}%')

    
    


#seq_record in SeqIO.parse(fasta_file, "fasta"):
 #   record_dict = SeqIO.index()
  #  print('ID', seq_record.id)
   # print('Sequence', seq_record.seq)
    #print('Length', len(seq_record))