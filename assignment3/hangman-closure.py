# Task 4.1 and 4.2: Create the hangman closure
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        displayed_word = ""

        for character in secret_word:
            if character in guesses:
                displayed_word += character
            else:
                displayed_word += "_"

        print(displayed_word)

        return all(character in guesses for character in secret_word)

    return hangman_closure


# Task 4.3: Play the hangman game
secret_word = input("Enter the secret word: ").lower()

hangman = make_hangman(secret_word)

while True:
    guess = input("Guess a letter: ").lower()

    if hangman(guess):
        print("Congratulations! You guessed the word!")
        break
