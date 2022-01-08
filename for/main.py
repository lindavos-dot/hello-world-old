from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

# shortest_names: takes a list of country names and returns a list of country names that have the shortest length. 

names = []

def shortest_names(countries):
    a = len(min(countries, key=len))
    for country in countries:
      if a == len(country):
        names.append(country)
    return names

print(shortest_names(countries))

# most_vowels: takes a list of country names and returns a list with the top three countries that have the most vowels in their name. 
# alphabet_set: takes a list of country names and returns a list of country names whose letters can be combined to form the complete alphabet. 

