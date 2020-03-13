#!/usr/bin/python3.7
# Create a lambda function that takes one parameter (a) and returns
#if it is even number or not:


n=lambda a: True if a%2==0 else False

a=input("input one number\n")

n(a)
print(n)
