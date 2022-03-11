# Author: Timur Guner
# Date: 2021-04-28
# Description: Project 4b has a box object initializes three inputs length, width, and height, to private data members
#              of the same name. It has a volume method to return the volume and three get methods for each of the
#              measurements. The is a separate function that takes a list of boxes and returns the volumes from smallest
#              to biggest using the insertion sort.

class Box():
    """The box class initializes three inputs length, width, and height, to private data members of the same name. It
       has a volume method to return the volume and three get methods for each of the measurements."""

    def __init__(self, length, width, height):
        """initializes private data members length, width, and height from user inputs"""
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        """returns the volume by multiplying length, width, and height"""
        return self._length * self._width * self._height

    def get_length(self):
        """returns the length"""
        return self._length

    def get_width(self):
        """returns the width"""
        return self._width

    def get_height(self):
        """returns the height"""
        return self._height


def box_sort(box_list):
    """The box_sort function that takes a list of boxes and and does an insertion sort based on volume"""

    # for loop and while loop to sort the Box list using insertion based on volume
    for slot in range(1, len(box_list)):
        box_object = box_list[slot]
        pos = slot - 1
        while pos >= 0 and box_list[pos].volume() < box_object.volume():
            box_list[pos + 1] = box_list[pos]
            pos -= 1
        box_list[pos + 1] = box_object

def main():
    b1 = Box(3.4, 19.8, 2.1)
    b2 = Box(1.0, 1.0, 1.0)
    b3 = Box(8.2, 8.2, 4.5)
    b4 = Box(.5, .2, .5)
    b5 = Box(12.0, 11.0, 23.0)
    b6 = Box(5.1, 5.3, 5.5)
    box_list = [b1, b2, b3, b4, b5, b6]

    print(box_list)
    for x in range(0, len(box_list)):
        print(box_list[x].get_length(),", ",box_list[x].get_width(),", ", box_list[x].get_height(),", ",box_list[x].volume())

    box_sort(box_list)

    print(box_list)
    for x in range(0, len(box_list)):
        print(box_list[x].get_length(),", ",box_list[x].get_width(),", ",box_list[x].get_height(),", ",box_list[x].volume())

if __name__ == '__main__':
    main()