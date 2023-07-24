"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, num):
        check = self.cargo + num
        if check > self.max_cargo:
            raise CargoOverload
        self.cargo += num

    def remove_all_cargo(self):
        cargo_before_null = self.cargo
        self.cargo = 0
        return cargo_before_null

