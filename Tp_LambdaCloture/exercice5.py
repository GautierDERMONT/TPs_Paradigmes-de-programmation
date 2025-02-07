#====Question 1====:
def compose(f, g):
    return lambda x: f(g(x))

#====Question 2====:
add_one = lambda x: x + 1
square = lambda x: x ** 2

composed_function = compose(add_one, square)


print("Composition de add_one et square (3) :", composed_function(3))  # Résultat attendu : 10 (3² + 1)