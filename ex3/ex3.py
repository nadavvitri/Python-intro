##########################################################
# file : ex3.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex3 2016-2017
# DESCRIPTION: This program contain 8 functions that uses variable and
# loops. Some of the function contain loop in inside loop.
##########################################################


def create_list():
    """this function gets many strings from the user until the use enter
    empty string. the function make one list with all the strings
    the user enter.space bar consider like a string and not like empty string.
    if the function receive empty string the function return also empty string.
     the function uses the 'append' method"""
    main_list = []
    while True:
        string_from_user = input()
        if len(string_from_user) != 0:
            main_list.append(string_from_user)
        else:
            break #when the user enter empty string the function gives the list
    return (main_list)


def concat_list(str_lst):
    """the function receive list of strings and concatenation them
    and return them as one string. """
    list_to_string = ''
    for word in str_lst:
        list_to_string += word
    return list_to_string


def average(num_list):
    """the function receive list of numbers and return the average of them.
    if the function receive empty list the function return None."""
    total = 0
    if len(num_list) == 0: # if the list empty!
        return None
    else:
        for number in num_list:
            total += number
        return total/len(num_list)


def cyclic(lst1,lst2):
    """the function receive two lists and check if one list is the cyclic
    formation of the other: if the list is the cyclic formation of the
     second list the function return True. if not the function return False"""
    check_list = lst1[:]
    if lst1 == [] and lst2 == []: # if they both empty it's True!
        return True
    for i in range(len(lst1)):
        if check_list[i:] + check_list[:i] == lst2:
            return True
    else:
        return False


def histogram(n, num_list):
    """this function receive list of numbers and another number.
    the function return the hystogram list. the value for numbers that not
    show in the list is zero.
    the function create new empty list and count how many times the number
    show in the list and put it in the new list and
    after that return the list"""
    new_list = [0]*n
    for i in range(n):
        counting = 0
        for number in num_list:
            if i == number:
                counting += 1
        new_list[i] = counting

    return new_list


def prime_factors(n):
    """the function receive one number and return list of all the prime
    numbers of the number. if the function receive prime number the
    function return this number
    the function return all the prime numbers from lower to greater"""
    prime_numbers = []
    for i in range(2, n):
        while n % i == 0:
            prime_numbers.append(i)
            n = n/(i)
    if n != 1:
        prime_numbers.append(n)
    return prime_numbers


def cartesian(lst1, lst2):
    """this function receive two lists and return all the cartesian product
    between them. the element in the list can be from any type.
    if one list or two of the list are empty the function return return empty
    list"""
    index = []
    for i in lst1:
        for j in lst2:
            index.append((i,j))
    return index


def pairs(n, num_list):
    """the function receive list of numbers and another number and return all
     the pairs (list in length 2) that the sum of them is exactly to
     another number"""
    pairs_index = []
    new_num_list = num_list[:]
    for i in num_list:
        for j in new_num_list:
            if i + j == n:
                pairs_index.append([i,j])
                new_num_list.remove(i)
    return pairs_index