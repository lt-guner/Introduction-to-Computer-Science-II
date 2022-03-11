# Author: Timur Guner
# Date: 2021-05-05
# Description: Project 5c creates a class called SatData(). It has an init method that opens a json file and stores it
#              in in a private data member called sats. It also has a save_as_csv method that takes a list of DBNs and
#              pulls the corresponding data from sats then saves it to as csv file

import json


class SatData():
    """SatData is class has an init method that opens a json file and stores it in in a private data member called sats.
       It also has a save_as_csv method that takes a list of DBNs, then pulls the corresponding data from sats and saves
       it to as csv file"""

    def __init__(self):
        """init method opens a json file and stores in the private data member noble_winners"""
        with open("sat.json", 'r') as infile:  # just 'r' since it's a text file
            self._sats = json.load(infile)

    def save_as_csv(self, dbns):
        """The save_as_csv method that takes a list of DBNs, then pulls the corresponding data from sats and saves
           it to as csv file"""

        # Create a blank list that is used for sorting
        list_to_csv = []

        # Nested for loops and if statements that search through sats and saves the data into a list
        for x in range(0, len(self._sats["data"])):
            for i in range(0, len(dbns)):
                if self._sats["data"][x][8] == dbns[i]:
                    list_to_csv.append(
                        "\"" + self._sats["data"][x][8] + "\",\"" + self._sats["data"][x][9] + "\",\"" +
                        self._sats["data"][x][10] + "\",\"" + self._sats["data"][x][11] + "\",\"" +
                        self._sats["data"][x][12] + "\",\"" + self._sats["data"][x][13] + "\"" + "\n")

        # Sort the list
        list_to_csv.sort()

        # Write the list to output.csv using with and for loops and this also hard codes the headers
        with open('output.csv', 'w') as outfile:
            outfile.write(
                "\"DBN\"," + "\"School Name\"," + "\"Number of Test Takers\"," + "\"Critical Reading Mean\"," +
                "\"Mathematics Mean\"," + "\"Writing Mean\"" + "\n")
            for i in list_to_csv:
                outfile.write(i)

def main():
    sd = SatData()
    dbns = ["02M303", "02M294", "01M450", "32K552", "02M418", "79X490", "21K540", "17K382", "29Q283"]
    sd.save_as_csv(dbns)

if __name__ == '__main__':
    main()