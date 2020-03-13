#!/usr/bin/python3.7
#Write  a Python code to read the first three lines of a file

f=open("new_set.py","r")
num=0
while num<3:
    print(f.readline().strip())
    num=num+1
