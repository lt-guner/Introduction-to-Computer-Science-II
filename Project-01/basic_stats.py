# Author: Timur Guner
# Date: 2021-04-07
# Description: Project 1 imports the statistics module to use in finding the mean, median, and mode from a list of
#              students. The students are created from a class object called Student() that takes two parameters, name
#              and age. It assigns these variables to two private data members. The class also has a get method that
#              returns the age. A separate function from the class takes a list of students and returns the mean,
#              median and mode list. The variable that is returned is a tuple.

# statistics module is imported to find mean, median, and mode
import statistics

# The Student class used for storing student name and age and pulling the student's age
class Student():

    """The Student Class stores the student's name and grade as private data members. It also has a get method to return
    the grade"""

    def __init__(self, name, grade):

        """The init method initials two private to store name and grade from the input values"""

        self._name = name
        self._grade = grade

    def get_grade(self):

        """The get_grade method returns the grade of the student"""

        return self._grade

# This function is used to find the mean, median, and mode from a list of student objects
def basic_stats(list_of_students):

    """The basic_stats function takes a list of student objects and returns the mean, median, and mode as a tuple"""

    # A blank list is created that will store a list of student ages
    list_of_ages = []

    # The for loop iterates through the list of students to grab the the age with get_grade method and append it to
    # list_of_ages
    for x in range(0, len(list_of_students)):
        temp_age = list_of_students[x].get_grade()
        list_of_ages.append(temp_age)

    # Three variables are created to find the mean, median, and mode in list_of_ages using the mean, median, and mode
    # functions from statistics
    mean = float(statistics.mean(list_of_ages))
    median = float(statistics.median(list_of_ages))
    mode = float(statistics.mode(list_of_ages))

    # tuple_ages stores the above variables a tuple.
    tuple_ages = (mean, median, mode)

    # returns tuple_age
    return tuple_ages