import random

from hangman_art import stages, logo
from hangman_words import word_list

word_list = ["aardvark", "baboon", "camel"]

lives = 6

print(logo)

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for index in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(
        f"**************************** {lives}/6 LIVES LEFT ****************************"
    )

    guess = input("Guess a letter: ").lower()

    display = ""
    for char in chosen_word:
        if guess == char:
            display += char
            correct_letters.append(guess)
        elif char in correct_letters:
            display += char
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(
                f"*********************** IT WAS {chosen_word}! YOU LOSE **********************"
            )

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")
