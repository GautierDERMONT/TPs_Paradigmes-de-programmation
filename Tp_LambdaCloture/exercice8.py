#====Question 3====:
def calculateDiscount(products, discount_func):
    total = sum(products)
    return total - discount_func(total)

#====Question 4====:
products = [100, 200, 300, 400]
discount = lambda total: total * 0.20

total_after_discount = calculateDiscount(products, discount)
print("Montant total après réduction de 20% :", total_after_discount)