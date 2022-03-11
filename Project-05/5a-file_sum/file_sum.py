# Author: Timur Guner
# Date: 2021-05-05
# Description: Project 5a takes a text file with a list of numbers, sums them up, and saves it a file called sum.txt

def file_sum(file_name):
    """This function takes a text file with a list of numbers, sums them up, and writes it a file called sum.txt"""

    # declare sum
    sum = 0.00

    # iterate through the open file and sum up each number (with closes file automatically
    with open(file_name, 'r') as infile:
        for line in infile:
            sum += float(line.strip())

    # create or overwrites a file called sum.txt and store the sum
    outfile = open('sum.txt','w')
    outfile.write(str(sum))
    outfile.close()