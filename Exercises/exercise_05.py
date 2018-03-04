"""
Exercise 5

Word association with Nodes

When you type text into your phone, you may notice that a next word is automatically suggested to you before
you have even started typing a next word.

In this simplified example, we will create a node for each word in a string;
the "next" property for each Node will be a list of the words that have immediately followed that word.

** Reminder **
    Instance variables are: self.variable_name
    Class variables are: Class.variable_name

"""

import random
class Node:
    """
    Node class for word association that includes:
     * A class variable "node_dictionary" to store instances of the Node class where
        * Keys are words (strings) and values are Nodes (the Node instance corresponding to the word)
     * Instance variables "word" and "next"
        * word - a string
        * next - a list of words that follow this word (contains duplicate words)
     * A __str__ method that returns the word instance variable of the node
    """
    node_dictionary = {}

    # The class variable, node_dictionary (below) is a dictionary with words (strings) as keys and lists as values.


    def __init__(self, word):
        """
        Takes in 1 argument, the word associated with the Node and also
        initializes an instance variable "next" as an empty list.
        The empty list will store words (not Nodes) that follow this word
        :param word: A string
        """
        self.word = word
        self.next=[]

    def __str__(self):
        """
        returns the word associated with the Node
        :return: string
        """
        return


def print_all_nodes():
    """
    Call this function in your main function to print all of the nodes
    :return: None
    """
    for k,v in Node.node_dictionary.items():
        print("Word: {} \t Followed by: {}".format(k, v.next))
    return

def new_beatles():
    """
    This definition is purely for fun. Starting at the word "she", this will select a random word that could follow
    and repeat this process to print a new beatles song of the same format.
    :return: None
    """
    nd = Node.node_dictionary  # shortcut to the class dictionary

    new_song = []
    current_word = 'she'
    for i in range(23):
        new_song.append(current_word)
        if len(nd[current_word].next) > 0:
            current_word = random.choice(nd[current_word].next)
        else: # word has no next word available - so pick a random word
            current_word = random.choice(list(nd.keys()))

    print(' '.join(new_song[:5]))
    print(' '.join(new_song[5:12]))
    print(' '.join(new_song[12:16]))
    print(' '.join(new_song[16:]))
    return

def main():
    """
    When print_all_nodes() is called, the main definition for this script should print out (in any order):
    Word: she 	 Followed by: ['says', 'loves', 'loves']
    Word: says 	 Followed by: ['she']
    Word: loves 	 Followed by: ['you', 'you']
    Word: you 	 Followed by: ['and', 'know', 'and', 'know', 'should']
    Word: and 	 Followed by: ['you', 'you']
    Word: know 	 Followed by: ['that', 'you']
    Word: that 	 Followed by: ['cant']
    Word: cant 	 Followed by: ['be']
    Word: be 	 Followed by: ['bad', 'glad']
    Word: bad 	 Followed by: ['yes']
    Word: yes 	 Followed by: ['she']
    Word: should 	 Followed by: ['be']
    Word: glad 	 Followed by: []
    :return: None
    """

    # This is the text we will by analyzing
    beatles = """She says she loves you
    And you know that cant be bad
    Yes she loves you
    And you know you should be glad
    """
    # In this following example of list comprehension, we process the text above into a list.
    # The "if word" check at the end, will return false if word is an empty string
    word_list = [word.lower().replace('\n','') for word in beatles.split(' ') if word]

    previous_word = None
    for word in word_list:
        if not word in Node.node_dictionary:
            Node.node_dictionary[word] =Node(word)
        if previous_word:
            Node.node_dictionary[word].next.append(previous_word)
        previous_word = word

    print_all_nodes()
    # new_beatles()
    return



if __name__ == '__main__':
    main()











