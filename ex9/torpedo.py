##########################################################
# file : ex9.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION: This file have the class Torpedo that define the torpedoes
# in the asteroid game
##########################################################

############################################################
# Imports
############################################################
from ship import Ship
import math
############################################################
# Constant
############################################################
ACCELERATE_FACTOR = 2
TORPEDO_RADIUS = 4
TORPEDO_STARTING_LIVES = 200

############################################################
# Class definition
############################################################
class Torpedo:
    """
    this class define every torpedo in the game. ship can shoot torpedo and
    destroy asteroid. the characteristics of torpedo are: position in axis x
    and axis y (coordinate), speed in axis x, speed in axis y, and heading (in
    degrees). torpedo show's in the game to specific time, and there is a limit
    of numbers that ship can shoot (more in the asteroid_main.py).
    the radius of the torpedo is 4.
    """

    def __init__(self, ship: Ship):
        """
        Constructor of torpedo
        """
        self.__speed_x = ship.get_speed_x() +\
                         ACCELERATE_FACTOR * math.cos(math.radians
                                                      (ship.get_heading()))
        self.__speed_y = ship.get_speed_y() + \
                         ACCELERATE_FACTOR * math.sin(math.radians
                                                      (ship.get_heading()))
        self.__pos_x = ship.get_pos_x()
        self.__pos_y = ship.get_pos_y()
        self.__heading = ship.get_heading()
        self.__radius = TORPEDO_RADIUS
        self.__lives = TORPEDO_STARTING_LIVES

    def get_pos_x(self):
        """return the current position in axis x"""
        return self.__pos_x

    def get_pos_y(self):
        """return the current position in axis y"""
        return self.__pos_y

    def get_speed_x(self):
        """return the current speed in axis x"""
        return self.__speed_x

    def get_speed_y(self):
        """return the current speed in axis y"""
        return self.__speed_y

    def set_speed_x(self, new_speed):
        """set new speed (new_speed) in axis x for the torpedo"""
        self.__speed_x = new_speed

    def set_speed_y(self, new_speed):
        """set new speed (new_speed) in axis y for the torpedo"""
        self.__speed_y = new_speed

    def get_heading(self):
        """return the current heading of the torpedo"""
        return self.__heading

    def set_new_pos_in_x(self, new_pos):
        """set new position (new_pos) in axis x for the torpedo"""
        self.__pos_x = new_pos

    def set_new_pos_in_y(self, new_pos):
        """set new position (new_pos) in axis y for the torpedo"""
        self.__pos_y = new_pos

    def get_radius(self):
        """return the radius of the torpedo"""
        return self.__radius

    def get_lives(self):
        """return the current lives of the torpedo"""
        return self.__lives

    def set_lives(self, new_number_of_lives):
        """set the new number of lives (new_number_of_lives) of the torpedo"""
        self.__lives = new_number_of_lives

