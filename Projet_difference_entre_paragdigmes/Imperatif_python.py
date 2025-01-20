recettes = {
    "pizza": ["farine", "eau", "sel", "levure", "tomate", "fromage"],
    "salade": ["laitue", "tomate", "concombre", "vinaigre", "huile"],
    "carbonara": ["pates", "creme", "lardons", "fromage", "sel", "poivre"],
    "omelette": ["oeufs", "sel", "poivre", "fromage", "herbes"],
    "sandwich jambon-beurre": ["pain", "beurre", "jambon"],
    "sandwich salade": ["pain", "beurre", "jambon", "salade"],
}


def recettes_possibles(ingredients_dispo):
    recettes_realisees = []
    for recette, ingredients_recette in recettes.items():
        if all(ingredient in ingredients_dispo for ingredient in ingredients_recette):
            recettes_realisees.append(recette)
    return recettes_realisees

if __name__ == "__main__":

    ingredients_dispo = ["farine", "eau", "sel", "levure", "tomate", "fromage"]
    print("Ingrédients disponibles :", ingredients_dispo)
    print("Recettes possibles :", recettes_possibles(ingredients_dispo))


    ingredients_dispo = ["pain", "beurre", "jambon", "salade"]
    print("\nIngrédients disponibles :", ingredients_dispo)
    print("Recettes possibles :", recettes_possibles(ingredients_dispo))


    ingredients_dispo = ["oeufs", "sel", "poivre", "fromage"]
    print("\nIngrédients disponibles :", ingredients_dispo)
    print("Recettes possibles :", recettes_possibles(ingredients_dispo))
