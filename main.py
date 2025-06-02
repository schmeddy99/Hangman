import random


word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for index in range(word_length):
    placeholder += "_"
print(placeholder)


guess = input("Guess a letter: ").lower()


display = ""
for char in chosen_word:
    if guess == char:
        display += char
    else:
        display += "_"


print(display)
