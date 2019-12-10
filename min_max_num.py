#!/usr/bin/env python3

num_list=[]

while True:
    num=input("Enter a number\n")
    if num.lower() != "done":
        try:
            num=int(num)
            num_list.append(int(num))
        except ValueError:
            print("Bad data")
            continue
    else:
        print ("The minumum number is ", min(num_list),"\n")
        print ("The maximum number is ", max(num_list),"\n")
        break
