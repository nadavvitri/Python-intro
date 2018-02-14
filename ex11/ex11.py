#!/usr/bin/env python3
##########################################################
# file : ex11.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex6 2016-2017
# DESCRIPTION: This program contain many function that create mathematical
# function together. all the function draw with plot_func function.
# in this program there is also advanced function that return the solve of
# function, to return the invers function of function and more.
##########################################################
import math

EPSILON = 1e-5
DELTA = 1e-3
DELTA_2 = 0.01
SEGMENTS = 100
DEFAULT_FOR_X0 = -10000.0
DEFAULT_FOR_X1 = 10000.0
DOUBLE_THE_RANGE = 2
STARTING_RANGE_X1 = -80
STARTING_RANGE_X2 = 80
DEFAULT_COLOR = 'black'


def plot_func(graph, f, x0, x1, num_of_segments=SEGMENTS, c=DEFAULT_COLOR):
    """
    plot f between x0 to x1 using num_of_segments straight lines
    to the graph object. the function will be plotted in color c
    """
    # if there is no dotes or number of segments or color
    if not x0 or not x1 or not num_of_segments or not c:
        return None
    x2 = x0
    first_dot = (x2, f(x2))
    segment = (x1 - x0) / num_of_segments
    for i in range(num_of_segments):
        # each time draw line between two points (and after change the points)
        # until we draw all the function
        second_dot = (x2 + segment, f(x2 + segment))
        graph.plot_line(first_dot, second_dot, c)
        # change the points every iteration
        x2 += segment
        first_dot = second_dot


def const_function(c):
    """return the mathematical function f such that f(x) = c
    >>> const_function(2)(2)
    2
    >>> const_function(4)(2)
    4
    """
    return lambda x: c


def identity():
    """return the mathematical function f such that f(x) = x

    >>> identity()(3)
    3
    """
    return lambda x: x


def sin_function():
    """return the mathematical function f such that f(x) = sin(x)
    >>> sin_function()(math.pi/2)
    1.0
    """
    return lambda x: math.sin(x)


def sum_functions(g, h):
    """return f s.t. f(x) = g(x)+h(x)"""
    return lambda x: g(x) + h(x)


def sub_functions(g, h):
    """return f s.t. f(x) = g(x)-h(x)"""
    return lambda x: g(x) - h(x)


def mul_functions(g, h):
    """return f s.t. f(x) = g(x)*h(x)"""
    return lambda x: g(x) * h(x)


def div_functions(g, h):
    """return f s.t. f(x) = g(x)/h(x)"""
    return lambda x: g(x) / h(x)


def solve(f, x0=DEFAULT_FOR_X0, x1=DEFAULT_FOR_X1, epsilon=EPSILON):
    """
    Find a solution to f in the range x0 and x1
    assuming that f is monotnic.
    If no solution was found return None
    we use the binary search here
    """
    # if there is no solution for the function
    if f(x0) * f(x1) >= 0:
        return None
    c = (x0 + x1) / 2  # middle points of the function

    while f(x0) * f(x1) < 0:
        # each time create new middle point for search
        c = (x0 + x1) / 2
        if abs(f(c)) < epsilon:
            return c
        # ignore the right side and search in the left side
        elif f(x0) * f(c) > 0:
            x0 = c
        # ignore the left side and search in the right side
        else:
            x1 = c
    return c


def inverse(g, epsilon=EPSILON):
    """return f s.t. f(g(x)) = x"""
    def inverse_function(y):
        """
        return solution for g(x) - y (close to epsilon)
        """
        x1 = STARTING_RANGE_X1
        x2 = STARTING_RANGE_X2
        while (g(x1) - y) * (g(x2) - y) >= 0:
            # run until we found two points (if we don't double the range)
            # that there is point c between them that the function there
            # cross axis x.
            x1 *= DOUBLE_THE_RANGE
            x2 *= DOUBLE_THE_RANGE
        # return the solution for the new function g(x) - y by using solve
        return solve(lambda x: g(x) - y, x1, x2, epsilon)
    return inverse_function


def compose(g, h):
    """return the f which is the compose of g and h """
    return lambda x: g(h(x))


def derivative(g, delta=DELTA):
    """return f s.t. f(x) = g'(x)"""
    return lambda x: (g(x + delta) - g(x)) / delta


def definite_integral(f, x0, x1, num_of_segments=SEGMENTS):
    """
    return a float - the definite_integral of f between x0 and x1
    >>> round(definite_integral(const_function(3),-2,3),6)
    15.0
    """
    segment_length = ((x1 - x0) / num_of_segments)
    riemann_sum = 0
    x2 = x0 + segment_length
    for i in range(num_of_segments):
        riemann_sum += f((x0 + x2) / 2) * (x2 - x0)  # riemann sum for integral
        x0 = x2
        # update x2 point
        x2 += segment_length
    return riemann_sum


def integral_function(f, delta=DELTA_2):
    """return F such that F'(x) = f(x)"""

    def inverse_integral_function(x):
        """
        return the sum of the integral
        """
        num_of_segments = int(math.ceil(abs(x) / delta))
        # the formula for positive x
        if x > 0:
            return definite_integral(f, 0, x, num_of_segments)
        # the formula for negative x
        elif x < 0:
            return (-1) * definite_integral(f, x, 0, num_of_segments)
        # if x == 0
        else:
            return 0
    return inverse_integral_function


def function_0():
    """
    return f(x) = 4
    """
    return const_function(4)


def function_1():
    """
    return f(x) = 3 - sin(x)
    """
    const_number_3 = const_function(3)  # 3
    sin = sin_function()   # sin(x)
    final_function = sub_functions(const_number_3, sin)
    return final_function


def function_2():
    """
    return f(x) = sin(x-2)
    """
    const_number_2 = const_function(2) # 2
    same_number = identity() # x
    sub_func = sub_functions(same_number, const_number_2)  # x - 2
    sin = sin_function()  # sin(x)
    final_function = compose(sin, sub_func)  # sin(x-2)
    return final_function


def function_3():
    """
    return f(x) = 10/[2+sin(x)+(x^2)]
    """
    const_number_10 = const_function(10)  # 10
    sin = sin_function()  # sin(x)
    same_number = identity()  # x
    pow_number = mul_functions(same_number, same_number)  # x^2
    const_number_2 = const_function(2)  # 2
    sum_func_1 = sum_functions(const_number_2, sin)  # 2 + sin(x)
    sum_func_2 = sum_functions(sum_func_1, pow_number)  # 2 + sin(x) + (x^2)
    # 10/[2+sin(x)+(x^2)]
    final_function = div_functions(const_number_10, sum_func_2)
    return final_function


def function_4():
    """
    return f(x) = cos(x)/(sin(x)-2)
    """
    sin_x = sin_function()  # sin(x)
    cos_x = derivative(sin_x)  # cos(x)
    const_number_2 = const_function(2)  #
    sub_func = sub_functions(sin_x, const_number_2)  # sin(x) - 2
    final_function = div_functions(cos_x, sub_func)  # cos(x)/(sin(x)-2)
    return final_function


def function_5():
    """
    return f(x) = 0.1*(0.3x^2+0.7x-1)dx
    """
    const_number_01 = const_function(-0.1)  # -0.1
    const_number_03 = const_function(0.3)  # 0.3
    const_number_07 = const_function(0.7)  # 0.7
    const_number_1 = const_function(1) # 1
    same_number = identity() # x
    pow_number = mul_functions(same_number, same_number)  # x^2
    mul_func_1 = mul_functions(pow_number, const_number_03)  # 0.3x^2
    mul_func_2 = mul_functions(same_number, const_number_07)  # 0.7x
    sum_func = sum_functions(mul_func_1, mul_func_2)  # 0.3x^2 + 0.7x
    sub_func = sub_functions(sum_func, const_number_1)   # 0.3x^2 + 0.7x - 1
    integral = integral_function(sub_func)  # (0.3x^2+0.7x-1)dx
    # 0.1*(0.3x^2+0.7x-1)dx
    final_function = mul_functions(const_number_01, integral)
    return final_function


def function_6():
    """
    return f(x) = [cos(sin(x)) 0.3*cos(x)]*2
    """
    const_number_03 = const_function(0.3)  # 0.3
    const_number_02 = const_function(2)  # 2
    sin_x = sin_function()  # sin(x)
    cos_x = derivative(sin_x)  # cos(x)
    compose_func = compose(cos_x, sin_x)   # cos(sin(x))
    mul_func = mul_functions(const_number_03, cos_x)  # 0.3*cos(x)
    sub_func = sub_functions(compose_func, mul_func)  # cos(sin(x)) 0.3*cos(x)
    # [cos(sin(x)) 0.3 * cos(x)] * 2
    final_function = mul_functions(sub_func, const_number_02)
    return final_function


def function_7():
    """
    return inverse function of (2 - x^3)
    """
    const_number_02 = const_function(2)  # 2
    same_number = identity()  # x
    pow_number = mul_functions(same_number, same_number)  # x^2
    pow_number_2 = mul_functions(pow_number, same_number)  # x^3
    sub_func = sub_functions(const_number_02, pow_number_2)  # 2 - x^3
    final_function = inverse(sub_func)   # inverse function of (2 - x^3)
    return final_function


def ex11_func_list():
    """return list with the functions in q.13"""
    func_list = list()
    func_list.append(function_0())
    func_list.append(function_1())
    func_list.append(function_2())
    func_list.append(function_3())
    func_list.append(function_4())
    func_list.append(function_5())
    func_list.append(function_6())
    func_list.append(function_7())
    return func_list

# func that genrate the figure in the ex description
def example_func(x):
    return (x/5)**3


if __name__ == "__main__":
    import tkinter as tk
    from ex11helper import Graph
    import doctest
    doctest.testmod()
    master = tk.Tk()
    graph = Graph(master, -10, -10, 10, 10)
    plot_func(graph,example_func,-10,10,SEGMENTS,'red')
    color_arr = ['black', 'blue', 'red', 'green', 'brown', 'purple',
                 'dodger blue', 'orange']
    for f in ex11_func_list():
        plot_func(graph, f, -10, 10, SEGMENTS, 'red')
    master.mainloop()
