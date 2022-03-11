# Author: Timur Guner
# Date: 2021-05-26
# Description: Project 8b has uses a decorator function to record the time lapse of the sorts in bubble_sort and
#              insertion_sort. A function called compare_sort takes in bubble_sort and insertion_sort as parameters and
#              generates different random lists for those functions to sort. The function then plots that data.

import time
import random
import functools
from matplotlib import pyplot

def sort_timer(func):
    """
    A decorator function that is used to record and return the times of the bubble sort and insertion sort functions.
    This function returns the sort time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestart = time.perf_counter()      # start time
        func(*args, **kwargs)                # sort function call
        endtime = time.perf_counter()        # end time
        finishtime = endtime - timestart     # time elapsed
        return finishtime
    return wrapper

@sort_timer
def bubble_sort(a_list):
    """
    Sorts a_list in ascending order using bubble sort
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp

@sort_timer
def insertion_sort(a_list):
    """
    Sorts a_list in ascending order using insertion sort
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value

def compare_sorts(bubsort, insertsort):
    """
    The compare_sorts function takes in the two sort decorated sort function as parameters. It generates a random list
    of numbers that range from 1 - 10000. If first generates a list of a 1000 numbers calculates the time it took to
    sort, then it generates a list of 2000, 3000, ......, 10000. When all the times are recorded, they plotted to a
    graph to so the time lapse.
    """

    # bubbletime and inserttime are blank lists that will store the time elapsed for all list size sorts
    # listsize will be used for the x-axis in the plot and counter1000s is used in the while loop to increment list size
    bubbletime = []
    inserttime = []
    listsize = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    counter1000s = 1000

    while counter1000s <= 10000:

        # generate a blank list and store number from 1 - 10000 with size of counter1000s
        list1 = []
        for x in range(0, counter1000s):
            list1.append(random.randint(1, 10000))

        # copy the random list over listb and listi
        listb = list(list1)
        listi = list(list1)

        # call the bubblesort and insertsort functions and append the times to bubbletime and inserttime
        bubbletime.append(bubsort(listb))
        inserttime.append(insertsort(listi))

        # increment the while loop
        counter1000s += 1000

    # plot the two sets of sort times in a graph
    pyplot.plot(listsize, bubbletime, 'ro--', linewidth=2)
    pyplot.plot(listsize, inserttime, 'go--', linewidth=2)
    pyplot.xlabel("List Size")
    pyplot.ylabel("Sort Time in Seconds")
    pyplot.show()
    return

def main():

    compare_sorts(bubble_sort, insertion_sort)

if __name__ == '__main__':
    main()
