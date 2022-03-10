# Author: Timur Guner
# Date: 2021-04-21
# Description: Project 3

class LibraryItem():
    """The LibraryItem class is a parent class used for Book, Album, and Movie class items. The class contains six
       private data member; library_item_id, title, location, date_checked_out, checked_out_by, and requested_by. Each
       each of the data members has a get method. There are are set methods for location, date_checked_out,
       checked_out_by, and requested_by. When the object is created it takes two parameters for library_item_id and
       title. The other four members have default parameters. The set methods are used to change those data members
       as needed."""

    def __init__(self, item_id, title):
        """The init method creates six private data members; library_item_id, title, location, date_checked_out,
           checked_out_by, and requested_by. The method takes two parameters for library_item_id and title. The other
           four parameters are set with default parameters"""
        self._library_item_id = item_id
        self._title = title
        self._location = "ON_SHELF"
        self._date_checked_out = 0
        self._checked_out_by = None
        self._requested_by = None

    def get_item_id(self):
        """The get_item_id method returns the library_item_id"""
        return self._library_item_id

    def get_title(self):
        """The get_title method returns the title"""
        return self._title

    def get_location(self):
        """The get_location method returns the location"""
        return self._location

    def get_checked_out_by(self):
        """The get_checked_out_by method returns the Patron object who checked out the item"""
        return self._checked_out_by

    def get_requested_by(self):
        """The get_requested_by returns the Patron object that requested the item to be on hold"""
        return self._requested_by

    def get_date_checked_out(self):
        """The get_date_checked_out returns the date the item was checked out"""
        return self._date_checked_out

    def set_date_checked_out(self, current_date):
        """The set_date_checked_out method assigns the current date of the library to the date the item is checked out"""
        self._date_checked_out = current_date

    def set_checked_out_by(self, patron_id):
        """The set_check_out_by method assigns the Patron object that checked out the book"""
        self._checked_out_by = patron_id

    def set_requested_by(self, patron_id):
        """The set_requested_by method assigns the Patron object that requested the item"""
        self._requested_by = patron_id

    def set_location(self, location_status):
        """the set_location method assigns the location of the item"""
        self._location = location_status


class Book(LibraryItem):
    """The Book class inherits from the LibraryItem class, while also adding two new data members; author and
       check_out_length. It has two get methods for these two new data members"""

    def __init__(self, item_id, title, author):
        """The init method inherits from the LibraryItem class using super() and adding author and check_out_length"""
        super().__init__(item_id,title)
        self._author = author
        self._check_out_length = 21

    def get_check_out_length(self):
        """The get_check_out_length returns check_out_length which is the allowable days a Book can be checked out"""
        return self._check_out_length

    def get_author(self):
        """the get_author returns the author"""
        return self._author

class Album(LibraryItem):
    """The Album class inherits from the LibraryItem class, while also adding two new data members; artist and
       check_out_length. It has two get methods for these two new data members"""

    def __init__(self, item_id, title, artist):
        """The init method inherits from the LibraryItem class using super() and adding artist and check_out_length"""
        super().__init__(item_id, title)
        self._artist = artist
        self._check_out_length = 14

    def get_check_out_length(self):
        """The get_check_out_length returns check_out_length which is the allowable days a Album can be checked out"""
        return self._check_out_length

    def get_artist(self):
        """The get_artist returns the artist"""
        return self._artist

class Movie(LibraryItem):
    """The Movie class inherits from the LibraryItem class, while also adding two new data members; movie and
       check_out_length. It has two get methods for these two new data members"""

    def __init__(self, item_id, title, director):
        """The init method inherits from the LibraryItem class using super() and adding director and check_out_length"""
        super().__init__(item_id, title)
        self._director = director
        self._check_out_length = 7

    def get_check_out_length(self):
        """The get_check_out_length returns check_out_length which is the allowable days a Movie can be checked out"""
        return self._check_out_length

    def get_director(self):
        """The get_director returns the director"""
        return self._director

class Patron():
    """The Patron class is used to create a member for the Library. It has four private data members; patron_id, name,
       checked_out_items, and fine_amount. patron_id and name are passed to the class when it is first initialized.
       checked_out_items is a list of all current items checked out by the Patron and fine_amount is the penalties for
       late returns. There are get methods for all four data members. There are two methods that add and remove items
       from checked_out_list; add_library_item and remove_library_item. There is also an amend_fine method that adds
       late fees and removes fines when a customer pays"""

    def __init__(self, patron_id, name):
        """The init method takes two parameters upon initializing; patron_id and name. These are assigned to private
           data members patron_id and name. Two more data members are initialized with default values to track the
           checked out items and the current fines; check_out_items and fine_amount"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.00

    def get_patron_id(self):
        """The get_patron_id method returns the patron id"""
        return self._patron_id

    def get_name(self):
        """The get_name method returns the patron name"""
        return self._name

    def get_checked_out_items(self):
        """The get_checked_out_items returns the list of checked_out_items by the patron"""
        return self._checked_out_items

    def get_fine_amount(self):
        """The get_fine_amount returns the fine_amount balance"""
        return self._fine_amount

    def add_library_item(self, library_item):
        """The add_library_item adds a LibraryItem to the checked_out_items list"""
        self._checked_out_items.append(library_item)

    def amend_fine(self, dollar):
        """The amend_fine method is used to add late fees and reduce fees when paid"""
        self._fine_amount += dollar

    def remove_library_item(self, library_item):
        """The remove_library_item removes a LibraryItem from the checked_out_items list"""
        self._checked_out_items.remove(library_item)

class Library():
    """The Library class is used to create and keep track of everything in the Library object. It has three private
       data members; holdings, members, and current_date. These data members are used to store LibraryItems objects,
       Patron objects, and the current date which is the number of days since the library opened. There are three
       methods used to add items, patrons, and increase the date; add_library_item, add_patron, and
       increment_current_date. The increment_current_date method increments the current_date by one and amends fines as
       needed. There are two lookup functions to return LibraryItem and Patron objects by their unique ids;
       lookup_library_item_from_id and lookup_patron_by_id. The check_out_library_item method takes in two parameters,
       patron_person_id and library_item_id, and allows the Patron to checkout as long as the LibraryItem object is on
       the shelf or on hold for them. The request_library_item allows a Patron to reserve the book and have it placed on
       hold for them. The parameters for that method are patron_person_id and library_item_id. The return_library_item
       takes the library_item_id and checks in the book when it is returned and is removed from the Patron's checked out
       items. The pay_fine method is used by the Patron to pay off any fines that are due."""

    def __init__(self):
        """The init method is used to create three private data members holdings, members, and current_date"""
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, library_item):
        """The add_library_item method adds a LibraryItem to holdings"""
        self._holdings.append(library_item)

    def add_patron(self, patron_person):
        """The add_patron method adds a Patron to members"""
        self._members.append(patron_person)

    def lookup_library_item_from_id(self, library_item_id):
        """The lookup_library_item_from_id method takes the parameter, library_item_id, and returns the LibraryItem
           object if it exits. If it does not exist it returns None"""

        # Nested for loop and if statement for find if the LibraryItem exists
        for x in range(0, len(self._holdings)):
            if self._holdings[x].get_item_id() == library_item_id:
                return self._holdings[x]

        # Returns None if the item doesnt exist
        return None

    def lookup_patron_from_id(self, patron_person_id):
        """The lookup_patron_from_id method takes the parameter, patron_person_id, and returns the Patron object if it
           exits. If it does not exist it returns None"""

        # Nested for loop and if statement for find if the Patron exists
        for x in range(0, len(self._members)):
            if self._members[x].get_patron_id() == patron_person_id:
                return self._members[x]

        # Return None if it doesn't exist
        return None

    def check_out_library_item(self, patron_person_id, library_item_id):
        """The checked_out_library_item method allows a Patron to checkout a LibraryItem in holding. It requires two
           parameters method; patron_person_id and library_item_id. If neither of them exist, then a message is returned
           letting them know that the LibraryItem or Patron object does not exists. If the item is on hold by another
           Patron, the the Patron gets a message that item is on hold. If the item is already checked out, then the
           Patron is shown a message to let them know that. If everything passes, the LibraryItem attributes
           checked_out_by, date_checked_out, location, and requested_by (if needed) are updated. The LibraryItem is
           added to the Patrons checked_out_items list and a message is returnes 'checkout successful'"""

        # Variables used for tracking and slot numbers for later user
        patron_ticker = 0
        library_item_ticker = 0
        holding_slot = 0
        patron_slot = 0

        # Nested for loop and if statement for find if the Patron exists. If it does set patron_ticker to 1 and
        # patron_slot to x
        for x in range(0, len(self._members)):
            if self._members[x].get_patron_id() == patron_person_id:
                patron_ticker = 1
                patron_slot = x

        # If the patron_ticker is 0 then return Patron not found
        if patron_ticker == 0:
            return "patron not found"

        # Nested for loop and if statement for find if the LibraryItem exists. If it does set library_item_ticker to 1
        # and holding_slot to x
        for x in range(0, len(self._holdings)):
            if self._holdings[x].get_item_id() == library_item_id:
                library_item_ticker = 1
                holding_slot = x

        # If library_item_ticker is 0 return Item not found
        if library_item_ticker == 0:
            return "item not found"

        # If the item is checked out return Item already checked out
        if self._holdings[holding_slot].get_location() == "CHECKED_OUT" and \
        self._holdings[holding_slot].get_item_id() == library_item_id:
            return "item already checked out"

        # If the item is on hold by another Patron return item on hold by other patron
        if self._holdings[holding_slot].get_location() == "ON_HOLD_SHELF" and \
        self._holdings[holding_slot].get_item_id() == library_item_id and \
        self._holdings[holding_slot].get_requested_by() != self._members[patron_slot]:
            return "item on hold by other patron"

        # If everything above passes then set the checked_out_by to the Patron and date_checked_out current_date
        self._holdings[holding_slot].set_checked_out_by(self._members[patron_slot])
        self._holdings[holding_slot].set_date_checked_out(self._current_date)

        # If the item was on hold by this Patron then set requested_by to None
        if self._holdings[holding_slot].get_item_id() == library_item_id and \
        self._holdings[holding_slot].get_requested_by() == self._members[patron_slot]:
            self._holdings[holding_slot].set_requested_by(None)

        # Set location to CHECKED_OUT and add the LibraryItem to the Patron's checked_out_items
        self._holdings[holding_slot].set_location("CHECKED_OUT")
        self._members[patron_slot].add_library_item(self._holdings[holding_slot])

        return "check out successful"

    def return_library_item(self, library_item_id):
        """The return_library_item method takes in the parameter library_item_id. If the the item does not exist or is
           already in the library, then messages stating that are returned accordingly. If the object is in a Patron's
           checked_out_item list, then the book is added back ON_SHELF or ON_HOLD_SHELF if someone has requested it.
           The data member checked_out_by in LibraryItem is set to None and the LibraryItem is removed from the Patron's
           checked_out_list"""

        # Variables used for tracking and slot numbers for later user
        library_item_ticker = 0
        holding_slot = 0

        # Nested for loop and if statement to find if the item exists. If it does library_item_ticker is to 1 and
        # holding_slot is set to x
        for x in range(0, len(self._holdings)):
            if self._holdings[x].get_item_id() == library_item_id:
                library_item_ticker = 1
                holding_slot = x

        # if library_item_ticker is 0 return item not found
        if library_item_ticker == 0:
            return "item not found"

        # if item is not checked out return item already in library
        if self._holdings[holding_slot].get_location() != "CHECKED_OUT":
            return "item already in library"

        # This nested for loop and if statement returns the book. If it is requested by another Patron, then put it on
        # the hold shelf. Otherwise, put it on the shelf. Return "return successful"
        for x in range(0, len(self._members)):
            check_out_list = self._members[x].get_checked_out_items()
            for y in range (0, len(check_out_list)):
                if check_out_list[y] == self._holdings[holding_slot]:
                    if self._holdings[holding_slot].get_requested_by() is not None:
                        self._holdings[holding_slot].set_location("ON_HOLD_SHELF")
                    else:
                        self._holdings[holding_slot].set_location("ON_SHELF")
                    self._holdings[holding_slot].set_checked_out_by(None)
                    self._members[x].remove_library_item(check_out_list[y])
                    return "return successful"

    def request_library_item(self, patron_person_id, library_item_id):
        """The request_library_item method takes two parameters; patron_person_id and library_item_id. If neither of
           those ids exist, then a message is returned accordingly. If the item is already on hold, then the Patron
           will receive that message. If the book is reservable, then the LibraryItem attribute request_by is updated
           with the Patron object. If the item is ON_SHELF it is moved to ON_HOLD_SELF, otherwise the Patron needs to
           wait until the book is returned. Once this is complete the request successful message is returned"""

        # Variables used for tracking and slot numbers for later user
        patron_ticker = 0
        library_item_ticker = 0
        holding_slot = 0
        patron_slot = 0

        # Nested for loop and if statement for find if the Patron exists. If it does set patron_ticker to 1 and
        # patron_slot to x
        for x in range(0, len(self._members)):
            if self._members[x].get_patron_id() == patron_person_id:
                patron_ticker = 1
                patron_slot = x

        # If the patron_ticker is 0 then return Patron not found
        if patron_ticker == 0:
            return "patron not found"

        # Nested for loop and if statement to find if the item exists. If it does library_item_ticker is to 1 and
        # holding_slot is set to x
        for x in range(0, len(self._holdings)):
            if self._holdings[x].get_item_id() == library_item_id:
                library_item_ticker = 1
                holding_slot = x

        # if library_item_ticker is 0 return item not found
        if library_item_ticker == 0:
            return "item not found"

        # If the item is already on hold return
        if self._holdings[holding_slot].get_requested_by() is not None:
            return "item already on hold"

        # If the above passes set requested_by to the Patron
        self._holdings[holding_slot].set_requested_by(self._members[patron_slot])

        # If its on the shelf put it on the hold shelf
        if self._holdings[holding_slot].get_location() == "ON_SHELF":
            self._holdings[holding_slot].set_location("ON_HOLD_SHELF")

        # return request successful
        return "request successful"

    def pay_fine(self, patron_person_id, dollar_amount):
        """The pay_fine method takes parameters patron_person_id and dollar_amount. If the patron_person_id does not
           exist, then a message is returned accordingly. Otherwise, the Patron's fines are reduced by the
           dollar_amount"""

        # Variables used for tracking and slot numbers for later user
        patron_ticker = 0
        patron_slot = 0

        # Nested for loop and if statement for find if the Patron exists. If it does set patron_ticker to 1 and
        # patron_slot to x
        for x in range(0, len(self._members)):
            if self._members[x].get_patron_id() == patron_person_id:
                patron_ticker = 1
                patron_slot = x

        # If the patron_ticker is 0 then return Patron not found
        if patron_ticker == 0:
            return "patron not found"

        # Amend the fine amount
        self._members[patron_slot].amend_fine(-(dollar_amount))

        # return payment successful
        return "payment successful"

    def increment_current_date(self):
        """The increment_date method increments the current_date by one. If checks to see if any checked out items are
           past their due date and increments the fine amount by the extra dat that was added."""

        # increment current date by 1
        self._current_date += 1

        # add fines to each LibraryItem that is overdue, which 10 cents a day
        for x in range(0, len(self._members)):
            check_out_list = self._members[x].get_checked_out_items()
            for y in range(0, len(check_out_list)):
                for z in range(0, len(self._holdings)):
                    if check_out_list[y] == self._holdings[z]:
                        if (self._current_date - self._holdings[z].get_check_out_length()) > \
                        self._holdings[z].get_date_checked_out():
                            self._members[x].amend_fine(.10)

def main():

    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")
    print(b1.get_author())
    print(a1.get_artist())
    print(m1.get_director())

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

    print(p1.get_patron_id())
    #print(p2.get_name())
    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_library_item(m1)
    lib.add_patron(p1)
    lib.add_patron(p2)

    print(lib.check_out_library_item("bcd", "456"))
    print(lib.check_out_library_item("abc","456"))
    print(lib.check_out_library_item("abc", "457"))
    print(lib.check_out_library_item("abd", "456"))
    print(lib.request_library_item("abc","456"))
    print(lib.check_out_library_item("bcd", "345"))
    print(lib.request_library_item("abc", "345"))
    print(lib.request_library_item("bcd", "567"))
    print(lib.request_library_item("abc", "567"))
    print(lib.request_library_item("abc", "568"))
    print(lib.request_library_item("abd", "567"))

    print(p1.get_checked_out_items())
    print(b1.get_requested_by())
    print(p2.get_checked_out_items())
    print(m1.get_checked_out_by())
    print(m1.get_requested_by())
    print(a1.get_location())
    print(a1.get_checked_out_by())
    print(a1.get_requested_by())
    print(b1.get_location())
    print(m1.get_location())

    for i in range(57):
        lib.increment_current_date()

    print(p1.get_fine_amount())
    print(p2.get_fine_amount())
    fine = p2.get_fine_amount()
    print(lib.return_library_item("345"))
    print(lib.return_library_item("456"))
    print(lib.return_library_item("567"))

    print(lib.pay_fine("456",fine))
    print(lib.pay_fine("bcd", fine))
    print(a1.get_location())
    print(a1.get_requested_by())
    print(b1.get_location())
    print(b1.get_requested_by())
    print(m1.get_location())
    print(m1.get_requested_by())

if __name__ == '__main__':
    main()