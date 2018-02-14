ONE = 1
ZERO_BINARY = '0'
ONE_BINARY = '1'

def print_to_n(n):
    """the function receive number and print all the integer from 1 to the
    number by recursion"""
    if n == 1:
        print(n)
    elif n > 0:  # the number have to positive!
        print_to_n(n-1)
        print(n)

def print_reversed(n):
    """the function receive number and print all the integer from number to
    1 by recursion"""
    if n == 1:
        print(n)
    elif n > 0:  # the number have to positive!
        print(n)
        print_reversed(n-1)

def has_divisor_smaller_than(n, i):
    """this function check if number has other different divisors from one, by
    check the modulo of the number divide by all the smaller numbers, and if
    the modulo is zero (and we divide by with number that is not 1) the number
    is prime number"""
    if i == 1:
        return True
    if n % i == 0:
        return False
    else:
        return has_divisor_smaller_than(n, i-1)

def is_prime(n):
    """the function receive number and check if the number is prime or not by
    using the previous function. if the number is negative the function return
    False."""
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        return has_divisor_smaller_than(n, n-1)

def find_divisors(n, i, lst):
    """the function receive number return list of all the integers dividers of
    him, by checking if the modulo of the number and the integer equal to zero
    and if he is a divisor of the number the function append him to the list of
    the divisors."""
    if i == 1:
        lst.append(i)
        return lst
    else:
        if n % i == 0:
            lst.append(i)
        return find_divisors(n, i - 1, lst)

def divisors(n):
    """the function receive number and return list of all the integers divisors
    of him, by using the previous function. if the number is zero the function
    return empty list. also, if the number is negative the function use 'abs'
    method(absolute value) and return the integers divisors."""
    new_lst = []
    if n == 0:
        return new_lst
    else:
        return sorted(find_divisors(n, abs(n), lst=[]))

def factorial(n):
    """the function receive number and return the factorial value of him.
    if the number is zero the function return 1
    (is we now that 0! equal to one"""
    if n == 0:
        return ONE
    else:
        return n * factorial(n-1)

def exp_n_x(n, x):
    """the function receive two numbers - 'n' and 'x' and return the
    'exponential function series sum' of them. the function call to the
    previous function to calculate the factorial value in exponential sum"""
    if n == 0:
        return ONE
    else:
        return x**n / factorial(n) + exp_n_x(n - 1, x)

def play_hanoi(hanoi, n, src, dest, temp):
    """this function solve the 'hanoi game'. first the function move n-1 disks
    from the originally tower to the temporary tower. then move the n disk (the
    one that still in the originally tower) to the destination tower. then the
    function move the n-1 disks who left in the temporary tower to the
    destination tower, then we do it recursive"""
    if n > 0:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n-1, temp, dest, src)

def print_binary_sequences_with_prefix(prefix, n):
    """this function print all the possible binary (zero or one) combination
     is 'n' length by recursion. if the length is zero then the function print
     empty string"""
    if n == 0:
        print(prefix)
    else:
        print_binary_sequences_with_prefix(prefix + ZERO_BINARY, n - 1)
        print_binary_sequences_with_prefix(prefix + ONE_BINARY, n - 1)

def print_binary_sequences(n):
    """this function print all the possible binary (zero or one) combination
     is 'n' length by calling the previous function. the function call the
     previous function with empty string to get all the combination (when
     we have at the first index zero or one)"""
    print_binary_sequences_with_prefix('', n)

def print_sequences_with_prefix(prefix, char_list, n):
    """this function receive a char list and return all the possible
    combination in length n from the list by using recursion. the same chart
    can appear more then one time in a sequences."""
    if n == 0:
        print(prefix)
    else:
        for char in char_list:
            print_sequences_with_prefix(prefix + char, char_list, n - 1)

def print_sequences(char_list, n):
    """this function receive a char list and return all the possible
    combination in length n by using the previous function."""
    print_sequences_with_prefix('', char_list, n)

def print_no_repetition_with_prefix(prefix, char_list, n):
    """this function receive a char list and return all the possible
    combination in length n from the list by using recursion but chart can
    appear only one time in a sequences. in every irritation the function
    slice the chat_list in call the function with this list without the chart
    to assure that he appear only one time"""
    if n == 0:
        print(prefix)
    else:
        for i in range(len(char_list)):
            print_no_repetition_with_prefix(prefix + char_list[i],char_list[:i]
                                            + char_list[i + ONE:], n-1)

def print_no_repetition_sequences(char_list, n):
    """this function receive a char list and return all the possible
    combination in length n from the list by using the previous function"""
    print_no_repetition_with_prefix('', char_list, n)

def no_repetition_sequences_list_with_prefix(prefix, char_list,new_list, n):
    """this function receive a char list and return list of all the possible
    combination in length n from the list by using recursion, but chart can
    appear only one time.in every irritation the function
    slice the chat_list in call the function with this list without the chart
    to assure that he appear only one time"""
    if n == 0:
        new_list.append(prefix)
    else:
        for i in range(len(char_list)):
            no_repetition_sequences_list_with_prefix\
                (prefix + char_list[i],char_list[:i] + char_list[i + ONE:],
                 new_list, n-1)

def no_repetition_sequences_list(char_list, n):
    """this function receive a char list and return list of all the possible
    combination in length n from the list by using the previous function"""
    new_lst = []
    no_repetition_sequences_list_with_prefix('', char_list, new_lst, n)
    return new_lst