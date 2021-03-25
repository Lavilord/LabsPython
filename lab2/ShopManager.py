from Country import Country
from Water import Water
from Reptile import Snake, Alligator
from Bird import Parrot, Rooster
from Fish import Shark
from SortOrder import SortOrder
from operator import attrgetter


class ShopManager:
    def __init__(self, animals=None):
        if animals is None:
            self.animals = []
        else:
            self.animals = animals

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)

    def sort_by_price(self, sort_order: SortOrder):
        if sort_order == SortOrder.ASC:
            return sorted(self.animals, key=attrgetter('price'))
        if sort_order == SortOrder.DES:
            return sorted(self.animals, key=attrgetter('price'), reverse=True)

    def sort_by_is_predator(self, sort_order: SortOrder):
        if sort_order == SortOrder.ASC:
            return sorted(self.animals, key=attrgetter('is_predator'))
        if sort_order == SortOrder.DES:
            return sorted(self.animals, key=attrgetter('is_predator'), reverse=True)

    def sort_by_eats_in_grams(self, sort_order: SortOrder):
        if sort_order == SortOrder.ASC:
            return sorted(self.animals, key=attrgetter('eats_in_grams'))
        if sort_order == SortOrder.DES:
            return sorted(self.animals, key=attrgetter('eats_in_grams'), reverse=True)


def main():
    manager1 = ShopManager()
    rooster1 = Rooster(True, True, 10, False, 3500, 1000, Country.Ukraine.name, False, 200)
    rooster2 = Rooster(True, True, 10, False, 3500, 3000, Country.Ukraine.name, True, 400)
    rooster3 = Rooster(True, True, 10, False, 3500, 500, Country.Ukraine.name, False, 275)
    alligator1 = Alligator(True, 1000, 50000, 3000000, Country.China.name, True, 400000)
    manager1.add_animal(rooster1)
    manager1.add_animal(rooster2)
    manager1.add_animal(rooster3)
    manager1.add_animal(alligator1)

    sorted_by_price_asc = manager1.sort_by_price(SortOrder.ASC)
    sorted_by_price_des = manager1.sort_by_price(SortOrder.DES)
    print(sorted_by_price_asc)
    print(sorted_by_price_des)
    sorted_by_is_predator_asc = manager1.sort_by_is_predator(SortOrder.ASC)
    sorted_by_is_predator_des = manager1.sort_by_is_predator(SortOrder.DES)
    print(sorted_by_is_predator_asc)
    print(sorted_by_is_predator_des)


if __name__ == '__main__':
    main()
