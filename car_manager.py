from turtle import Turtle
import random

COLORS = ["DeepPink", "DeepPink1", "DeepPink2", "DeepPink3", "DeepPink4",
          "DarkOrchid", "DarkOrchid1", "DarkOrchid2", "DarkOrchid3", "DarkOrchid4",
          "coral", "coral1", "coral2", "coral3", "coral4",
          "hotpink", "HotPink", "HotPink", "HotPink1", "HotPink2", "HotPink3", "HotPink4",
          "PaleVioletRed", "PaleVioletRed1", "PaleVioletRed2", "PaleVioletRed3", "PaleVioletRed4",
          "plum", "plum1", "plum2", "plum3", "plum4",
          "VioletRed", "VioletRed1", "VioletRed2", "VioletRed3", "VioletRed4"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(a=-250, b=250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


