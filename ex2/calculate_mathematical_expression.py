##########################################################
# file : calculate_mathematical_expression.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: program that contain 2 functions that gets 2 numbers and
# mathematical operation (+,-,/,*) and to the math solution.
# the second function gets the mathematical question by one string and return
# the answer.
##########################################################


def calculate_mathematical_expression(number_one, math_operation, number_two):
    """this function do the mathematical operation you choose and return the
    value. if the you try to divide number by zero or choose another math
    operation from the +,-,/,* the function return "None' """
    if math_operation == '-' :
        return number_one - number_two
    elif math_operation == '/' and number_two == 0 :
        #the you can't divide number by zero!
        return None
    elif math_operation == '/' :
        return number_one/number_two
    elif math_operation == '+' :
        return number_one + number_two
    elif math_operation == '*' :
        return number_one * number_two
    else:  # if the user choose diffrent mathematical operation
        return None


def calculate_from_string(math_question):
    """this function gets a mathematical question from the user and return the
    answer by using the previous function. the user type the question and the
    function split the numbers and the math operation and put it in
    the previous function"""
    first_number,opertation,second_number = math_question.split()
    # split the string
    return calculate_mathematical_expression( float(first_number),
                            opertation, float(second_number))
