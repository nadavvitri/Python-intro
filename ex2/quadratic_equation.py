##########################################################
# file : quadratic_equation.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: program that contain 2 functions. the first function gets 3
# numbers and return the quadratic equation. the second function gets 3
# numbers from the user and return the solutions.
##########################################################


def quadratic_equation(a,b,c):
    """this function calculate quadratic equation"""
    DELTA = b**2-4*a*c  #the delta of the equation
    shoresh = DELTA**0.5
    solution_one = (-b+shoresh) / (2*a)
    solution_two = (-b-shoresh) / (2*a)
    if DELTA > 0: # checking if DELTA positive (2 solutions)
        return solution_one, solution_two
    elif DELTA == 0: # checking if DELTA equal to 0 (1 solution)
        return -b/2*a, None
    else: #DELTA negative (no solutions to the equation!)
        return None, None


def quadratic_equation_user_input():
    user_numbers = input('Insert coefficients a, b, and c: ')
    separate = user_numbers.split( )
    x, y = quadratic_equation( float(separate[0]),
                               float(separate[1]), float(separate[2]))
    if y is not None:
        print('The equation has 2 solutions: ' + str(x) + ' and ' + str(y))
    elif y is None and x is not None:
        print('The equation has 1 solution: ' + str(x))
    else:
        print('The equation has no solutions')