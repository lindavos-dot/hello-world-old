# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

# Part 1: Players

from unicodedata import name


class Player():
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

        list = [speed, endurance, accuracy]
        for input in list:
            if input < 0 or input > 1: 
                raise ValueError('value should be between 0 and 1')
          

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."
    

    def strength(self):
        if self.speed >= self.endurance and self.accuracy:
            return "speed", self.speed
        elif self.endurance >= self.accuracy:
            return "endurance", self.endurance
        else:
            return "accuracy", self.accuracy
        


player_1 = Player("Hans van Breukelen", 0.8, 0.7, 0.6)
# print(player_1.__dict__)
# print(player_1.introduce())

player_2 = Player("Frank de Boer", 0.7, 0.8, 0.9)
# print(player_2.__dict__)
# print(player_2.strength())

player_3 = Player("Ronald de Boer", 0.7, 0.8, 0.9)
# print(player_3.__dict__)