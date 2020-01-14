#!/usr/bin/env python3

fname=input('Enter the file name:')
try:
  fhand=open(fname)
except:
  print('File can not be opened:', fname)
  exit()

for line in fhand:
    line=line.upper()
    print(line)

fhand.close()
