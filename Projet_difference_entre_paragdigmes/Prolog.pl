recette(pizza, [farine, eau, sel, levure, tomate, fromage]).
recette(salade, [laitue, tomate, concombre, vinaigre, huile]).
recette(carbonara, [pates, creme, lardons, fromage, sel, poivre]).
recette(omelette, [oeufs, sel, poivre, fromage, herbes]).
recette(sandwich_jambon_beurre, [pain, beurre, jambon]).
recette(sandwich_salade, [pain, beurre, jambon, salade]).


tous_ingredients_disponibles([], _).
tous_ingredients_disponibles([Ing|Reste], IngredientsDispo) :-
    member(Ing, IngredientsDispo),
    tous_ingredients_disponibles(Reste, IngredientsDispo).


recette_disponible(IngredientsDispo, Recette) :-
    recette(Recette, IngredientsRecette),
    tous_ingredients_disponibles(IngredientsRecette, IngredientsDispo).

