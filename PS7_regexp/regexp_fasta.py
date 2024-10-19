#!/usr/bin/env python3

import re

#open text file
with open("Python_07.fasta","r") as fasta_file:
  for line in fasta_file:
    line = line.rstrip()
    #find every header 
    for match in re.finditer(r"(^>\S+)(.*)",line):
      print("id:", match.group(1), "desc:", match.group(2))

