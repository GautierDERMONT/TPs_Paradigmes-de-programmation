def saisir_donnees():
   
    noms = []
    notes = []

    while True:
        try:
            nb_etudiants = int(input("Combien d'étudiants souhaitez-vous saisir ? "))
            if nb_etudiants <= 0:
                print("Veuillez entrer un nombre positif.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    for i in range(nb_etudiants):
        nom = input(f"Nom de l'étudiant {i + 1} : ")
        while True:
            try:
                note = float(input(f"Note de {nom} : "))
                if 0 <= note <= 20:
                    break
                else:
                    print("Veuillez entrer une note entre 0 et 20.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        noms.append(nom)
        notes.append(note)

    return noms, notes

def calculer_moyenne(notes):
    return sum(notes) / len(notes)

def afficher_repartition(noms, notes):
    reussite = []
    echec = []

    for i in range(len(notes)):
        if notes[i] >= 10:
            reussite.append(noms[i])
        else:
            echec.append(noms[i])

    print("\nÉtudiants ayant réussi :", ", ".join(reussite))
    print("Étudiants en échec :", ", ".join(echec))

def meilleure_note(noms, notes):
    
    index_meilleure = notes.index(max(notes))
    print(f"\nL'étudiant ayant la meilleure note est {noms[index_meilleure]} avec {notes[index_meilleure]}.")

def trier_etudiants(noms, notes):

    etudiants = list(zip(notes, noms))
    etudiants.sort(reverse=True, key=lambda x: x[0])

    print("\nClassement des étudiants :")
    for i, (note, nom) in enumerate(etudiants):
        print(f"{i + 1}. {nom} - {note}")


def rechercher_etudiant(noms, notes):
   
    nom_recherche = input("\nEntrez le nom de l'étudiant à rechercher : ")
    if nom_recherche in noms:
        index = noms.index(nom_recherche)
        print(f"{nom_recherche} a obtenu la note de {notes[index]}.")
    else:
        print(f"{nom_recherche} n'est pas dans la liste des étudiants.")

def main():
   
    noms, notes = saisir_donnees()

    moyenne = calculer_moyenne(notes)
    print(f"\nLa moyenne de la classe est de {moyenne:.2f}.")

    afficher_repartition(noms, notes)

    meilleure_note(noms, notes)

    trier_etudiants(noms, notes)

    rechercher_etudiant(noms, notes)


if __name__ == "__main__":
    main()
