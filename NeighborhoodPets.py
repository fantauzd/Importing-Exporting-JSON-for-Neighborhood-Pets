# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 10/31/2023
# Description: Creates a class named NeighborhoodPets that has methods for adding a pet, deleting a pet, searching
# for the owner of a pet, saving data to a JSON file, loading data from a JSON file, and getting a set of all
# pet species. Using composition from a Pet class.

import json


class Pet:
    """
    A class representing a pet object with pet name, species, and pet owner data members.
    """

    def __init__(self, name, species, owner):
        self._name = name
        self._species = species
        self._owner = owner

    def get_name(self):
        """
        Returns the name of the pet.
        """
        return self._name

    def get_species(self):
        """
        Returns the species of the pet.
        """
        return self._species

    def get_owner(self):
        """
        Returns the owner of the pet.
        """
        return self._owner


class DuplicateNameError(Exception):
  """user-defined exception for duplicate pet name"""
  pass


class NeighborhoodPets:
    """
    A class representing pets in a neighborhood. Includes methods for adding and deleting pets,
    searching for the owner of a pet, saving data to a json file, and getting a set of all pwt species.
    """

    def __init__(self):
        self._neighborhood = []

    def add_pet(self, name, species, owner):
        """
        Creates a pet object and saves it to neighborhood pets. Checks if the name is already used
        and raises error if true.
        :param name: name of pet being added
        :param species: species of pet being added
        :param owner: owner of pet being added
        :return: n/a, creates a pet object and adds object to neighborhood data member (list)
        """
        for pet in self._neighborhood:
            if pet.get_name() == name:
                raise DuplicateNameError
        self._neighborhood.append(Pet(name, species, owner))

    def delete_pet(self, name):
        """
        Removes a pet object, based on the name (unique), from the neighborhood.
        :param name: name of pet to be removed
        :return: n/a, pet removed from neighborhood data member (list)
        """
        for pet in self._neighborhood:
            if pet.get_name() == name:
                self._neighborhood.remove(pet)

    def get_owner(self, name):
        """
        Takes the name of the pet (unique) and returns the name of the owner.
        :param name: name of the pet
        :return: name of the pet's owner
        """
        for pet in self._neighborhood:
            if pet.get_name() == name:
                return pet.get_owner()

    def save_as_json(self, file_name):
        """
        Takes a file name and creates a json with that name where each line represents a pet and has a list
        of the pet's name, species, and owner.
        :param file_name:
        :return: n/a, creates json file
        """
        lines = []
        with open(file_name, 'w') as outfile:
            for pet_object in self._neighborhood:
                new_line = []
                #  following three lines get relevant strings to create list for each pet object
                new_line.append(pet_object.get_name())
                new_line.append(pet_object.get_species())
                new_line.append(pet_object.get_owner())
                lines.append(new_line)  #  adds each pet list into final list
            json.dump(lines, outfile)  #  puts list of lists in json

    def read_json(self, file_name):
        """
        Takes a file name (json) and reads from that json file the pets belonging to neighborhood pets.
        Replaces all pets currently in memory
        :param file_name: file name of json to be read from
        :return: n/a, saves pets from json to data member (list)
        """
        with open(file_name, 'r') as infile:
            temp = json.load(infile)
            self._neighborhood = []  # clears the memory so it can be written from json
            for pet in temp:
                self.add_pet(pet[0], pet[1], pet[2])  # adds each pet into self._neighborhood data member (list)

    def get_all_species(self):
        """
        Returns a set of all species of pets in the neighborhood. Sets remove duplicates.
        :return: set of all species of pets in the neighborhood.
        """
        species_set = set()
        for pet in self._neighborhood:
            species_set.add(pet.get_species())  # use add method for sets
        return species_set
