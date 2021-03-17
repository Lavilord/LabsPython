from Animal import Animal


class Bird(Animal):
    def __init__(self, length_of_wing_in_centimeters, can_speak, weight_in_grams, price, origin_country, is_predator, eats_in_grams):
        
        self.length_of_wing_in_centimeters = length_of_wing_in_centimeters
        self.can_speak = can_speak
        Animal.__init__(self, weight_in_grams, price, origin_country, is_predator , eats_in_grams )


class Parrot(Bird):
    def __init__(self, color, length_of_wing_in_centimeters, can_speak, weight_in_grams, price, origin_country, is_predator, eats_in_grams):
        self.color = color
        Bird.__init__(self, length_of_wing_in_centimeters, can_speak, weight_in_grams, price, origin_country, is_predator, eats_in_grams)

    def __repr__(self):
        return 'Parrot: price: {self.price}, is predator: {self.is_predator}, eats in grams: {self.eats_in_grams} '.format(self=self)


class Rooster(Bird):
    def __init__(self,is_fertile,is_alarm_clock, length_of_wing_in_centimeters, can_speak, weight_in_grams, price, origin_country, is_predator, eats_in_grams):
        self.is_fertile = is_fertile
        self.s_alarm_clock = is_alarm_clock
        Bird.__init__(self, length_of_wing_in_centimeters, can_speak, weight_in_grams, price, origin_country, is_predator, eats_in_grams)

    def __repr__(self):
        return 'Rooster: price: {self.price}, is predator: {self.is_predator}, eats in grams: {self.eats_in_grams} '.format(self=self)