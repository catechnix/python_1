#!/usr/bin/env python3

fname=input("File name to parse which day to do the commit:\n")

nums_day=dict()
words=[]
fhand=open(fname)
for line in fhand:
    words=line.split()
    if len(words)==0: continue
    if words[0] != "From": continue
    day=words[2]
    if day not in nums_day:
        print(day)
        nums_day[day]=1
    else:
        nums_day[day]+=1
print(nums_day)
