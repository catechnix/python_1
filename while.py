#!/usr/bin/python3.7


#Write a program in python that print a list of numbers from 1
#to 9 in descending order using while loop,then print the last 5 items: :

num=9
num_list=[]
while num > 0:
  num_list.append(num)
  num=num-1
print(num_list)


for num in num_list[4:]:
    print(str(num)+'\n')
