#!/usr/bin/env python3

import re

#open text file
with open("Python_07_nobody.txt","r") as nobody_text:
  for line in nobody_text:
    line = line.rstrip()
    #replace nobody to bekah    
    new_line = re.sub(r'Nobody','Bekah', line)
    print(new_line)

