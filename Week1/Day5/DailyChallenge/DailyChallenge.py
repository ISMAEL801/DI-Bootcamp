import math
import turtle


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.diameter = diameter
        else:
            raise ValueError("Il faut donner soit un rayon, soit un diamètre.")

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Le rayon doit être positif.")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Le diamètre doit être positif.")
        self._radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area():.2f})"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("On ne peut additionner qu'un cercle avec un autre cercle.")
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius




def draw_circles(circles):
    screen = turtle.Screen()
    screen.title("Cercles triés avec Turtle")
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(5)
    pen.pensize(2)

    x_position = -300

    for circle in circles:
        pen.penup()
        pen.goto(x_position, -circle.radius)
        pen.pendown()

        pen.circle(circle.radius)

        pen.penup()
        pen.goto(x_position - 30, -circle.radius - 30)
        pen.write(
            f"R={circle.radius}",
            font=("Arial", 12, "normal")
        )

        x_position += circle.diameter + 40

    turtle.done()




c1 = Circle(radius=50)
c2 = Circle(diameter=160)
c3 = Circle(radius=30)
c4 = Circle(radius=70)

print("=== AFFICHAGE DES CERCLES ===")
print(c1)
print(c2)
print(c3)
print(c4)

print("\n=== ADDITION DE DEUX CERCLES ===")
c5 = c1 + c3
print("c1 + c3 =", c5)

print("\n=== COMPARAISONS ===")
print("c1 > c2 :", c1 > c2)
print("c1 == c2 :", c1 == c2)
print("c1 < c2 :", c1 < c2)

print("\n=== TRI DES CERCLES ===")
circles = [c1, c2, c3, c4, c5]

print("Avant tri :")
print(circles)

circles.sort()

print("Après tri :")
print(circles)

draw_circles(circles)