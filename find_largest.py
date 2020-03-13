#!/usr/bin/python3.7

# create a python function that return maximum number of the following numbers:
# 2000,10000,500000,1000000,20000000

list=[2000,10000,500000,1000000,20000000]
idx=0
def find_max(num):
    max_num=None
    if (max_num is None) or (num>max_num):
        max_num=num
    return max_num

while idx < len(list):
    large_num=find_max(list[idx])
    idx=idx+1

print(large_num)
