from Animal import Animal
from Water import Water


class Fish(Animal):
    def __init__(self, type_of_water: Water, weight_in_grams, price, origin_country, is_predator, eats_in_grams):
        self.type_of_water = type_of_water
        Animal.__init__(self, weight_in_grams, price, origin_country, is_predator, eats_in_grams)


class Shark(Animal):
    def __init__(self, is_dangerous_for_human, type_of_water: Water, weight_in_grams, price, origin_country, is_predator, eats_in_grams):
        self.is_dangerous_for_human = is_dangerous_for_human
        Fish.__init__(self, type_of_water, weight_in_grams, price, origin_country, is_predator , eats_in_grams)

    def __repr__(self):
        return 'Shark: price: {self.price}, is predator: {self.is_predator}, eats in grams: {self.eats_in_grams} '.format(self=self)