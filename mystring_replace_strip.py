#!/usr/bin/python3

#write a program in python to declare that The coding is fun, then replace the word 'fun' with  the 'awesome' and then remove the word ' The' :

MyString="The coding is fun"

MyNewString=MyString.replace('fun','awesome')
print(MyNewString+"\n")

MyNewString2=MyString.strip('fun')
print(MyNewString2+"\n")
