# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_one = "Ruud Gullit"
scorer_two = "Marco van Basten"
goal_0 = str(32)
goal_1 = str(54)
scorers = scorer_one + " scored in the \'" + goal_0, scorer_two + " scored in the \'" + goal_1
print (scorers)

report = (f"{scorer_one} scored in the {goal_0}nd minute") + '\n' + (f"{scorer_two} scored in the {goal_1}th minute")
print(report)

player = "Hans van Breukelen"
first_name = player[:4]
print(first_name)

last_name = player[len(player)-13:]
print(last_name)

name_short = player[-len(player)] + ". " + last_name
print(name_short)

chant = (f"{player[-len(player):4]}! "*4)[:23]
print(chant)
