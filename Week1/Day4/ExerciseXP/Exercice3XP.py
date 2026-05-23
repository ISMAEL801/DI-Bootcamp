#Exercise3
import random
from ExerciceXP import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [self.name]

        for dog in args:
            dog_names.append(dog.name)

        print(f"{', '.join(dog_names)} tous jouent ensemble")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]

            trick = random.choice(tricks)
            print(f"{self.name} {trick}")
        else:
            print(f"{self.name} n'est pas encore dressé")


dog1 = PetDog("Rex", 3, 12)
dog2 = PetDog("Max", 4, 18)
dog3 = PetDog("Bella", 2, 10)

dog1.train()
dog1.play(dog2, dog3)
dog1.do_a_trick()