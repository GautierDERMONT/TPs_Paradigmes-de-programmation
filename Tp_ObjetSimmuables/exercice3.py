from typing import List, Dict
from dataclasses import dataclass
import asyncio
import random

#====Question 1====:
@dataclass(frozen=True)
class Article:
    nom: str
    prix: float
    quantite: int


def ajouter_article(inventaire: List[Article], nouvel_article: Article) -> List[Article]:
    return inventaire + [nouvel_article]


def mettre_a_jour_quantite(inventaire: List[Article], nom_article: str, nouvelle_quantite: int) -> List[Article]:
    return [Article(a.nom, a.prix, nouvelle_quantite) if a.nom == nom_article else a for a in inventaire]


def supprimer_article(inventaire: List[Article], nom_article: str) -> List[Article]:
    return [a for a in inventaire if a.nom != nom_article]

#====Question 2====: 
@dataclass(frozen=True)
class Commande:
    articles: Dict[str, int]  


def calculer_montant_total(commande: Commande, inventaire: List[Article]) -> float:
    return sum(a.prix * commande.articles[a.nom] for a in inventaire if a.nom in commande.articles)

#====Question 3====:
@dataclass(frozen=True)
class Promotion:
    nom: str
    condition: float  
    reduction: float  


def appliquer_promotions(commande: Commande, inventaire: List[Article], promotions: List[Promotion]) -> float:
    total = calculer_montant_total(commande, inventaire)
    for promo in promotions:
        if total >= promo.condition:
            total -= promo.reduction
    return total

#====Question 4====:

def mettre_a_jour_stock(inventaire: List[Article], commandes: List[Commande]) -> List[Article]:
    inventaire_dict = {a.nom: a for a in inventaire}
    for commande in commandes:
        for nom_article, quantite in commande.articles.items():
            if nom_article in inventaire_dict:
                article = inventaire_dict[nom_article]
                inventaire_dict[nom_article] = Article(article.nom, article.prix, max(0, article.quantite - quantite))
    return list(inventaire_dict.values())


inventaire_test = [Article("Chaise", 50.0, 10), Article("Table", 150.0, 5)]
commande_test = Commande({"Chaise": 2, "Table": 1})
promotions_test = [Promotion("Réduction 10%", 100, 10)]

print(calculer_montant_total(commande_test, inventaire_test))  
print(appliquer_promotions(commande_test, inventaire_test, promotions_test)) 
print(mettre_a_jour_stock(inventaire_test, [commande_test]))
