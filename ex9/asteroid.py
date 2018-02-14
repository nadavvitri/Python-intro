##########################################################
# file : ex9.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION: This program contain class that define the asteroids in the
# asteroid game
##########################################################

############################################################
# Imports
############################################################
import screen as Sc
import random
import math

############################################################
# Constant
############################################################
STARTING_SPEED = 1
MAXIMUM_SPEED = 1
SIZE_COEFFICIENT = 10
NORMAL_FACTOR = 5

############################################################
# Class definition
############################################################
class Asteroid:
    """
    this class define every asteroid in the game. the characteristics of the
    asteroid are position in axis x and axis y (coordinate), speed in axis x,
    speed in axis y and size of the asteroid(int between 1 to 3).
    the radius of the asteroid is the size of the asteroid *
    (SIZE_COEFFICIENT - NORMAL_FACTOR). the position are random but can't be
    the same position of ship. the default number of asteroid in the game is 3.
    asteroid can destroyed if torpedo shoot him or he crushed with the ship.
    (mor in asteroid_main.py)
    """

    def __init__(self, size: int):
        """
        Constructor of torpedo
        """
        self.__pos = (
            random.randint(Sc.Screen.SCREEN_MIN_X, Sc.Screen.SCREEN_MAX_X),
            random.randint(Sc.Screen.SCREEN_MIN_Y, Sc.Screen.SCREEN_MAX_Y))
        self.__speed_x = random.randint(STARTING_SPEED, MAXIMUM_SPEED)
        self.__speed_y = random.randint(STARTING_SPEED, MAXIMUM_SPEED)
        self.__pos_x = self.__pos[0]
        self.__pos_y = self.__pos[1]
        self.__size = size
        self.__radius = size * (SIZE_COEFFICIENT - NORMAL_FACTOR)

    def has_intersection(self, obj):
        """
        this function check if there is a intersection between asteroid and
        object (torpedo or ship). iof there is a intersection the function
        return true. else the function return false
        """
        distance_in_x = math.pow(obj.get_pos_x() - self.get_pos_x(), 2)
        distance_in_y = math.pow(obj.get_pos_y() - self.get_pos_y(), 2)
        distance = math.sqrt(distance_in_x + distance_in_y)
        if distance <= self.get_radius() + obj.get_radius():
            return True
        else:
            return False

    def get_pos_x(self):
        """return the current position in axis x"""
        return self.__pos_x

    def get_pos_y(self):
        """return the current position in axis y"""
        return self.__pos_y

    def get_pos(self):
        """return the current position in axis x and axis y (x, y)"""
        return self.__pos

    def set_pos(self, new_pos):
        """set new speed (new_speed) in axis x for the torpedo"""
        self.__pos = new_pos

    def get_speed_x(self):
        """return the current speed in axis x"""
        return self.__speed_x

    def get_speed_y(self):
        """return the current speed in axis y"""
        return self.__speed_y

    def set_new_pos_in_x(self, new_pos):
        """set new position (new_pos) in axis x for the asteroid"""
        self.__pos_x = new_pos

    def set_new_pos_in_y(self, new_pos):
        """set new position (new_pos) in axis y for the asteroid"""
        self.__pos_y = new_pos

    def get_radius(self):
        """return the radius of the asteroid"""
        return self.__radius

    def get_size(self):
        """return the size of the asteroid"""
        return self.__size

    def set_new_speed_x(self, new_speed):
        """set new speed (new_speed) in axis x for the asteroid"""
        self.__speed_x = new_speed

    def set_new_speed_y(self, new_speed):
        """set new speed (new_speed) in axis y for the asteroid"""
        self.__speed_y = new_speed

