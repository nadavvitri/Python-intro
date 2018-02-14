##########################################################
# file : ex9.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION: This program contain class that define and run the asteroid game
# use the classes asteroid, torpedo and ship.
##########################################################

############################################################
# Imports
############################################################
from screen import Screen
import sys
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import math
############################################################

############################################################
# Constant
############################################################
DEFAULT_ASTEROIDS_NUM = 3
DEFAULT_ASTEROIDS_SIZE = 3
CHANGE_HEADING_LEFT = 7
CHANGE_HEADING_RIGHT = -7
BIG_ASTEROID = 3
MEDIUM_ASTEROID = 2
SMALL_ASTEROID = 1
STARTING_SCORE = 0
POINTS_FOR_BIG_ASTEROID = 20
POINTS_FOR_MEDIUM_ASTEROID = 50
POINTS_FOR_SMALL_ASTEROID = 100
ONE_UNIT_LESS = 1
OPPOSITE = -1
TORPEDOS_MAX_NUMBER = 15
TORPEDO_OUT_OF_LIFE = 0
SHIP_OUT_OF_LIFES = 0
ASTEROIDS_OUT_OF_LIFE = 0
TITLE_FOR_CRUSHING = "Crash!"
MESSAGE_FOR_CRUSHING = "Your ship has crushed with asteroid!"
TITLE_ENDED_ASTEROID = "Asteroids destroyed"
MESSAGE_ENDED_ASTEROID = "Great Job! you destroyed all the asteroids!"
TITLE_FOR_EXIT = "Exit"
MESSAGE_FOR_EXIT = "We hope to see you soon! Bye Bye"
TITLE_ENDED_LIVES = "Game over!"
MESSAGE_ENDED_LIVES = "Your lives are ended :("

############################################################
# Class definition
############################################################
class GameRunner:
    """
    this class define the game and include all the descriptions of the game -
    the object ship. torpedoes and asteroids.
    when the game start there is a ship and asteroids (default number is 3)
    moving in the screen. the ship can shoot torpedoes and hit destroy the
    asteroids. the game over when the user click on 'exit', or when he destroy
    all the asteroids or when the lives of the ship end (3 lives).
    this class contain functions that run the game and move the objects.
    """

    def __init__(self, asteroids_amnt):
        """
        Constructor of a GameRunner.
        the asteroids_amnt is the number of asteroids in the
        starting of the game
        """
        self._screen = Screen()
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.delta_x = self.screen_max_x - self.screen_min_x
        self.delta_y = self.screen_max_y - self.screen_min_y
        self.__ship = Ship()
        self.__asteroids = []
        self.__torpedos = []
        for i in range(asteroids_amnt):
            asteroid = Asteroid(DEFAULT_ASTEROIDS_SIZE)
            # check if the starting position not same like the ship
            self.check_asteroid_first_pos(asteroid)
            self._screen.register_asteroid(asteroid, DEFAULT_ASTEROIDS_SIZE)
            self.__asteroids.append(asteroid)
        self.__score = STARTING_SCORE

    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        self._game_loop()

        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

    def check_asteroid_first_pos(self, asteroid: Asteroid):
        """this function check if the position of a new asteroid in the game
        is not the same position of the ship. if so the function change
        the position to a new coordinate"""
        if asteroid.get_pos() == self.__ship.get_pos():
            asteroid.set_pos(asteroid.get_pos())

    def new_torpedo(self):
        """this function create a new torpedo (only if there is not more then
        15 torpedoes in the game!) to the game by using class
        Torpedo. the function register and add the new torpedo to the torpedoes
        list."""
        if len(self.__torpedos) < TORPEDOS_MAX_NUMBER:
            torpedo = Torpedo(self.__ship)
            self._screen.register_torpedo(torpedo)
            self.__torpedos.append(torpedo)

    def move_object(self, object):
        """this function move all the object in the game. the object can be
        asteroid, torpedo or ship. the movements of the object is according
        to a specific calculation (given in ex9.pdf)"""
        # the formula given in ex.pdf
        object.set_new_pos_in_x((object.get_speed_x() + object.get_pos_x()
                                      - self.screen_min_x) % \
                      self.delta_x + self.screen_min_x)
        object.set_new_pos_in_y((object.get_speed_y() + object.get_pos_y()
                                      - self.screen_min_y) % \
                      self.delta_y + self.screen_min_y)

    def change_ship_direction(self):
        """this function change the heading of the ship: if the user click
        'left button' the ship move 7 degrees, and if the user click 'right
        button' the ship move -7 degrees."""
        if self._screen.is_left_pressed():
            self.__ship.set_new_heading(self.__ship.get_heading()
                                        + CHANGE_HEADING_LEFT)
        elif self._screen.is_right_pressed():
            self.__ship.set_new_heading(self.__ship.get_heading()
                                        + CHANGE_HEADING_RIGHT)

    def accelerate_ship(self):
        """this function accelerate the ship if the user click 'up button'.
        the accelerate is according to a
        specific calculation (given in ex9.pdf)"""
        # the formula given in ex.pdf
        heading_to_radians = math.radians(self.__ship.get_heading())
        self.__ship.set_speed_x(self.__ship.get_speed_x() +
                                math.cos(heading_to_radians))
        self.__ship.set_speed_y(self.__ship.get_speed_y() +
                                math.sin(heading_to_radians))

    def torpedo_intersection(self):
        """this function check if the torpedo hit the asteroid.
        if so the user get points (depend in the size of the destroyed
        asteroid) and update the score in the screen. if the destroyed
        asteroid size more then 1 the function call to split_asteroid and split
        the asteroid to a two new smaller asteroids(more in split_asteroid)"""
        for asteroid in self.__asteroids:
            for torpedo in self.__torpedos:
                if asteroid.has_intersection(torpedo):
                    # getting score depend in the size of the asteroid
                    # while the size off the asteroid bigger then one then
                    # split the asteroid
                    if asteroid.get_size() == BIG_ASTEROID:
                        self.__score += POINTS_FOR_BIG_ASTEROID
                        self.split_asteroid(asteroid, torpedo)
                    elif asteroid.get_size() == MEDIUM_ASTEROID:
                        self.__score += POINTS_FOR_MEDIUM_ASTEROID
                        self.split_asteroid(asteroid, torpedo)
                    else:
                        # the asteroid is in size one so remove him
                        #  and not split him
                        self.__score += POINTS_FOR_SMALL_ASTEROID
                        self._screen.unregister_asteroid(asteroid)
                        self.__asteroids.remove(asteroid)
                        self._screen.unregister_torpedo(torpedo)
                        self.__torpedos.remove(torpedo)

    def split_asteroid(self, asteroid: Asteroid, torpedo: Torpedo):
        """if torpedo hit asteroid (in size more then 1) the function split
        the asteroid to two new smaller asteroids. the new asteroid move in
        opposite directions and the size of them is one unit less (from the
        original asteroid). the function remove the original asteroid and the
        torpedo that hit him!"""
        # the formula given in ex.pdf
        sum_speed_x = torpedo.get_speed_x() + asteroid.get_speed_x()
        sum_speed_y = torpedo.get_speed_y() + asteroid.get_speed_y()
        current_x_and_y_speed = math.pow(asteroid.get_speed_x(), 2) \
                                + math.pow(asteroid.get_speed_y(), 2)
        for i in range(2):
            # create two new asteroid (split the original asteroid)
            new_asteroid = Asteroid(asteroid.get_size() - ONE_UNIT_LESS)
            new_asteroid.set_new_speed_x(sum_speed_x /
                                         math.sqrt(current_x_and_y_speed))
            new_asteroid.set_new_speed_y(sum_speed_y /
                                         math.sqrt(current_x_and_y_speed))
            new_asteroid.set_new_pos_in_x(asteroid.get_pos_x())
            new_asteroid.set_new_pos_in_y(asteroid.get_pos_y())
            # the size of the new asteroids is smaller by one unit
            self._screen.register_asteroid(new_asteroid, asteroid.get_size()
                                           - ONE_UNIT_LESS)
            self.__asteroids.append(new_asteroid)
            if i == 1:
                # change the movement of one of the asteroids to the
                #  opposite direction
                new_asteroid.set_new_speed_x(new_asteroid.get_speed_x()
                                             * OPPOSITE)
                new_asteroid.set_new_speed_x(new_asteroid.get_speed_y()
                                             * OPPOSITE)
        # remove the original asteroid after we split him
        self._screen.unregister_asteroid(asteroid)
        self.__asteroids.remove(asteroid)
        # remove the torpedo after he hit the asteroid
        self._screen.unregister_torpedo(torpedo)
        self.__torpedos.remove(torpedo)

    def change_torpedo_live(self, torpedo: Torpedo):
        """this function update the lives of torpedo that has been shoot from
        the ship. as starting the live of torpedo are 200 and each step he lose
        one 'live'. if torpedo lose lives the function remove him!"""
        if torpedo.get_lives() == TORPEDO_OUT_OF_LIFE:
            self._screen.unregister_torpedo(torpedo)
            self.__torpedos.remove(torpedo)
        else:
            torpedo.set_lives(torpedo.get_lives() - ONE_UNIT_LESS)

    def check_if_exit_game(self):
        """this function check if the user end the game. there is three options
        to end game: if user click on 'exit button', or ship lives over or
        user win and destroy all the asteroids. the function pop a message
        to the user (each one different, depend why the user end game) and
        exit from the game"""
        # if user win and destroy all the asteroids
        if len(self.__asteroids) == ASTEROIDS_OUT_OF_LIFE:
            self._screen.show_message(TITLE_ENDED_ASTEROID,
                                      MESSAGE_ENDED_ASTEROID)
            self._screen.end_game()
            sys.exit()
        # if the user loss all his lives
        elif self.__ship.get_lives() == SHIP_OUT_OF_LIFES:
            self._screen.show_message(TITLE_ENDED_LIVES, MESSAGE_ENDED_LIVES)
            self._screen.end_game()
            sys.exit()
        # if user ask to exit:
        elif self._screen.should_end():
            self._screen.show_message(TITLE_FOR_EXIT, MESSAGE_FOR_EXIT)
            self._screen.end_game()
            sys.exit()

    def asteroid_in_the_game(self):
        """
        this function do all the things needed to do in the game for asteroids:
        first we check for every asteroid in the game and draw them. then we
        check if they crushed with object and if so to remove him.
        """
        # for each asteroid in the game
        for asteroid in self.__asteroids:
            # draw the asteroid in the game and move him
            self._screen.draw_asteroid(asteroid, asteroid.get_pos_x(),
                                       asteroid.get_pos_y())
            self.move_object(asteroid)
            # if ship crush the asteroid
            if asteroid.has_intersection(self.__ship):
                self._screen.show_message(TITLE_FOR_CRUSHING,
                                          MESSAGE_FOR_CRUSHING)
                # remove one live from ship lives
                self._screen.remove_life()
                self.__ship.set_lives(self.__ship.get_lives() - ONE_UNIT_LESS)
                # remove the asteroid from the game
                self._screen.unregister_asteroid(asteroid)
                self.__asteroids.remove(asteroid)


    def _game_loop(self):
        '''
        this function run game loop. the function check if user click on
        keyboard and change things to that.
        the game end when user click on exit button, or user lose and his ship
        lives ended, or if user win and destroyed all the asteroids
        '''
        # check if user end game
        self.check_if_exit_game()
        # draw the ship in the game and move her
        self._screen.draw_ship(self.__ship.get_pos_x(),
                         self.__ship.get_pos_y(), self.__ship.get_heading())
        self.move_object(self.__ship)
        # the user change the direction of the ship by clicking (left or right)
        self.change_ship_direction()
        # the user accelerate the ship by clicking up
        if self._screen.is_up_pressed():
            self.accelerate_ship()
        # create the asteroids and check if they crushed with objects
        self.asteroid_in_the_game()
        # the user shoot torpedo by clicking space bar button
        if self._screen.is_space_pressed():
            self.new_torpedo()
        # for each torpedo in the game
        for torpedo in self.__torpedos:
            # move and draw the torpedo
            self.move_object(torpedo)
            self._screen.draw_torpedo(torpedo, torpedo.get_pos_x()
                                      , torpedo.get_pos_y(),
                                      torpedo.get_heading())
            # check if torpedo hit asteroid
            self.torpedo_intersection()
            # update score in the screen
            self._screen.set_score(self.__score)
            # update the lives of the torpedo in the game
            self.change_torpedo_live(torpedo)


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )