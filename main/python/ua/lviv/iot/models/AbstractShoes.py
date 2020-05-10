from abc import ABC
from main.python.ua.lviv.iot.models.Sex import Sex


#class AbstractShoes(ABC):
class AbstractShoes:

    def __init__(self, size_eur_standard: int, price_in_uah: float, assignment: str, sex: Sex, brand: str, color: str,
                 material_of_vamp: str, material_of_lining: str, toecap_type: str):
       self.size_eur_standard = size_eur_standard
       self.price_in_uah = price_in_uah
       self.assignment = assignment
       self.sex = sex
       self.brand = brand
       self.color = color
       self.material_of_vamp = material_of_vamp
       self.material_of_lining = material_of_lining
       self.toecap_type = toecap_type

    def __del__(self):
        print("Deleting object")

    def __str__(self):
        return "Information about these shoes: size_eur_standard = " + str(self.size_eur_standard) + \
               ", price_in_uah = " + str(self.price_in_uah) + ", assignment = " + str(self.assignment) + ", sex = " + str(self.sex) + ", brand = " + \
               str(self.brand) + ", color = " + str(self.color) + ", material_of_vamp = " + \
               str(self.material_of_vamp) + ", material_of_lining = " + str(self.material_of_lining) + \
               ", toecap_type = " + str(self.toecap_type)

    def __repr__(self):
        return str(self)
