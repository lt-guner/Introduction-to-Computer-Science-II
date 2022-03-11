# Author: Timur Guner
# Date: 2021-05-05
# Description: Project 5d creates a class called NeighborhoodPets(). It has one private data member, a dictionary
#              initialized as {Pets : []}. If has the method called get_pets to return the dictionary and get get_owner
#              to return the owner. The add_pet method adds a pet to the Pet dictionary and if the pet doesn't exist
#              yet. There are two json methods, one to save a json file and one to read a json file from a previous
#              session. There are also methods to return all species as a set and delete a pet from the dictionary.

import json

class NeighborhoodPets():
    """
    The class NeighboorhoodPets is used to store a dictionary of pets. It has a private data member called petsdict that
    initializes as {Pets: []} to store each pet subdictionary object in its list. There are three get methods; get_pets
    (returns the entire dictionary), get_owner (returns pet owner), and get_all_species (returns a set of all species).
    The add_pet method adds a pet dictionary object to petsdict, if the pet doesn't already exist. The current petsdict
    can be saved in json using the save_as_json method and previous session json file can be loaded using read_json
    method. The method delete pet removes a pet from petsdict
    """

    def __init__(self):
        """
        Creates a private data member called petsdict that initializes as {Pets: []} to store each pet susbdictionary
        object in its list
        """
        self._petsdict = {'Pets': []}

    def get_pets(self):
        """
        The get_pets method returns petsdict
        """
        return self._petsdict

    def add_pet(self, petname, species, owner):
        """
        The add_pet method takes in three arguments; petname, species, and owner. The method first verifies that the pet
        is not already in petsdict. If it is not, it will store the three arguments as a subdictionary in petsdict.
        """
        for x in range (0, len(self._petsdict["Pets"])):
            if self._petsdict["Pets"][x]["Pet Name"].lower() == petname.lower():
                return
        self._petsdict["Pets"].append({"Pet Name": petname, "Species": species, "Owner" :owner})

    def delete_pet(self, petname):
        """
        The delete_pet method takes the petname as an argument and removes the pet from petsdict
        """
        i = 0

        for x in range (0, len(self._petsdict["Pets"])):
            if self._petsdict["Pets"][x]["Pet Name"] == petname:
                i = x

        del self._petsdict["Pets"][i]

    def get_owner(self, petname):
        """
        The get_owner method takes the pets name as an argument and returns the owner of the pet from petsdict
        """
        for x in range (0, len(self._petsdict["Pets"])):
            if self._petsdict["Pets"][x]["Pet Name"] == petname:
                return self._petsdict["Pets"][x]["Owner"]

    def save_as_json(self, filename):
        """
        The save_as_json method takes in the file name as an argument and saves petsdict as a json file
        """
        with open(filename, 'w') as outfile:
            json.dump(self._petsdict, outfile)


    def read_json(self, filename):
        """
        The read_json method takes in the file name as an argument and loads it to petsdict
        """
        try:
            with open(filename, 'r') as infile:
                self._petsdict = json.load(infile)
        except FileNotFoundError:
            print("The file was not found.")

    def get_all_species(self):
        """
        The get_all_species method returns a set of all species in petsdict
        """
        species_set = set()

        for x in range(0, len(self._petsdict["Pets"])):
            species_set.add(self._petsdict["Pets"][x]["Species"])

        return species_set


def main():
    np = NeighborhoodPets()

    np.add_pet("Fluffy", "gila monster", "Oksana")
    np.add_pet("Tiny", "stegasaurus", "Rachel")
    np.add_pet("Spot", "zebra", "Farrokh")
    print(np.get_pets())

    np.add_pet("Tiny", "stegasaurus", "Rachel")
    np.add_pet("Spot", "zebra", "Farrokh")
    np.add_pet("Jim ", "rock", "Tyler")
    print(np.get_pets())

    np.save_as_json("pets.json")
    np.delete_pet("Tiny")
    print(np.get_pets())

    spot_owner = np.get_owner("Spot")
    print(spot_owner)

    np.read_json("pets_old.json")
    print(np.get_pets())

    species_set = np.get_all_species()
    print(species_set)

    np.add_pet("Jim ", "rock", "Tyler")
    print(np.get_pets())

    species_set = np.get_all_species()
    print(species_set)

if __name__ == '__main__':
    main()
