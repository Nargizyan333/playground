# Chapter 27(Inheritance)
from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model, year, capacity):
        super.__init__(brand, model, year)
        self.capacity = capacity

    def add_capacity(self, value):
        self.capacity += value

    def reduce_capacity(self, value):
        self.capacity -= value
