##########################################################
# file : shapes.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: program that contain 4 functions that calculate together the
# area the user want: circle, rectangle or trapezoid.
# first function gets the user answer and uses the other function to return
# the area the user ask for.
##########################################################
import math

PI = math.pi


def shape_area():
    """this function gets the user request and call to the matching function"""
    choosen_shape = input('Choose shape (1=circle, 2=rectangle,'
                          ' 3=trapezoid): ')
    if choosen_shape == '1':
        return circle_area()
    elif choosen_shape == '2':
        return rectangle_area()
    elif choosen_shape == '3':
        return trapezoid_area()
    else: #if the user choose shape that not on the option
        return None


def circle_area():
    """this function  ask for radus from the user and
    return the area of the circle"""
    radus = float(input())
    circ_area = (radus**2) * PI
    return circ_area


def rectangle_area():
    """this function  ask for sides sizes from the user and
    return the area of the rectangle"""
    side_one = float(input())
    side_two = float(input())
    rect_area = side_two*side_one
    return rect_area


def trapezoid_area():
    """this function  ask for bases and high sizes from the user and
    return the area of the trapezoid"""
    base_one = float(input())
    base_two = float(input())
    high = float(input())
    trape_area = ((base_one+base_two)*high) /2
    return trape_area
