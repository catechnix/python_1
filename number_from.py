#!/usr/bin/env python3

fhand=open("mbox-short.txt")
count=0
for line in fhand:
  words=line.split()
  if len(words)==0: continue
  #print(words)
  if words[0]=="From":
      print(words[1])
      count=count+1

print("There are " + str(count) + " number lines to have From in the beginning.")
