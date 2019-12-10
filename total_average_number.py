#!/usr/bin/env python3

total=0
count=0
average=0
while True:
    num=input("Enter a number\n")
    print (type(num))
    if num.lower() != 'done':
        try:
            num=int(num)
        except ValueError:
            print("Invalid input")
            continue
        total=total+num
        count=count+1
    else:
        print ("Total is ",total,"\n")
        print ("Total number is ",count,"\n")
        print ("Average is ",total/count,"\n")
        break

## is and == comparison are different. == compare exact value, "is" compares id
