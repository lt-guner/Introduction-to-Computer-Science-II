# Author: Timur Guner
# Date: 2021-05-19
# Description: Project 7 is a program that creates a linked list using nodes. Node() is the node object and LinkedList()
#              is the linked list of nodes. LinkedList has add, remove, insert, reverse, and contains methods. It also
#              has a get_head method to return the beginning of the linked list and to_plain_list() to print out the
#              linked list in Python list form.

class Node():
    """
    Represents a node in a linked list
    """

    def __init__(self, data):
        """
        Initializes the node with private members _data and _next
        """
        self._data = data
        self._next = None

    def get_data(self):
        """
        returns node data
        """
        return self._data

    def get_next(self):
        """
        returns node next
        """
        return  self._next

    def set_data(self, data):
        """
        sets node data
        """
        self._data = data

    def set_next(self, next):
        """
        sets node next
        """
        self._next = next

class LinkedList():
    """
    LinkedList represents a linked list implementation of the List ADT. It contains five important methods to manipulate
    the list; add, remove, contains, insert, and reverse.

    - add: Adds a new node with data to the end of the linked list
    - remove: Removes a node based on the value passed by the user
    - contains: Returns true or false if the passed value is in one of the nodes
    - insert: Inserts a new node with a value based on the position parameter passed by the user
    - reverse: Reverses the entire linked list

    There is also a get_head() method to return the head node of the linked list and a method called to_plain_list()
    that returns the linked list in a Python list format
    """

    def __init__(self):
        """
        Initialize a blank linked list
        """
        self._head = None

    def get_head(self):
        """
        Returns the head of the linked list
        """
        return self._head

    def add(self, val):
        """
        Adds a new node with data to the end of the linked list. It uses a helper method called addhelper() to do this
        recursively
        """

        # add to front if list is empty, else call addhelper()
        if self._head is None:
            self._head = Node(val)
        else:
            self.addhelper(val, self.get_head())

    def remove(self, val):
        """
        Removes a node based on the value passed by the user. It uses a helper method called removehelper() to do this
        recursively
        """

        # If linked is blank exist
        if self._head is None:
            return

        # if user specifies that the new value needs to be the head, assign it to head. Else, call removehelper
        if self._head._data == val:
            self._head = self._head._next
        else:
            self.removehelper(val, self.get_head())

    def contains(self, key):
        """
        Returns true or false if the passed value is in one of the nodes. It uses a helper method called
        containshelper() to do this recursively.
        """

        # return false if linked list is None
        if self._head is None:
            return False

        # return true if key is at the head, else call containshelper to see if it exists in the linked list.
        if self._head._data == key:
            return True
        else:
            tracker = self.containshelper(key, self.get_head())
            if tracker == True:
                return True
            else:
                return False

    def insert(self, val, pos):
        """
        Inserts a new node with a value based on the position parameter passed by the user. It uses the method
        inserthelper() to do this recursively.
        """

        # insert at beginning if linked list is empty
        if self._head is None:
            self.add(val)
            return

        # insert at beginning is the used passed 0 as the position, else call inserthelper()
        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head._next = temp
        else:
            self.inserthelper(val,pos,self.get_head())

    def reverse(self):
        """"
        Reverses the entire linked list. It uses the method reversehelper() to do this recursively
        """
        self.reversehelper(None, self.get_head())

    def to_plain_list(self):
        """
        Returns a regular Python list from the linked list nodes
        """
        result = []
        results = self.to_plain_list_helper(self.get_head(), result)
        return results

    #------------------------------------------HELPER METHODS-------------------------------------------------------

    def addhelper(self, val, current=None):
        """
        addhelper helps the add method to recursively add nodes to the end of the linked list
        """

        # recursively call the addhelper method until current._next is None and then add the new noder
        if current._next is not None:
            self.addhelper(val, current._next)
        else:
            current._next = Node(val)

    def removehelper(self, val, current=None, previous=None):
        """
        removehelper helps the remove method remove a specified node recursively
        """

        # recursively call removehelper until the value is found and remove it the node
        if current is not None and current._data != val:
            self.removehelper(val, current._next, current)
        elif current is not None and current._data == val:
            previous._next = current._next

    def containshelper(self, key, current=None):
        """
        containshelper helps the contains method to find if the value is present, recursively
        """

        # if statement will recursively call containshelper to check and return true if it does. Saved in tracker
        if current is not None:
            if current._data == key:
                return True
            tracker = self.containshelper(key, current._next)

        # try and except is used here because we always want it to return true or false, even when tracker contains
        # nothing
        try:
            if tracker == True:
                return True
            else:
                return False
        except:
            return False

    def inserthelper(self, val, pos, current=None, counter=0):
        """
        inserthelper helps the insert method recursively insert a node
        """

        # recursively call inserthelper until counter is the same as position and break out of the recursion loop
        if counter <= pos:
            if current is None:
                return
            counter += 1
            self.inserthelper(val, pos, current._next, counter)

        # once counter matches position insert the new node at the location creating a new link
        if counter == pos:
            temp = current._next
            current._next = Node(val)
            current._next._next = temp

    def reversehelper(self, previous, current):
        """
        reversehelper helps the reverse method recursively reverse the linked lis
        """
        if current is not None:
            following = current._next
            current._next = previous
            previous = current
            current = following
            self._head = previous
            self.reversehelper(previous, current)

    def to_plain_list_helper(self, current, result):
        """
        to_plain_list_helper helps the to_plain_list recursively return the linked list as a Python list
        """
        if current is not None:
            result += [current._data]
            current = current._next
            self.to_plain_list_helper(current, result)
        return result





def main():
    list1 = LinkedList()
    list1.add(1)
    print(list1.to_plain_list())
    list1.add(2)
    print(list1.to_plain_list())
    list1.add(3)
    print(list1.to_plain_list())
    list1.add(4)
    print(list1.to_plain_list())
    list1.add(5)
    print(list1.to_plain_list())
    list1.add(6)
    print(list1.to_plain_list())
    list1.insert(7,5)
    print(list1.to_plain_list())
    list1.insert(8,6)
    print(list1.to_plain_list())
    print(list1.contains(1))
    print(list1.contains(3))
    print(list1.contains(0))
    print(list1.to_plain_list())
    list1.reverse()
    print(list1.to_plain_list())
    list1.remove(2)
    print(list1.to_plain_list())
    list1.remove(5)
    print(list1.to_plain_list())
    list1.remove(6)
    print(list1.to_plain_list())

if __name__ == '__main__':
    main()
