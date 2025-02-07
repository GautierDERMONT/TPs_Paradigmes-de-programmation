#====Question 1====: 
from typing import List

def addToEach(n: int, lst: List[int]) -> List[int]:
    return [x + n for x in lst]  # Création d'une nouvelle liste sans modifier l'originale

#====Question 2====:
def removeDuplicates(lst: List[int]) -> List[int]:
    return list(dict.fromkeys(lst))  # Utilisation d'un dictionnaire pour préserver l'ordre sans doublons

test_list = [1, 2, 2, 3, 4, 4, 5]
n = 3
print(addToEach(n, test_list))  # [4, 5, 5, 6, 7, 7, 8]
print(removeDuplicates(test_list))  # [1, 2, 3, 4, 5]
