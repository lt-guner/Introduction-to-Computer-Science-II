# Author: Timur Guner
# Date: 2021-05-12
# Description: Project 6c creates a function called is_sequence and uses recursion to determine if the first string is
#              subsequence of the second string

def is_subsequence(string_a, string_b, pos_a=0, pos_b=0):
    """
    The function is_sequence takers in two strings as parameters. It then uses recursion to determine if the first
    string is subsequence of the second string.
    """

    # if the indexing of a is complete then we return True because we were able to iterate through list_a and matching
    # it to list_b before was completely iterated. Else we return False if list_b was iterated through.
    if pos_a == len(string_a):
        return True
    elif pos_b == len(string_b):
        return False

    # if the letters in both lists match, then we increment the indexes by one in the recursion. Else, we only increment
    # the index of list_b in the recursion
    if string_a[pos_a] == string_b[pos_b]:
        return is_subsequence(string_a, string_b, pos_a+1, pos_b+1)
    else:
        return is_subsequence(string_a, string_b, pos_a, pos_b+1)