# Author: Timur Guner
# Date: 2021-05-05
# Description: Project 5

import json

class NobelData():
    """
    The NobleData class initializes by taking in a json file and stores it in a private data member called
    noble_winners. It also has a search_noble method that takes the parameters year and category and returns a sorted
    list of surnames based on the input
    """

    def __init__(self):
        """init method opens a json file and stores in the private data member noble_winners"""
        with open("nobels.json", 'r') as infile:  # just 'r' since it's a text file
            self._nobel_winners = json.load(infile)

    def search_nobel(self, year, category):
        """
        The search_nobel method takes in parameters the parameter year and category and searches through noble_winners.
        The winners for the search criteria are stored in a list, sorted, and returned
        """

        # create a blank list
        list_of_winners= []

        # a concoction of for loops and if statements search through the dictionary and store the winners in a list
        for x in range (0, len(self._nobel_winners["prizes"])):
            if self._nobel_winners["prizes"][x]["year"] == year:
                if self._nobel_winners["prizes"][x]["category"] == category:
                    for i in range (0, len(self._nobel_winners["prizes"][x]["laureates"])):
                        list_of_winners.append(self._nobel_winners["prizes"][x]["laureates"][i]["surname"])

        # sort list and return
        list_of_winners.sort()
        return list_of_winners

def main():
    nd = NobelData()
    print(nd.search_nobel("2001", "economics"))

if __name__ == '__main__':
    main()

