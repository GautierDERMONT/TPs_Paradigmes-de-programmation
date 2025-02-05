recettes = {
    "pizza": ["farine", "eau", "sel", "levure", "tomate", "fromage"],
    "salade": ["laitue", "tomate", "concombre", "vinaigre", "huile"],
    "carbonara": ["pates", "creme", "lardons", "fromage", "sel", "poivre"],
    "omelette": ["oeufs", "sel", "poivre", "fromage", "herbes"],
    "sandwich jambon-beurre": ["pain", "beurre", "jambon"],
    "sandwich salade": ["pain", "beurre", "jambon", "salade"],
}

def recettes_realisables(ingredients_disponibles, recettes):
    filtre = filter(lambda recette: all(ing in ingredients_disponibles for ing in recettes[recette]), recettes)
    return list(map(str.capitalize, filtre))


ingredients_utilisateur = {"pain", "beurre", "jambon", "oeufs", "sel", "poivre", "fromage", "herbes"}
recettes_possibles = recettes_realisables(ingredients_utilisateur, recettes)

print("Recettes réalisables:", recettes_possibles)
