# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

# Part 1: Create Passport

def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport_person = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
    }
    return passport_person


my_passport = create_passport("Linda Vos", "1986-8-19", "Amsterdam", 1.80, "Netherlands")
print(my_passport["name"])

# Part 2: Add Stamp


# Part 3: Add biometric data