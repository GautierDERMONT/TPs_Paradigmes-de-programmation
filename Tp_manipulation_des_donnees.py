#--------------------Exercice 1--------------------:

# prix_euros = [50, 20, 35, 100, 80]

# taux_conversion = 1.10

# prix_dollars = list(map(lambda prix: prix * taux_conversion, prix_euros))
# print("Prix convertis en dollars :", prix_dollars)

# prix_dollars_avec_symbole = list(map(lambda prix: f"{prix:.2f}$", prix_dollars))
# print("prix en dollars avec symbole :", prix_dollars_avec_symbole)

#--------------------Exercice 2--------------------:

# ages = [12, 25, 17, 18, 40, 15, 22]

# ages_adultes = list(filter(lambda age: age >= 18, ages))
# print("Ages des adultes :", ages_adultes)

# ages_seniors = [45, 67, 72, 33, 58, 60, 85]

# ages_seniors_filtrés = list(filter(lambda age: age >= 60, ages_seniors))
# print("Ages des seniors:", ages_seniors_filtrés)

#--------------------Exercices 3--------------------:

# from functools import reduce

# ventes = [120, 50, 30, 20, 90, 100]

# total_ventes = reduce(lambda x, y: x + y, ventes)
# print("Total des ventes:", total_ventes)

# produit_ventes = reduce(lambda x, y: x * y, ventes)
# print("Produit des ventes :", produit_ventes)

#--------------------Exercices 4--------------------:

# from functools import reduce

# notes = [12, 15, 9, 18, 6, 20, 14]

# notes_sur_100 = list(map(lambda note: note * 5, notes))
# print("Notes sur 100 :", notes_sur_100)

# notes_sup_50 = list(filter(lambda note: note >= 50, notes_sur_100))
# print("Notes supérieure ou égale à 50 :", notes_sup_50)

# if notes_sup_50:  
#     moyenne_notes = reduce(lambda x, y: x + y, notes_sup_50)/len(notes_sup_50)
# else:
#     moyenne_notes = 0

# print("Moyenne des notes supérieure ou égale à 50 :", moyenne_notes)

#--------------------Exercice 5--------------------:

import csv
from functools import reduce

def charger_donnees(fichier):
    with open(fichier, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def noms_en_majuscules(donnees):
    return list(map(lambda row: {**row, "Nom": row["Nom"].upper()}, donnees))

def filtrer_salaire(donnees, seuil):
    return list(filter(lambda row: int(row["Salaire"]) > seuil, donnees))

def calculer_salaire_total(donnees):
    return reduce(lambda total, row: total + int(row["Salaire"]), donnees, 0)

def ajouter_categorie_salaire(donnees):
    def categoriser(row):
        salaire = int(row["Salaire"])
        if salaire < 30000:
            categorie = "Junior"
        elif 30000 <= salaire <= 50000:
            categorie = "Intermédiaire"
        else:
            categorie = "Senior"
        return {**row, "Categorie": categorie}
    return list(map(categoriser, donnees))

fichier_csv = 'employes.csv'
donnees = charger_donnees(fichier_csv)

donnees = noms_en_majuscules(donnees)
print("Données avec noms en majuscules :", donnees)

employes_senior = filtrer_salaire(donnees, 50000)
print("Employés avec un salaire > 50 000 :", employes_senior)

salaire_total = calculer_salaire_total(employes_senior)
print("Salaire total des employés filtrés :", salaire_total)

donnees_avec_categories = ajouter_categorie_salaire(donnees)
print("Données avec catégorie :", donnees_avec_categories)


