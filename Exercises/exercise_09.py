"""
Exercise 9


1) Write a decorator function that prints the:
     - real world time taken to run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowlege of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math

def time_decorator(my_def):
    def internal_wrapper():
        t0 = time.time()
        def_result = my_def()
        t1 = time.time()
        print("'{}' finished in {} seconds".format(my_def.__name__, t1-t0))
        return "The size of return is {} ".format(sys.getsizeof(def_result))
    return internal_wrapper()

def for_loop():
    result_list =[]
    for i in range(1000000):
        result_list.append(i+1)
    return result_list

def list_comp():
    return [i+1 for i in range(1000000)]

def numpy_list():
    return numpy.arange(1,1000001)

def pandas_list():
    return pandas.Series(range(1,1000001))

def generator_list():
    return (i+1 for i in range(1000000))

# print(time_decorator(for_loop))
# print(time_decorator(list_comp))
# print(time_decorator(numpy_list))
# print(time_decorator(pandas_list))
# print(time_decorator(generator_list))

def for_loop_log():
    result_list =[]
    for i in range(1000000):
        result_list.append(math.log(i+1,10))
    return result_list

def list_com_log():
    return [math.log(i+1,10) for i in range(1000000)]

def numpy_list_log():
    return numpy.log10(numpy.arange(1,1000001))

def pandas_list_log():
    return pandas.Series(range(1,1000001)).apply(math.log10)

def generator_list_log():
    return (math.log(i+1,10) for i in range(1000000))

# print(time_decorator(for_loop_log))
# print(time_decorator(list_com_log))
# print(time_decorator(numpy_list_log))
# print(time_decorator(pandas_list_log))
# print(time_decorator(generator_list_log))