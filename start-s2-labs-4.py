# Author: CMOB 1/25/2022

def double_every_other(lst):
    lst1 = []
    for index, value in enumerate(lst):
        if index % 2 != 0: # if the index doesn't have a remainder of 0
            value *= 2 # take the value and double it
            lst1.append(value) # add it back to a list
        else:
            lst1.append(value) # if not add the original value to the list

    return lst1

print(double_every_other([1,2,3,4]))