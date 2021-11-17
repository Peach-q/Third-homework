def palindrome(word):
    if word == word[::-1]:
        print("Полиндром")
    else:
        print("Не полиндром")

text = input("Ведите текст:\n")
palindrome(text.lower().replace(" ", ""))