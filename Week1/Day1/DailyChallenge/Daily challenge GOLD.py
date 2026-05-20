date_saisie = input("Entrez votre date de naissance (DD/MM/YYYY) : ")

jours, mois, annee = date_saisie.split("/")
jours = int(jours)
mois = int(mois)
annee = int(annee)

annee_actuelle = 2026
mois_actuel = 5
jour_actuel = 20

age = annee_actuelle - annee

if (mois_actuel, jour_actuel) < (mois, jours):
    age = age - 1

nb_bougies = age % 10

bougies_str = "i" * nb_bougies
tirets_restants = 11 - nb_bougies
cote_gauche = tirets_restants // 2
cote_droit = tirets_restants - cote_gauche

ligne_bougies = "_" * cote_gauche + bougies_str + "_" * cote_droit

gateau = f"""
       {ligne_bougies}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

est_bissextile = (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

print(f"\nVous avez {age} ans. Voici votre gâteau :")
if est_bissextile:
    print(gateau)
    print(gateau)  
else:
    print(gateau)
    
       |
    ---