from Animal import Animal


class Reptile(Animal):
    def __init__(self, length_in_centimeters: int, weight_in_grams, price, origin_country, is_predator, eats_in_grams):
        self.length_in_centimeters = length_in_centimeters
        Animal.__init__(self, weight_in_grams, price, origin_country, is_predator, eats_in_grams)


class Alligator(Reptile):
    def __init__(self, is_trained: bool, length_in_centimeters, weight_in_grams, price, origin_country, is_predator,
                 eats_in_grams):
        self.is_trained = is_trained
        Reptile.__init__(self, length_in_centimeters, weight_in_grams, price, origin_country, is_predator,
                         eats_in_grams)

    def __repr__(self):
        return 'Alligator: price: {self.price}, is predator: {self.is_predator}, eats in grams: {self.eats_in_grams}\n'\
            .format(self=self)


class Snake(Reptile):
    def __init__(self, is_poisonous: bool, length_in_centimeters, weight_in_grams, price, origin_country, is_predator,
                 eats_in_grams):
        self.is_poisonous = is_poisonous
        Reptile.__init__(self, length_in_centimeters, weight_in_grams, price, origin_country, is_predator,
                         eats_in_grams)

    def __repr__(self):
        return 'Snake: price: {self.price}, is predator: {self.is_predator}, eats in grams: {self.eats_in_grams}\n '\
            .format(self=self)
