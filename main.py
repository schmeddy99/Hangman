import random

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()
print(guess)

for char in chosen_word:
    if guess == char:
        print("Right")
    else:
        print("Wrong")
