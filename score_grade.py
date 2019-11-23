#!/usr/bin/env python3

def compute_grade(score):
        if score>=0.9:
                print ("A")
        elif score>=0.8:
                print ("B")
        elif score>=0.7:
                print ("C")
        elif score>=0.6:
                print ("D")
        else:
                print ("F")

while True:
    iscore=input("Enter Interger or float number:\n")

    try:
        iscore = float (iscore)
    except ValueError:
        print ("Not an digit number")
    compute_grade(iscore)
