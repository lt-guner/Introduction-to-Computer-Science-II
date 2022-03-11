# Author: Timur Guner
# Date: 2021-05-26
# Description: Project 8a has that called count_seq that begins with the number two. To get a term of the sequence,
#              enumerate how many there are of each digit (in a row) in the previous term. For example, the first term
#              is "one 2", which gives us the second term "12". That term is "one 1" followed by "one 2", which gives us
#              the third term "1112". That term is "three 1" followed by "one 2", or 3112. Etc.

def count_seq():
    """
    The count_seq functions begins with 2 in the generator and produces a sequence. To get a term of the sequence,
    enumerate how many there are of each digit (in a row) in the previous term. For example, the first term
    is "one 2", which gives us the second term "12". That term is "one 1" followed by "one 2", which gives us
    the third term "1112". That term is "three 1" followed by "one 2", or 3112. Etc.
    """

    # start with numstring as 2
    numstring ="2"

    # infinite loop to continuously generator new numbers in the generate
    while numstring:

        # yield the numstring to be pulled
        yield numstring

        # if this numstring is only 1 digit long make numstring 1 + numstring
        if numstring == numstring[0]:
            numstring = "1" + numstring

        else:
            # set x and tempstring for loop counter and storing a new string
            x = 0
            tempstring = ""

            # iterate through the previous numstring to generate a new numstring based on the specs in the docstring
            while x < len(numstring):
                try:
                    # tempval is assigned the current iteration of the previous numstring
                    # count is 0
                    tempval = numstring[x]
                    count = 0

                    # current numstring slot = tempval increment counts and x
                    while numstring[x] == tempval:
                        count += 1
                        x+=1
                except:
                    x+=1

                # append count and tempval to the new tempstring
                tempstring += str(count) + tempval

            # once tempstring is done generating data, assign it to numstring
            numstring = tempstring

def main():
    test = count_seq()
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))

if __name__ == '__main__':
    main()
