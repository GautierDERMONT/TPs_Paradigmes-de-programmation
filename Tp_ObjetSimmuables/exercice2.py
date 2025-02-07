from typing import List
from dataclasses import dataclass
import asyncio
import random


#====Question 1====: 
@dataclass(frozen=True)
class Personne:
    nom: str
    age: int

#====Question 2====:
def anniversaire(personnes: List[Personne]) -> List[Personne]:
    return [Personne(p.nom, p.age + 1) for p in personnes]

#====Question 3====:
async def getRandomNumber() -> int:
    await asyncio.sleep(1)  
    return random.randint(1, 100)

#====Question 4====: 
async def main():
    num1 = await getRandomNumber()
    num2 = await getRandomNumber()
    print(f"Nombre aléatoire 1: {num1}")
    print(f"Nombre aléatoire 2: {num2}")

if __name__ == "__main__":
    asyncio.run(main())


def addToEach(n: int, lst: List[int]) -> List[int]:
    return [x + n for x in lst]

def removeDuplicates(lst: List[str]) -> List[str]:
    return list(dict.fromkeys(lst))

test_list = [Personne("Jhin", 25), Personne("Zac", 30)]
n = 3
print(addToEach(n, [p.age for p in test_list]))  
print(removeDuplicates([p.nom for p in test_list]))  
print(anniversaire(test_list))  
