#!/usr/bin/python3.7
#get the result of the union the two last sets:

a ={'red', 'yellow','orange','green'}
#print(a)

b ={'red','orange','black'}
#print(b)

for elm in b:
    a.add(elm)

print(a)
