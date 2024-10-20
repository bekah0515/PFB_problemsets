#!/usr/bin/env python3
import subprocess

rtn = subprocess.run(['ls','-l'], stdout=subprocess.PIPE)

if rtn.returncode !=0:
    print('Failed!')
else:
    print('printing now')

bytes = rtn.stdout
stdout = bytes.decode('utf-8')
lines = stdout.splitlines()

print (lines[0])
