#!/usr/bin/env python3

fname=input ("Enter file name to look for: \n")
try:
    fhand=open(fname)
except:
    print('File can not be opened:', fname)
    exit

count=0
total=0
for line in fhand:
    #print(line)
    str='X-DSPAM-Confidence: '
    num=len(str)
    if str in line:
        str=line[num:].strip()
        total=total+float(str)
        count=count+1
average=total/count
print (average)

fhand.close()
