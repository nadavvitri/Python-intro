##########################################################
# file : ex6.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex6 2016-2017
# DESCRIPTION: This program contain class that define the game and use the
# ships define from ship.py
##########################################################

############################################################
# Imports
############################################################
import game_helper as gh
############################################################
# Class definition
############################################################

NEW_BOMB = 4

class Game:
    """
    A class representing a battleship game.
    A game is composed of ships that are moving on a square board and a user
    which tries to guess the locations of the ships by guessing their
    coordinates.
    """

    def __init__(self, board_size, ships):
        """
        Initialize a new Game object.
        :param board_size: Length of the side of the game-board.
        :param ships: A list of ships (of type Ship) that participate in the
            game.
        :return: A new Game object.
        """
        self.__board_size = board_size
        self.__ships = ships
        self.__bombs = {}

    def move_all_ship(self):
        for ship in self.__ships:
            ship.move()

    def update_ship_on_hit(self):
        hit = set()
        for ship in self.__ships:
            for bomb in list(self.__bombs):
                if ship.hit(bomb):
                    hit.add(bomb)
                    del self.__bombs[bomb]
        return list(hit)

    def check_if_bomb_hit(self, target):
        coordinates_of_hits = []
        for ship in self.__ships:
            if target in ship.coordinates():
                coordinates_of_hits.append(target)
                del self.__bombs[target]
        return coordinates_of_hits

    def coordinates_of_hited_ships(self):
        hited_coordinates = []
        for ship in self.__ships:
            for i in ship.coordinates():
                if ship.cell_status(i):
                    hited_coordinates.append(i)
        return hited_coordinates

    def not_hitted_coordinates(self):
        not_hitted = []
        for ship in self.__ships:
            for i in ship.coordinates():
                if ship.cell_status(i) == False:
                    not_hitted.append(i)
        return not_hitted


    def __play_one_round(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. The logic defined by this function must be implemented
        but if you wish to do so in another function (or some other functions)
        it is ok.

        The function runs one round of the game :
            1. Get user coordinate choice for bombing.
            2. Move all game's ships.
            3. Update all ships and bombs.
            4. Report to the user the result of current round (number of hits and
             terminated ships)
        :return:
            (some constant you may want implement which represents) Game status :
            GAME_STATUS_ONGOING if there are still ships on the board or
            GAME_STATUS_ENDED otherwise.
        """
        number_of_terminated = 0
        # getting the coordinates of the new bomb
        target = gh.get_target(self.__board_size)
        self.__bombs[target] = NEW_BOMB
        self.move_all_ship()
        this_turn_hits = self.update_ship_on_hit()

        if self.__ships:
            for i in self.__bombs:
                self.__bombs[i] -= 1
            for key in list(self.__bombs):  # remove hits that are 3 turns
                if self.__bombs[key] <= 0:
                    del self.__bombs[key]

        not_hited_coordinate = self.not_hitted_coordinates()
        hited_coordinate = self.coordinates_of_hited_ships()
        print(gh.board_to_string(self.__board_size,
                                 this_turn_hits, self.__bombs,
                                 hited_coordinate, not_hited_coordinate))

        for ship in self.__ships:  # remove ship if terminated
            if ship.terminated():
                self.__ships.remove(ship)
                number_of_terminated += 1
        gh.report_turn(len(this_turn_hits), number_of_terminated)

    def __repr__(self):
        """
        Return a string representation of the board's game.
        :return: A tuple converted to string (that is, for a tuple x return
            str(x)). The tuple should contain (maintain
        the following order):
            1. Board's size.
            2. A dictionary of the bombs found on the board, mapping their
                coordinates to the number of remaining turns:
                 {(pos_x, pos_y) : remaining turns}
                For example :
                 {(0, 1) : 2, (3, 2) : 1}
            3. A list of the ships found on the board (each ship should be
                represented by its __repr__ string).
        """
        return str((self.__board_size, self.__bombs, self.__ships))

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        gh.report_legend()
        print(gh.board_to_string(self.__board_size, [],
                                 self.__bombs, [],
                                 self.not_hitted_coordinates()))
        # if there is no ships on the game then stop playing!
        while len(self.__ships) > 0:
            self.__play_one_round()
        gh.report_gameover()

############################################################
# An example usage of the game
############################################################
if __name__=="__main__":
    # game = Game(5, gh.initialize_ship_list(4, 2))
    import ship
    ship1 = ship.Ship((1, 1), 1, "l", 5)
    ship2 = ship.Ship((1, 3), 3, "r", 5)
    game = Game(5, [ship1, ship2])
    game.play()
