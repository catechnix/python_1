#!/usr/bin/python3.7

#Write  Python code lines to get the sum all numbers in a list then get the result of multiplying them,
# then get the largest number of them, then get the smallest number of them,
#finally get the numbers of items in that list.

list=[12,23,24,45]

#total=sum(list)
#print(total)

multi_result=1
idx=0
while idx<len(list)-1:
    multi_result=multi_result*list[idx]
    #print(list[idx])
    idx=idx+1

print(multi_result)

max_num=max(list)
print(max_num)

min_num=min(list)
print(min_num)

max_num=None
idx=0
while idx<len(list):
    if (max_num is None) or (list[idx]>max_num):
        max_num=list[idx]
    idx=idx+1
print(max_num)
