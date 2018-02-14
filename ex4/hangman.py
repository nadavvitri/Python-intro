##########################################################
# file : ex4.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex3 2016-2017
# DESCRIPTION: This program contain diffrent function and function
# from hangman_helper.py together, and then made a "hangman" game.
##########################################################
import hangman_helper
import string

def update_word_pattern(word,pattern,letter):
    """this function receive one word, pattern(exactly like the word, but some
    of the letter hidden by underscores) and one letter and return
    update pattern that contain that letter (if the letter in the word """
    new_pattern = list(pattern)
    for i in range(len(word)):
        if word[i] == letter:
            new_pattern[i] = letter
    return ''.join(new_pattern)


def run_single_game(word_list):
    """this function receive word list (from get_random_word) and start the
    game. first the function get a one random word. at the start the error
    counter and the wrong guess list empty. the game will be again and again
    until the user guesses to much (6 guesses) or the user expose the word.
    the user can choose play again or for hint. if the user choose the hint he
    the game suggest for hime letter"""
    error_count = 0
    wrong_guess_lst = []
    word = hangman_helper.get_random_word(word_list)
    msg = hangman_helper.DEFAULT_MSG
    pattern = '_'*len(word)
    while error_count != hangman_helper.MAX_ERRORS and pattern != word:
        hangman_helper.display_state(pattern,error_count,wrong_guess_lst,msg)
        user_decision, second_choice = hangman_helper.get_input()
        if user_decision == hangman_helper.LETTER:  #user choose a letter
            if len(second_choice) != 1 or not second_choice.islower():
                msg = hangman_helper.NON_VALID_MSG
            elif second_choice in wrong_guess_lst or second_choice in pattern:
                msg = hangman_helper.ALREADY_CHOSEN_MSG + second_choice
            elif second_choice in word:
                pattern = update_word_pattern(word,pattern,second_choice)
                msg = hangman_helper.DEFAULT_MSG
            else:
                wrong_guess_lst.append(second_choice)
                error_count += 1
                msg = hangman_helper.DEFAULT_MSG
        elif user_decision == hangman_helper.HINT:  #user choose for hint
            final = filter_words_list(word_list,pattern,wrong_guess_lst)
            hint_letter = choose_letter(final,pattern)
            msg = hangman_helper.HINT_MSG + hint_letter
    if error_count == hangman_helper.MAX_ERRORS:
        msg = hangman_helper.LOSS_MSG + word
    else:
        msg = hangman_helper.WIN_MSG

    hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg
                                 , ask_play=True)

def main():
    """this function load word from word list(from hangman_helper).
    this function start the game and when the game end the function suggest
    to play again"""
    word_list = hangman_helper.load_words()
    while True:
        run_single_game(word_list)
        user_decision, second_choice = hangman_helper.get_input()
        if not second_choice:
            break

def filter_by_length(words,pattern):
    """this function receive word list and pattern and filter the word list
    and return the matching words (matching by length"""
    filterd_list = []
    for i in words:
        if len(i) == len(pattern):
            filterd_list.append(i)
    return filterd_list

def filter_by_wrong_guess_lst(new_lst,wrong_guess_lst):
    """this function receive word list that (matching by length) and the wrong
    guess list of letter and filter the words list, and return only the words
    that the wrongs letter not in them"""
    second_lst = []
    if not wrong_guess_lst:
        return new_lst
    for word in new_lst:
        for j in wrong_guess_lst:
            if j not in word:
                second_lst.append(word)
            else:
                break
    return second_lst


def filter_by_same_places(new_second_lst,pattern):
    """this function receive word list(that filter by length and wrong letters)
    and filter the list and return the words that have the exposed letter from
    the pattern in the same index letter in the word list"""
    final = []
    for word in new_second_lst:
        check = True
        for i in range(len(word)):
            if pattern[i] == word[i]:
                check = True
            elif pattern[i] == '_':
                check = True
            else:
                check = False
                break
        if check == True:
            final.append(word)
    return final


def filter_words_list(words, pattern, wrong_guess_lst):
    """this function receive word list,the pattern and the wrong guess list
    and filter them(for the user if he ask for help). the word filter by
    length,without the letter from the wrong guess list and by the same_places
    (that return the words that have the exposed letter from
    the pattern in the same index letter in the word list).
     after the words filterd the function return them"""
    new_lst = filter_by_length(words,pattern)
    new_second_lst = filter_by_wrong_guess_lst(new_lst,wrong_guess_lst)
    final_lst = filter_by_same_places(new_second_lst,pattern)
    return final_lst


def choose_letter(words,pattern):
    """this function receive word list and the pattern, and check if the
    exposed letter in the pattern are in the word. if not the function check
    for the maximum occurrence letter in the list and return this letter"""
    alphabet = list(string.ascii_lowercase)
    occurrence_lst = [0]*26
    for i in range(len(alphabet)):
        for word in words:
            if alphabet[i] in pattern:
                break
            else:
                if alphabet[i] in word:
                    occurrence_lst[i] += word.count(alphabet[i])
    return alphabet[occurrence_lst.index(max(occurrence_lst))]


if __name__ == "__main__":
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()