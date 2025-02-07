#====Question 1====:
def filterMap(filter_func, map_func, lst):
    return [map_func(item) for item in lst if filter_func(item)]

#====Question 2====:
strings = ["hello", "", "world", " ", "python", ""]
filtered_mapped_strings = filterMap(lambda s: s.strip() != "", lambda s: s.upper(), strings)
print("Liste filtrée et transformée :", filtered_mapped_strings)