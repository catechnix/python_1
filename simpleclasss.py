#!/usr/bin/python3.7
#Define a simple class for fruits:

class fruits:

    type='plants'

    def __init__(self, name, grow_season):
        self.name=name
        self.grow_season=grow_season

apple=fruits("Apple", "summer")
pear=fruits("Pears", "summer")

print("{} grows during {}".format(apple.name, apple.grow_season))
print("{} grows during {}".format(pear.name, pear.grow_season))
print("{}\'s type is {}".format(apple.name, apple.type))
