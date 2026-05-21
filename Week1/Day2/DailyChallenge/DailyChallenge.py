#Challenge 1

# mot = input("Entrez un mot : ")

# lettre_indexes = {}

# for index, lettre in enumerate(mot):
#     if lettre in lettre_indexes:
#         lettre_indexes[lettre].append(index)
#     else:
#         lettre_indexes[lettre] = [index]

# print(lettre_indexes)

#Challenge 2

articles_achat = {
    "Téléphone": "$999",
    "Haut-parleurs": "$300",
    "Ordinateur portable": "$5,000",
    "PC": "$1200"
}

portefeuille = "$1"

panier = []

portefeuille = int(portefeuille.replace("$", "").replace(",", ""))

for article, prix in articles_achat.items():
    prix_nettoye = int(prix.replace("$", "").replace(",", ""))

    if portefeuille >= prix_nettoye:
        panier.append(article)
        portefeuille = portefeuille - prix_nettoye

if panier:
    print(sorted(panier))
else:
    print("Rien")