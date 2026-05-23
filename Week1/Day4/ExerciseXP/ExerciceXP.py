#Exercise 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())
            
class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    pass


bengal_obj = Bengal("Bengalou", 3)
chartreux_obj = Chartreux("Charti", 5)
siamese_obj = Siamese("Sia", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)

sara_pets.walk()

#Exercise 2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} aboie"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} a gagné le combat contre {other_dog.name}"
        elif other_power > my_power:
            return f"{other_dog.name} a gagné le combat contre {self.name}"
        else:
            return f"{self.name} et {other_dog.name} sont à égalité"


# Exercise 4
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return

        print(f"{first_name} n'est pas dans la famille.")

    def family_presentation(self):
        print(f"Nom de famille : {self.last_name}")

        for person in self.members:
            print(f"{person.first_name} {person.last_name}, {person.age} ans")


my_family = Family("OUEDRAOGO")

my_family.born("Ismael", 20)
my_family.born("Junior", 15)
my_family.born("Ana", 22)

my_family.family_presentation()

my_family.check_majority("Ismael")
my_family.check_majority("Junior")
