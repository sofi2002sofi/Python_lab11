from main.python.ua.lviv.iot.models.Sex import Sex
from main.python.ua.lviv.iot.models.AbstractShoes import AbstractShoes
from main.python.ua.lviv.iot.models.DegreeOfOpenness import DegreeOfOpenness


class Pumps(AbstractShoes):
    def __init__(self, size_eur_standard: int, price_in_uah: float, assignment: str, sex: Sex, brand: str, color: str,
                 material_of_vamp: str, material_of_lining: str, toecap_type: str, degree_of_openness: DegreeOfOpenness):
        AbstractShoes.__init__(self, size_eur_standard, price_in_uah, assignment, sex, brand, color,
                               material_of_vamp, material_of_lining, toecap_type)
        self.degree_of_openness = degree_of_openness

    def __str__(self):
        return AbstractShoes.__str__(self) + ", degree_of_openness = " + str(self.degree_of_openness)

    def __repr__(self):
        return str(self)
