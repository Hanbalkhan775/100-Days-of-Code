import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for i in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_words = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_words.append(letter)
        elif letter in correct_words:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")