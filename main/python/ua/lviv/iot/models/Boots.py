from main.python.ua.lviv.iot.models.AbstractShoes import AbstractShoes
from main.python.ua.lviv.iot.models.Sex import Sex


class Boots(AbstractShoes):
    def __init__(self, size_eur_standard: int, price_in_uah: float, assignment: str, sex: Sex, brand: str, color: str,
                 material_of_vamp: str, material_of_lining: str, toecap_type: str, hight_of_shaft_in_sm: float):
        AbstractShoes.__init__(self, size_eur_standard, price_in_uah, assignment, sex, brand, color,
                               material_of_vamp, material_of_lining, toecap_type)
        self.hight_of_shaft_in_sm = hight_of_shaft_in_sm

    def __str__(self):
        return AbstractShoes.__str__(self) + ", hight_of_shaft_in_sm = " + str(self.hight_of_shaft_in_sm)

    def __repr__(self):
        return str(self)
