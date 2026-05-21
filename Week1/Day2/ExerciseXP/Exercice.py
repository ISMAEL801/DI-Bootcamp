#Exercise1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))
print(my_dict)

# exercice 2

family_dict = {}

while True:
    name = input("entrer le nom d'un membre de la famille ou total pour afficher le total : ").strip()

    if name.lower() == "total":
        break

    age = input("entrer l'age de ce membre de la famille : ").strip()

    if not age.isdigit():
        print("Erreur : l'âge doit être un nombre.")
        continue

    family_dict[name] = int(age)


prix_total = 0

for name, age in family_dict.items():

    if age < 3:
        prix_billet = 0

    elif 3 <= age < 12:
        prix_billet = 10

    else:
        prix_billet = 15

    print(f"{name} doit payer {prix_billet} $")
    prix_total += prix_billet

print(f"le prix total du billet est de {prix_total} $")

#exercicse3
brand = {"name": "Zara",
         "creation_date": 1975,
         "creator_name": "Amancio Ortega Gaona",
         "type_of_clothes": ["men", "women", "children", "home"],
         "international_competitors": ["Gap", "H&M", "Benetton"],
         "number_stores": 7000,
         "major_color": {
             "France": "blue",
             "Spain": "red",
             "US": ["pink", "green"]
         }}
brand["number_stores"] = 2
print(f" les clients zara en utilise le {brand["type_of_clothes"]} ")

brand["country_creation"]="Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
    
del brand["creation_date"]

print(brand["international_competitors"][-1])

print(f"{brand['major_color']['US']}")

print(len(brand))

print(brand.keys())

more_on_zara ={
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)
print(brand)

#Exercise4
def describe_city(city,country="None ") :
        print(f"{city} is in {country}")


describe_city("abidjan","côte d'ivoire")

describe_city("paris","france")

describe_city("londres")

#Exercise5
import random
def nombre_aleatoire(nombre) :
    random_nombre = random.randint(1, 100) 
    if nombre == random_nombre :
        print("félicitations vous aves trouvé le nombre aléatoire")
    else :
        print(f"désolé le nombre aléatoire était {random_nombre} et votre nombre était {nombre}")

nombre_aleatoire(89)

#Exercise6
def make_shirt(size="large",text="I love Python") :
    print(f"The size of the shirt is {size} and the text is  {text}")
    
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="Custom message")

#Exercise7
import random

def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 16), 1)
    elif season == "spring":
        return round(random.uniform(0, 23), 1)
    elif season == "summer":
        return round(random.uniform(24, 40), 1)
    elif season == "autumn":
        return round(random.uniform(10, 25), 1)


def main():
    month = int(input("Entrez un mois entre 1 et 12 : "))

    if month == 12 or month == 1 or month == 2:
        season = "winter"
    elif month == 3 or month == 4 or month == 5:
        season = "spring"
    elif month == 6 or month == 7 or month == 8:
        season = "summer"
    elif month == 9 or month == 10 or month == 11:
        season = "autumn"
    else:
        print("Mois invalide. Veuillez entrer un nombre entre 1 et 12.")
        return

    temperature = (season)

    print(f"The season is {season}.")
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, it's freezing! Wear some extra layers today.")
    elif temperature <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif temperature <= 23:
        print("Nice weather.")
    elif temperature <= 32:
        print("It's a bit warm, make sure you drink enough water.")
    else:
        print("It's really hot! Stay cool.")

main()


#Exercise8

def main():
    base_price = 10.0
    topping_price = 2.50
    toppings = []

    while True:
        ingredient = input("Entrez un ingrédient pour votre pizza ou 'quit' pour terminer : ").strip()
        if ingredient.lower() == 'quit':
            break
        if ingredient == '':
            continue
        toppings.append(ingredient)
        print(f"Adding {ingredient} to your pizza.")

    print('\nIngredients de votre pizza :')
    if toppings:
        for t in toppings:
            print(f"- {t}")
    else:
        print("- (aucune garniture)")

    total = base_price + topping_price * len(toppings)
    print(f"Prix total de la pizza : ${total:.2f}")


if __name__ == '__main__':
    main()
