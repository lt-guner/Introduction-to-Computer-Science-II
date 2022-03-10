# Author: Timur Guner
# Date: 2021-04-14
# Description: Project 2 creates simple store by using three classes; Product, Customer, and Store.
#
#              The Product class establishes a product for the store. It has five private data members; product id,
#              product name, description, price, and quantity available. The class has five get methods to pull each of
#              the private data members; get_product_id, get_title, get_description, get_price, and
#              get_quantity_available. There is one method called decrease_quantity. This method decreases the quantity
#              by 1 each time one of that product is purchased.
#
#              The Customer class is used to store customer information for the store. It contains four private data
#              members; name, customer id, premium member and cart. It has four get methods to pull each of the data
#              members; get_name, get_customer_id, get_cart and is_premium_member. This class has an
#              add_product_to_cart, which adds items to the customers cart for Store, and a method that is called
#              empty_cart that empties the cart on checkout
#
#              The Store class creates a store that stores data for inventory and customers. It has two private data
#              members; inventory and members. Inventory is a list of the Product class objects are passed to the Store.
#              Members is a list of all the Customer class objects added to the store. There are two methods to add
#              Product and Customer objects to those lists; add_product and add_member. There are three look up methods
#              in this class; lookup_product_from_id which lookups a product by id and returns the Product object,
#              lookup_member_from_id which looks up a customer by id and returns the Customer object, and product_search
#              which looks up products by keywords and returns the product id for each product that contains that
#              keyword. The method add_product_to_member_cart adds items to the cart of the Customer object. Last, there
#              is check_out_member which allows the active member purchase the items that were stored in their cart and
#              empties the cart after.

class InvalidCheckoutError(Exception):
    """This is an exception that will be issued when there is an invalid id passed to the check_out_member in Store."""
    pass

class Product():
    """The Product class establishes a product for the store. It has five private data members; product id, product
       name, description, price, and quantity available. The class has five get methods to pull each of the private data
       members; get_product_id, get_title, get_description, get_price, and get_quantity_available. There is one method
       called decrease_quantity. This method decreases the quantity by 1 each time one of that product is purchased."""

    def __init__(self, productid, productname, description, price, quantity_available):
        """Establishes the private data members for Product class; _productid, _productname, _description, _price,
           _quantity_avaiable"""
        self._productid = productid
        self._productname = productname
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        """returns product id"""
        return self._productid

    def get_title(self):
        """returns the product name"""
        return self._productname

    def get_description(self):
        """returns the description of the product"""
        return self._description

    def get_price(self):
        """returns the price of the product"""
        return self._price

    def get_quantity_available(self):
        """returns the available quantity of the product"""
        return self._quantity_available

    def decrease_quantity(self):
        """decreases the quantity by one for each item in checkout"""
        self._quantity_available -= 1

class Customer():
    """The Customer class is used to store customer information for the store. It contains four private data members;
       name, customer id, premium member and cart. It has four get methods to pull each of the data members; get_name,
       get_customer_id, get_cart and is_premium_member. This class has an add_product_to_cart, which adds items to the
       customers cart for Store, and a method that is called empty_cart that empties the cart on checkout"""

    def __init__(self, name, customerid, premium_member):
        """Establishes four private data members for customer name, id, premium membership, and cart which is empty"""
        self._name = name
        self._customerid = customerid
        self._premium_member = premium_member
        self._cart = []

    def get_name(self):
        """returns the customer's name"""
        return self._name

    def get_customer_id(self):
        """returns the customer's id"""
        return self._customerid

    def get_cart(self):
        """returns the cart"""
        return self._cart

    def is_premium_member(self):
        """returns if the customer is a premium member or not"""
        return self._premium_member

    def add_product_to_cart(self, productid):
        """This method puts items into the customers cart when the customer adds items from the store"""

        # Establish an initial variable to be used to check if the product already exists
        product_ticker = 0

        # The nested for loop and if statement checks to see if the product was already added to cart and sets
        # product_ticker to 1 if it does exist
        for x in range(0, len(self._cart)):
            if self._cart[x][0] == productid:
                product_ticker = 1

        # If the product exists add 1 more to the quantity, else add the new item to the cart
        if product_ticker == 1:
            for x in range(0, len(self._cart)):
                if self._cart[x][0] == productid:
                    self._cart[x][1] += 1
        else:
            self._cart.append([productid, 1])

    def empty_cart(self):
        """Empties the cart when this method is called"""
        self._cart = []

class Store():
    """The Store class creates a store that stores data for inventory and customers. It has two private data members;
       inventory and members. Inventory is a list of the Product class objects are passed to the Store. Members is a
       list of all the Customer class objects added to the store. There are two methods to add Product and Customer
       objects to those lists; add_product and add_member. There are three look up methods in this class;
       lookup_product_from_id which lookups a product by id and returns the Product object, lookup_member_from_id which
       looks up a customer by id and returns the Customer object, and product_search which looks up products by keywords
       and returns the product id for each product that contains that keyword. The method add_product_to_member_cart
       adds items to the cart of the Customer object. Last, there is check_out_member which allows the active member
       purchase the items that were stored in their cart and empties the cart after."""

    def __init__(self):
        """intializes two blank private lists for inventory and customers"""
        self._inventory = []
        self._members = []

    def add_product(self, added_product):
        """The add_product method adds product objects created by Product to the Store"""

        # Tracker variable to be used to see if the product was already added to the store
        product_ticker = 0

        # The nested for loop and if statement checks if the product exists and sets product_ticker to 1 if it does
        for x in range(0, len(self._inventory)):
            if added_product.get_product_id() == self._inventory[x].get_product_id():
                product_ticker = 1

        # If the ticker remains 0, add product to the list
        if product_ticker == 0:
            self._inventory.append(added_product)

    def add_member(self, added_member):
        """The add_member method adds customer objects created by Customer to the Store"""

        # Tracker variable to be used to see if the customer was already added to the store
        customer_ticker = 0

        # The nested for loop and if statement checks if the customer exists and sets customer_ticker to 1 if it does
        for x in range(0, len(self._members)):
            if added_member.get_customer_id() == self._members[x].get_customer_id():
                customer_ticker = 1

        # If the ticker remains 0, add customer to the list
        if customer_ticker == 0:
            self._members.append(added_member)

    def lookup_product_from_id(self, product_id):
        """The lookup_product_from_id method lookups a product by id and returns the Product object"""

        # The nested for loop and if statement checks to see if the product exists and returns it if it does
        for x in range(0, len(self._inventory)):
            if product_id == self._inventory[x].get_product_id():
                return self._inventory[x]

        # Return None if the product does not exist
        return None

    def lookup_member_from_id(self, customer_id):
        """The lookup_member_from_id method looks up a customer by id and returns the Customer object"""

        # The nested for loop and if statement returns the customer if they exist
        for x in range(0, len(self._members)):
            if customer_id == self._members[x].get_customer_id():
                return self._members[x]

        # Return None if the customer does not exist
        return None

    def product_search(self, searchterm):
        """ THe product_search method looks up products by keywords and returns the product id for each product that
            contains that keyword. The list is in ascending order by id."""

        list_of_ids = []

        for x in range(0, len(self._inventory)):
            if searchterm.lower() in self._inventory[x].get_title().lower() or searchterm.lower() in \
            self._inventory[x].get_description().lower():
                list_of_ids.append(self._inventory[x].get_product_id())
        return sorted(list_of_ids)

    def add_product_to_member_cart(self, product_id, customer_id):
        """The add_product_to_member_cart method is used to add an item to the cart of the Customer object. It takes in
           two variables; product_id and customer_id. If the product_id does not exist, it returns 'product ID not
           found'. If the customer_id does not exist, it returns 'member ID not found'. The last check this method does
           is to check if the item is in stock. If the item is not in stock, it returns 'product out of stock'. If
           all three checks pass, the item is added to cart and returns 'product added to cart'."""

        # Three to trackers that are used to see if the product exists, customer exists, and quantity > 0
        product_ticker = 0
        customer_ticker = 0
        zero_stock_ticker = 0

        # The nested for loop and if statement checks if the product id exists and sets product_ticker to 1 if it does
        for x in range(0, len(self._inventory)):
            if product_id == self._inventory[x].get_product_id():
                product_ticker = 1

        # If the product_ticker remained 0, returns "product ID not found"
        if product_ticker == 0:
            return "product ID not found"

        # The nested for loop and if statement checks if customer id exists and sets the customer_ticker to 1 if it does
        for x in range(0, len(self._members)):
            if customer_id == self._members[x].get_customer_id():
                customer_ticker = 1

        # If the product_ticker remained 0, returns "member ID not found"
        if customer_ticker == 0:
            return "member ID not found"

        # The nested for loop and if statement checks if the product is in stock and sets zero_stock_ticker to 1 if
        # the product is out of stock.
        for x in range(0, len(self._inventory)):
            if product_id == self._inventory[x].get_product_id() and self._inventory[x].get_quantity_available() == 0:
                zero_stock_ticker = 1

        # If the zero_stock_ticker was set to 1, returns "product of stock
        if zero_stock_ticker == 1:
            return "product out of stock"

        # If everyone above passes, this section adds the item to cart and returns "product added to cart
        for x in range(0, len(self._members)):
            if customer_id == self._members[x].get_customer_id():
                self._members[x].add_product_to_cart(product_id)
                return "product added to cart"

    def check_out_member(self, customer_id):
        """The check_out_member method checks out the customer during purchase. It has customer_id passed as a variable.
           If the customer_id is not found the InvalidCheckoutError exception is raised. If the customer_id does exist,
           then the checkout process proceeds and the total is calculate by quantity * price for each product id. If the
           customer had more units in the cart than were available, then they will only be purchasing what is left. If
           the customer is not a premium member, then they are charge an additional 7% shipping fee on top of the
           subtotal. Once everything is added up the customer is then checked out, the cart is emptied, and the total
           purchase amount is returned."""

        # Defined variables that will be used later
        customer_ticker = 0
        sub_total = 0

        # The nested for loop and if statement is used to check if the customer id valid. If the customer exists, the
        # customer_ticker is set to 1 and the x is assigned to slot_track which is used for the slot index of the
        # of the customer in the list
        for x in range(0, len(self._members)):
            if customer_id == self._members[x].get_customer_id():
                slot_track = x
                customer_ticker = 1

        # If the customer does not exist raise InvalidCheckError. If customer does exist then the else statement
        # contains nested for loops and if statements to calculate the cost by mapping product ids, units, and prices
        # together and stores the cost in sub_total while also decreasing the quantity available
        if customer_ticker == 0:
            raise InvalidCheckoutError
        else:
            item_count = len(self._members[slot_track].get_cart())
            current_cart = self._members[slot_track].get_cart()
            for x in range(0, len(self._inventory)):
                for y in range(0, item_count):
                    if self._inventory[x].get_product_id() == current_cart[y][0]:
                        for z in range(0, current_cart[y][1]):
                            if self._inventory[x].get_quantity_available() > 0:
                                sub_total += self._inventory[x].get_price()
                                self._inventory[x].decrease_quantity()

        # If the customer is not a premium member add a 7% shipping charge to sub_total
        if self._members[slot_track].is_premium_member() == False:
            sub_total *= 1.07

        # assign subtotal to full_charge, which is just used for visual styling
        full_charge = sub_total

        # Empty the customer's cart
        self._members[slot_track].empty_cart()

        # return full_charge
        return full_charge

def main():
    try:
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 20)
        c1 = Customer("Yinsheng", "QWF", False)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("889", "QWF")
        result = myStore.check_out_member("QWF")
        print(result)
    except InvalidCheckoutError:
        print("The Customer ID does not exist, so you are unable to checkout.")

if __name__ == '__main__':
    main()