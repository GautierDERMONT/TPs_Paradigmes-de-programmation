#====Question 3.1====:
words = ["apple", "banana", "avocado", "cherry", "apricot", "blueberry"]

#====Question 3.2====:
words_starting_with_a = list(filter(lambda word: word.startswith('a'), words))
print("Mots commençant par 'a' :", words_starting_with_a)


def count_long_words(words):
    def is_long(word):
        return len(word) > 5
    return len(list(filter(is_long, words)))

long_word_count = count_long_words(words)
print("Nombre de mots de longueur > 5 :", long_word_count)