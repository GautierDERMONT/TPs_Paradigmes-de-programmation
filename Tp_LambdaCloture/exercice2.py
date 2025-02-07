#====Question 2.1====:
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

#====Question 2.2=====:
double = create_multiplier(2)
triple = create_multiplier(3)

#====Question 2.3====:
print("Double de 5 :", double(5))  
print("Triple de 5 :", triple(5))  