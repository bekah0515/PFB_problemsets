#!/usr/bin/env python3
import sys
import re 
import pprint
from collections import defaultdict 

restrictenz_dict=defaultdict(list)
sequence=[]
#open text file
with open("bionet.txt","r") as bionet_file:
  for linenumber,line in enumerate(bionet_file):
    if linenumber < 10:
        continue
    line = line.rstrip()
    #delineate header as key and sequence as value for RE dictionary
    enzyme_name,sequence = re.split(r"\s{2,}", line)
    print(enzyme_name, sequence)
    if enzyme_name in restrictenz_dict:
        restrictenz_dict[enzyme_name].append(sequence)
    else:
        restrictenz_dict[enzyme_name] = [sequence]



    
  #  for enzyme_name in re.search(r"(^\S+ \S*)", line):
   #   restrictenz_dict[enzyme_name]=''
    #  #print(header)
  #  for sequence in re.findall(r'(\S+$)',line):
   #   restrictenz_dict[header] = [sequence]
      #if "^" in sequence:
        #carrot_rmv_seq = sequence.replace("^","")
        #sequence.append(carrot_rmv_seq)


      
pprint.pprint(restrictenz_dict)
#print(restrictenz_dict)
#print(len(restrictenz_dict))

#grab input from command line
#inputfile=sys.argv[2]

#open fasta file
#with open(inputfile,"r") as seq_read:
#  for line in seq_read:
#    line = line.rstrip()
#    if not line.startswith(">"):
#      inputseq = line.upper()
#      print(inputseq)

#try:
#  enzyme_to_search=sys.argv[1]
#  print("You searched for:", enzyme_to_search)
#  cut_site = restrictenz_dict[enzyme_to_search]
#  print("cut_site:", cut_site)
  
#except:
#  print("No enzyme by that name.")
