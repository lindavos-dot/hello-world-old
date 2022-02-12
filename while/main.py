from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())

# unique_koala_facts: takes an integer as an argument and returns that number of unique koala facts in a list. 


koala_facts = []


def unique_koala_facts(number):
    while len(koala_facts) < number:
        fact = random_koala_fact()
        koala_facts.append(fact)            
    return len(koala_facts)


print(unique_koala_facts(60))

# num_joey_facts: young marsupials are called 'joeys'. How many unique facts mentioning this term are in our facts dataset?

# koala_weight: somewhere in the data is a fact about how heavy a koala is. This function should return that weight in kilogram (kg) as an integer.