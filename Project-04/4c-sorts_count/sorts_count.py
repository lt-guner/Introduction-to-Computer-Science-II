# Author: Timur Guner
# Date: 2021-04-28
# Description: Project 4D list and does a bubble sort and insertion sort for count the comparisons ans exchanges between
#              for each type of sort

def bubble_count(list):
    """
    Sorts list in ascending order using bubble sort and returns the numbers of comparisons and exchanges in the loop
    """

    # Comparison and exchange counters
    comparisons = 0
    exchanges = 0

    # Double for loop to iterate through each index of length of list - 1 once the largest number is pushed to the back.
    # The number of exchanges is in the if statement and number of comparisons in the second for loop
    for pass_num in range(len(list) - 1):
        for index in range(len(list) - 1 - pass_num):
            if list[index] > list[index + 1]:
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp
                exchanges += 1
            comparisons += 1

    # return tuple of comparisons and exchanges
    return (comparisons, exchanges)


    for pass_num in range(input_bag.size() - 1):
        for index in range(input_bag.size() - 1 - pass_num):
            if input_bag.da.get_at_index(index) > input_bag.da.get_at_index(index + 1):
                temp = input_bag.da.get_at_index(index)
                input_bag.da.get_at_index(index) = input_bag.da.get_at_index(index + 1)
                input_bag.da.get_at_index(index + 1) = temp

def insertion_count(list):
    """
    Sorts list in ascending order using insertion sort and returns the numbers of comparisons and exchanges in the loop
    """

    # Comparison and exchange counters
    comparisons = 0
    exchanges = 0

    # Begin the outer index to track loop through list starting at index 1. Count the exchanges and the comparisons in
    # thw while loop. We still need to count the comparison if the while didn't trigger so we have an if statement to
    # add to comparisons if the left index was compared and small than the right index
    for index in range(1, len(list)):
        value = list[index]
        pos = index - 1
        while pos >= 0 and list[pos] > value:
            list[pos + 1] = list[pos]
            exchanges += 1
            pos -= 1
            comparisons += 1
        if list[pos] < value and pos >= 0:
            comparisons += 1
        list[pos + 1] = value

    # return tuple of comparisons and exchanges
    return (comparisons, exchanges)

def main():
    list1 = [23,5,87,16,44,-9,0,31,11,88,97,64]
    print(bubble_count(list1))
    print(list1)

    list2 = [23,5,87,16,44,-9,0,31,11,88,97,64]
    print(insertion_count(list2))
    print(list2)

if __name__ == '__main__':
    main()