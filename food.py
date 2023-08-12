from turtle import Turtle
import random
color_list = ["blue", "cyan", "#F4A460", "#00FF00", "#00FF00", "#8A2BE2", "#8A2BE2", "#800000", "#FF8C00", "#DDA0DD", "#FF00FF" ]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food = Turtle()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.color(random.choice(color_list))
