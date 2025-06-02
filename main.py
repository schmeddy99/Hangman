import random

word_list = ["aardvark", "baboon", "camel"]
placeholder = ""
display = ""


chosen_word = random.choice(word_list)
print(chosen_word)

for letter in chosen_word:
    print("_", end="")

print("")
guess = input("Guess a letter: ").lower()


for char in chosen_word:
    if guess == char:
        print(char)
    else:
        print("_")

print(display)
