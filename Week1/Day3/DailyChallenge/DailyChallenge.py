# EXERCICSE5 
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        result = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            result += f"{animal:<10} : {count}\n"

        result += "\n    E-I-E-I-0!"

        return result

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_names = []

        for animal in animal_types:
            count = self.animals[animal]

            if count > 1:
                animal_names.append(animal + "s")
            else:
                animal_names.append(animal)

        if len(animal_names) == 1:
            animals_text = animal_names[0]
        else:
            animals_text = ", ".join(animal_names[:-1])
            animals_text += " et " + animal_names[-1]

        return f"La ferme de {self.name} possède des {animals_text}."


macdonald = Farm("McDonald")

macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)

print(macdonald.get_info())

print(macdonald.get_short_info())



