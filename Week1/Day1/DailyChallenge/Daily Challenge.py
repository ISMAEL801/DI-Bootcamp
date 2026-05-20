# #Challenge 1

number = int(input("Entrez le nombre  : "))
length = int(input("Entrez la longueur de la liste  : "))

liste_multiples = []
for i in range(1, length + 1):
    multiple = number * i
    liste_multiples.append(multiple)
print(f"Résultat : {liste_multiples}")

#Challenge 2

chaîne_caractères = input("Entrez chaîne de caractères à nettoyer : ")
mot_nettoye = ""
for lettre in chaîne_caractères:
    if mot_nettoye == "" or lettre != mot_nettoye[-1]:
        mot_nettoye = mot_nettoye + lettre
print(f"Résultat : {mot_nettoye}")
