#!/usr/bin/env python3

import sys, os, re, statistics

#number of contigs in fil
contig_dict = {}
fasta_filename = sys.argv[1]
def contig_dict_from_fasta_file(fasta_filename):
    contig_dict = {}
    fasta_filename = sys.argv[1]

    with open(fasta_filename, 'r') as fasta_file:
        for line in fasta_file:
            line = line.rstrip()
            if line.startswith(">"):
                for match in re.finditer(r"(^>\S+.*)",line):
                    id = match.group(1)
                    gene_id = id.lstrip(">")
                    contig_dict[gene_id] = ''
            else:
                contig_dict[gene_id] += line
        return contig_dict

print(f'total number of contigs in the file: {len(contig_dict_from_fasta_file(sys.argv[1]).keys())}')
#make a list of sequences
contig_dict = contig_dict_from_fasta_file(fasta_filename)
seq_list = list(contig_dict.values())
#print(seq_list[0:2])
#print(len(seq_list))

#count length of each sequence
seq_count_list = []
for seq in seq_list:
    seq_count_list.append(len(seq))
#print(seq_count_list) 
#print(len(seq_count))
total_contig_length = sum(seq_count_list)
shortest_contig = min(seq_count_list)
longest_contig = max(seq_count_list)
print(f'Total contig length:{total_contig_length}')
print(f'Shortest contig:{shortest_contig}')
print(f'Longest contig:{longest_contig}')

#calculating N50, where 50% of contigs are larger or equal to the N50 value
sorted_seq_count_list = sorted(seq_count_list, reverse = True)
half_length = total_contig_length/2
counter = 0
for count in sorted_seq_count_list:
    if counter < half_length:
        counter +=count
        if counter >= half_length:
            n50 = count
            print(f'N50: {n50}')
#print(counter)

#n50 = statistics.median(sorted_seq_count_list)
#print(f'N50 is: {n50}')
#print(sorted_seq_count_list)

#get index of n50
index_of_n50 = sorted_seq_count_list.index(n50)
#print(index_of_n50)
#get contigs up to index of n50
upper50 = sorted_seq_count_list[:index_of_n50 + 1]
l50 = len(upper50)
print(f'L50: {l50}')
upper49 = sorted_seq_count_list[:index_of_n50]
print("upper49:", sum(upper49))