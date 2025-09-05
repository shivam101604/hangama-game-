import random

# List of 5 predefined words
word_list = ['apple', 'banana', 'cherry', 'grape', 'orange']
chosen_word = random.choice(word_list)

# Game setup
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Create blank display
display = ['_' for _ in chosen_word]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses. Good luck!\n")

while incorrect_guesses < max_guesses and '_' in display:
    print("Word: ", ' '.join(display))
    print(f"Guessed Letters: {', '.join(guessed_letters)}")
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("❗ You've already guessed that letter. Try again.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display[i] = guess
        print("✅ Correct guess!\n")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! You have {max_guesses - incorrect_guesses} tries left.\n")

# Final result
if '_' not in display:
    print(f"🎉 You won! The word was: {chosen_word}")
else:
    print(f"💀 You lost. The word was: {chosen_word}")
