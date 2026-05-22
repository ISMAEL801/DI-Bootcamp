# EXERCICSE1 

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Milou", 4)
cat2 = Cat("Miaou", 7)
cat3 = Cat("Bobi", 3)


def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1

    if cat2.age > oldest.age:
        oldest = cat2

    if cat3.age > oldest.age:
        oldest = cat3

    return oldest


oldest_cat = find_oldest_cat(cat1, cat2, cat3)

print(f"Le chat le plus âgé est {oldest_cat.name}, et a {oldest_cat.age} ans.")



# EXERCICSE2 

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} fait ouaf !")

    def jump(self):
        print(f"{self.name} saute {self.height * 2} cm de haut !")


davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 40)


print(f"Le chien de David s'appelle {davids_dog.name} et mesure {davids_dog.height} cm.")
davids_dog.bark()
davids_dog.jump()

print(f"Le chien de Sarah s'appelle {sarahs_dog.name} et mesure {sarahs_dog.height} cm.")
sarahs_dog.bark()
sarahs_dog.jump()


if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} est le plus grand.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} est le plus grand.")
else:
    print("Les deux chiens ont la même taille.")



# EXERCICSE3 

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])


stairway.sing_me_a_song()


# EXERCICSE4 

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(f"Animaux dans le zoo {self.name} :")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} a été vendu.")
        else:
            print(f"{animal_sold} n'est pas dans le zoo.")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)

        sorted_dict = {}

        for animal in sorted_animals:
            first_letter = animal[0]

            if first_letter not in sorted_dict:
                sorted_dict[first_letter] = []

            sorted_dict[first_letter].append(animal)

        return sorted_dict

    def get_groups(self):
        groups = self.sort_animals()

        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cat", "Cougar", "Lion", "Zebra")

brooklyn_safari.get_animals()

brooklyn_safari.sell_animal("Bear")

brooklyn_safari.get_animals()

brooklyn_safari.get_groups()

