##########################################################
# file : largest_and_smallest.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: program that gets three numbers and return the largest and
# after that the smallest number between the 3 numbers
##########################################################


def largest_and_smallest(x, y, z):
    """this function """
    if x >= y and x <= z or x >= z and x <= y:
        # checking x isn't the largest or the smallest number
        if y > z: # checking who is largest: y or z
            return y, z
        else:
            return z, y
    elif y >= x and y <= z or y >=z and y <= x:
        # checking y isn't the largest or the smallest number
        if x > z: # checking who is largest: x or z
            return x, z
        else:
            return z, x
    elif z >= y and z <= x or z >= x and z <= x:
        # checking z isn't the largest or the smallest number
        if x > y: # checking who is largest: y or x
            return x, y
        else:
            return y, x