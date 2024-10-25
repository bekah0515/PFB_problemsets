#!/usr/bin/env python3
import sys

hit_files = []
filename = sys.argv[1]
#remove newline char
hit_data = {}
#make my field headers into lists
field_str = 'qseqid sseqid percid alen mismat gaps q_start q_end s_start s_end evalue bits'
fields = field_str.split(' ')

hits_list = []
for hit_file in sys.argv[1:]:
    #open the files
    with open(hit_file,'r')as fin:
        for line in fin:
            #skip lines that start with #
            if line[0] == '#':
                continue
            #strip endline and make list of different values and make it into a dictionary by using dict(zip(key,value))
            hit_data = dict(zip(fields,line.strip('\n').split('\t')))
            #add into file that gave me this data so i know what scoring matrix it came from
            hit_data['file'] = hit_file
            hits_list.append(hit_data)
            break

#print(hit_data)
print(hits_list)
#print(hit_file)

#for hit in hits_list: 
    #print(hit)
    #print('\t'.join([hit[x] for x in ('file','percid','alen','evalue')]))


#def ssearch_file_to_dict(filename):
#    with open(filename, 'r') as ssearch_file:
#        for line in ssearch_file:
#            line = line.rstrip()
#            if not line.startswith('#'):
#                qseqid, sseqid, percid, alen, mismat, gaps, q_start, q_end, s_start, s_end, evalue, bits = line.split("\t")
#                
#                #data_dict[qseqid] = 
#    return sseqid

#print(ssearch_file_to_dict(sys.argv[1]))