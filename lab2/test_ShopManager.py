import unittest
import ShopManager


class TestShopManager(unittest.TestCase):
    def setUp(self):
        self.manager1 = ShopManager.ShopManager()
        self.manager1.animal1 = ShopManager.Alligator(True, 10, 1000002, 50000, ShopManager.Country.China.name, True,
                                                      20000)
        self.manager1.animal2 = ShopManager.Shark(True, ShopManager.Water.SeaWater.name, 10, 200000,
                                                  ShopManager.Country.US.name, True, 1029201)
        self.manager1.animal3 = ShopManager.Parrot("Blue", 10, True, 200, 500, ShopManager.Country.Ukraine.name, False,
                                                   60)

    def test_add_animal(self):
        self.manager1.add_animal(self.manager1.animal1)
        print(self.manager1.animals)
        self.assertEqual(self.manager1.animals, [self.manager1.animal1])
        self.manager1.add_animal(self.manager1.animal2)
        print(self.manager1.animals)
        self.assertEqual(self.manager1.animals, [self.manager1.animal1, self.manager1.animal2])
        self.manager1.add_animal(self.manager1.animal3)
        print(self.manager1.animals)
        self.assertEqual(self.manager1.animals, [self.manager1.animal1, self.manager1.animal2, self.manager1.animal3])

    def test_sort_by_price(self):
        self.manager1.add_animal(self.manager1.animal1)
        self.manager1.add_animal(self.manager1.animal2)
        self.manager1.add_animal(self.manager1.animal3)
        sorted_by_price_asc = self.manager1.sort_by_price(ShopManager.SortOrder.ASC)
        self.assertEqual(sorted_by_price_asc, [self.manager1.animal3, self.manager1.animal1, self.manager1.animal2])
        sorted_by_price_des = self.manager1.sort_by_price(ShopManager.SortOrder.DES)
        self.assertEqual(sorted_by_price_des, [self.manager1.animal2, self.manager1.animal1, self.manager1.animal3])

    def test_sort_by_is_predator(self):
        self.manager1.add_animal(self.manager1.animal1)
        self.manager1.add_animal(self.manager1.animal2)
        self.manager1.add_animal(self.manager1.animal3)
        sorted_by_is_predator_asc = self.manager1.sort_by_is_predator(ShopManager.SortOrder.ASC)
        self.assertEqual(sorted_by_is_predator_asc, [self.manager1.animal3, self.manager1.animal1,
                                                     self.manager1.animal2])
        sorted_by_is_predator_des = self.manager1.sort_by_is_predator(ShopManager.SortOrder.DES)
        self.assertEqual(sorted_by_is_predator_des, [self.manager1.animal1, self.manager1.animal2,
                                                     self.manager1.animal3])


if __name__ == "__main__":
    unittest.main()
