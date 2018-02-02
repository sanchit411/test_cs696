"""
exercise_02
2/1/2018
"""


def first_elements(my_list, n):
    """
    returns the first n elements in a list.
    EX: first_element([0, 1, 2, 3], 2) should return [0, 1]
    :param my_list: a non-empty list
    :param n: an integer greater than 0
    :return: a list of length n
    """
    return my_list[0:n]

def first_element(my_list, n):
    """
    returns the last n elements in a list.
    EX: last_element([0, 1, 2, 3], 2) should return [2, 3]
    :param my_list: a non-empty list
    :param n: an integer greater than 0
    :return: a list of length n
    """
    start = len(my_list) - n
    return my_list[start:len(my_list)]

def n_elements(my_list, start, n):
    """
    returns n elements in a list, starting at the position "start".
    EX: n_elements([0, 1, 2, 3, 4, 5], 2, 3) should return [2, 3, 4]
    :param my_list: a non-empty list
    :param start: a non-negative integer
    :param n: an integer greater than 0
    :return: a list of length n
    """
    last = start + n
    return my_list[start:last]

def count_letters(s):
    """
    returns a dictionary containing each letter in s as a key and
    the number of times each letter has occurred as the value
    :param s: a string
    :return: a dictionary
    """
    dict = {}
    for letter in s:
        if letter in dict:
            dict[letter] +=1
        else:
            dict[letter] = 1
    return dict

def protein_wight(protein):
    """
    Given a string of amino acids coding for a protein, return the total mass of the protein
    :param protiein: a string containing only G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    :return: a float
    """
    AMINO_ACID_WEIGHTS = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
                          'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
                          'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
                          'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06}
    sum = 0.0
    for amino in protein:
        sum += AMINO_ACID_WEIGHTS[amino]
    return sum

