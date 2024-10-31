# Chapter 26(Classes)

class Vehicle:
    def __init__(self, brand, model, year, curr_speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.curr_speed = curr_speed
    def move(self):
        self.curr_speed += 1
    def accelerate(self, value):
        self.curr_speed += value
    def stop(self):
        self.curr_speed = 0
    def details(self):
        return f"{self.brand} {self.model} {self.year}"