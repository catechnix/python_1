#!/usr/bin/env python3

fhand=open("romeo.txt")
allwords=[]
for line in fhand:
    words=line.split()
    #print(words)
    for word in words:
        if word not in allwords:
            allwords.append(word)
allwords.sort()
print(allwords)
