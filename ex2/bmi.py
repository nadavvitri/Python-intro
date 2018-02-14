##########################################################
# file : bmi.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: program that function that calculate BMI (weight/height**2)
# if the bmi between 18.5 and 24.9 (included) the function return true, other
# the function return false.
##########################################################


def is_normal_bmi(weight, height):
    bmi = weight / (height**2)
    if bmi >= 18.5 and bmi <= 24.9:   # check if the bmi Ok
        return True
    else:
        return False
