#!/usr/bin/env python3

with open('Python_06.txt','r') as open_file, open('Python_06_uc.txt','w') as write_file:
  for line in open_file:
    line = line.upper()
    write_file.write(line)
  print('done!')

