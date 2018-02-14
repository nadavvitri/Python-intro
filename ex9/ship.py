##########################################################
# file : ex9.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION: This file have the class Ship that define the ship
# in the asteroid game
##########################################################

############################################################
# Imports
############################################################
import screen as Sc
import random

############################################################
# Constant
############################################################
STARTING_SPEED = 0
STARTING_HEADING = 0
SHIP_RADIUS = 1
STARTING_LIVES = 3

############################################################
# Class definition
############################################################
class Ship:
    """
    this class define every ship in the game. the characteristics of the ship
    are position in axis (coordinate), the speed in axis x and y, the heading
    (in degrees). the starting position are random (in the screen size).
    the starting heading is 0. the radius of the ship is 1.
    ship start with 3 lives, and when ship crushed with asteroid she loss one
    live, and when all the three lives gone the game over
    (the game run in asteroid_main.py)
    """
    def __init__(self):
        """
        Constructor of ship
        """
        self.__pos = (
            random.randint(Sc.Screen.SCREEN_MIN_X, Sc.Screen.SCREEN_MAX_X),
            random.randint(Sc.Screen.SCREEN_MIN_Y, Sc.Screen.SCREEN_MAX_Y))
        self.__speed_x = STARTING_SPEED
        self.__speed_y = STARTING_SPEED
        self.__pos_x = self.__pos[0]
        self.__pos_y = self.__pos[1]
        self.__heading = STARTING_HEADING
        self.__radius = SHIP_RADIUS
        self.__lives = STARTING_LIVES

    def get_pos_x(self):
        """return the current position in axis x"""
        return self.__pos_x

    def get_pos_y(self):
        """return the current position in axis y"""
        return self.__pos_y

    def get_pos(self):
        """return the current position in axis x and axis y (x, y)"""
        return self.__pos

    def get_speed_x(self):
        """return the current speed in axis x"""
        return self.__speed_x

    def get_speed_y(self):
        """return the current speed in axis y"""
        return self.__speed_y

    def get_heading(self):
        """return the current heading of the ship"""
        return self.__heading

    def set_new_pos_in_x(self, new_pos):
        """set new position (new_pos) in axis x for the ship"""
        self.__pos_x = new_pos

    def set_new_pos_in_y(self, new_pos):
        """set new position (new_pos) in axis y for the ship"""
        self.__pos_y = new_pos

    def set_new_heading(self, new_heading):
        """set new heading (new_heading) for the ship"""
        self.__heading = new_heading

    def set_speed_x(self, new_speed):
        """set new speed (new_speed) in axis x for the ship"""
        self.__speed_x = new_speed

    def set_speed_y(self, new_speed):
        """set new speed (new_speed) in axis y for the ship"""
        self.__speed_y = new_speed

    def get_radius(self):
        """return the radius of the ship"""
        return self.__radius

    def get_lives(self):
        """return the current lives of the ship"""
        return self.__lives

    def set_lives(self, new_number_of_lives):
        """set the new number of lives (new_number_of_lives) of the ship"""
        self.__lives = new_number_of_lives




