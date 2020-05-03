import doctest
from main.python.ua.lviv.iot.models.AbstractShoes import AbstractShoes
from main.python.ua.lviv.iot.models.Boots import Boots
from main.python.ua.lviv.iot.models.Pumps import Pumps
from main.python.ua.lviv.iot.models.Sneakers import Sneakers
from main.python.ua.lviv.iot.models.Sex import Sex
from main.python.ua.lviv.iot.models.DegreeOfOpenness import DegreeOfOpenness
from main.python.ua.lviv.iot.models.Specification import Specification


class ShoppingManager:
    def __init__(self):
        pass

    @staticmethod
    def find_shoes_by_assignment(shoes, assignment: str):
        """
        searching shoes by assignment
        >>> shoes = [Boots(39, 1599.0, "winter", Sex.FEMALE, "Ecco", "black", "leather", "wool", "oval", 27.5), Pumps(38, 600.0, "classic", Sex.FEMALE, "Ecco", "red", "leather", "leather", "oval", DegreeOfOpenness.MIX), Sneakers(41, 789.9, "summer", Sex.MALE, "Adidas", "blue", "cotton", "cotton", "oval", True, Specification.FOR_TRAINING)]
        >>> ShoppingManager.find_shoes_by_assignment(shoes, "winter")
        [Information about these shoes: size_eur_standard = 39, price_in_uah = 1599.0, assignment = winter, sex = Sex.FEMALE, brand = Ecco, color = black, material_of_vamp = leather, material_of_lining = wool, toecap_type = oval, hight_of_shaft_in_sm = 27.5]
        """
        found_pairs_of_shoes_by_assignment: list[AbstractShoes] = []
        for pair_of_shoes in shoes:
            if pair_of_shoes.assignment == assignment:
                found_pairs_of_shoes_by_assignment.append(pair_of_shoes)
        return found_pairs_of_shoes_by_assignment

    @staticmethod
    def find_shoes_by_size_eur_standard(shoes, size_eur_standard):
        """
        searching shoes by assignment
        >>> shoes = [Boots(39, 1599.0, "winter", Sex.FEMALE, "Ecco", "black", "leather", "wool", "oval", 27.5), Pumps(38, 600.0, "classic", Sex.FEMALE, "Ecco", "red", "leather", "leather", "oval", DegreeOfOpenness.MIX), Sneakers(41, 789.9, "summer", Sex.MALE, "Adidas", "blue", "cotton", "cotton", "oval", True, Specification.FOR_TRAINING)]
        >>> ShoppingManager.find_shoes_by_size_eur_standard(shoes, 39)
        [Information about these shoes: size_eur_standard = 39, price_in_uah = 1599.0, assignment = winter, sex = Sex.FEMALE, brand = Ecco, color = black, material_of_vamp = leather, material_of_lining = wool, toecap_type = oval, hight_of_shaft_in_sm = 27.5]
        """
        found_pairs_of_shoes_by_size_eur_standard: list[AbstractShoes] = []
        for pair_of_shoes in shoes:
            if pair_of_shoes.size_eur_standard == size_eur_standard:
                found_pairs_of_shoes_by_size_eur_standard.append(pair_of_shoes)
        return found_pairs_of_shoes_by_size_eur_standard


if __name__ == "__main__":
    doctest.testmod()
