# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# Write a function alphabetical_order that takes one argument: a list of strings that represent film names. 
# It returns a list of the same films in alphabetical order.

list_of_films = ["Daddy-O", "I passed for White", "The Secret Ways", "Bachelor Flat", "Daimond Head", "Gidget Goed to Rome"]

def alphabetical_order(list):
    list = input(x)
    return list.sort()

alphabetical_order(list_of_films)
print(list_of_films)

# Write a function won_golden_globe that takes a film name and returns True or False based on whether or not this movie won a Golden Globe.
# Look into using the lower-function on the given film string.

list_golden_globe = ["Jaws", "E.T. the Extra-Terrestrial", "Star Wars: Episode IV - A New Hope", "Memoirs of a Geisha"]

def won_golden_globe(list_to_search, element):
  if element in list_to_search:
    return True
  else:
    return False

print(won_golden_globe(list_golden_globe, "Jaws"))

for element in list_golden_globe:
  print(element.lower())

# Write a function remove_toto_albums that takes a list of strings, removes Joseph's Toto albums from it and returns the tidy list. 

toto_albums = ["Fahrenheit", "The Seventh One", "Toto XX", "Falling in Between", "Old Is New"]
list_of_films.extend(toto_albums)

print(list_of_films)

def remove_toto_albums(list1, list2):
    for element in list1:
        if element in list2:
          list2.remove(element)
    return list2

remove_toto_albums(toto_albums, list_of_films)

print(list_of_films)