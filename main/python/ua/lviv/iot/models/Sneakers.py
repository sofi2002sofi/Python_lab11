from main.python.ua.lviv.iot.models.Sex import Sex
from main.python.ua.lviv.iot.models.AbstractShoes import AbstractShoes
from main.python.ua.lviv.iot.models.Specification import Specification


class Sneakers(AbstractShoes):
    def __init__(self, size_eur_standard: int, price_in_uah: float, assignment: str, sex: Sex, brand: str, color: str,
                 material_of_vamp: str, material_of_lining: str, toecap_type: str, eyelets_presence: bool,
                 specification: Specification):
        AbstractShoes.__init__(self, size_eur_standard, price_in_uah, assignment, sex, brand, color,
                               material_of_vamp, material_of_lining, toecap_type)
        self.eyelets_presence = eyelets_presence
        self.specification = specification

    def __str__(self):
        return AbstractShoes.__str__(self) + ", eyelets_presence = " + str(self.eyelets_presence) + ", specification = " + str(self.specification)

    def __repr__(self):
        return str(self)
