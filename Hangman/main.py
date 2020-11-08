import random
import hangman_words
import hangman_art


chosen_word = random.choice(hangman_words.word_list)
wordLength = len(chosen_word)

lettersGuessedList = []
lettersGuessedText = ""

print(chosen_word)

print(hangman_art.logo)

lives = 6

displayList = []
displayText = ""

for letter in chosen_word:
    displayList.append("_")

for space in displayList:
    displayText += space

while True:

    print(hangman_art.stages[lives])
    print(f"Guess a letter: {displayText}")
    
    lettersGuessedText = ""

    for guessedLetters in lettersGuessedList:
        lettersGuessedText += guessedLetters
        lettersGuessedText += ".. "

    print(f"You have already guessed: {lettersGuessedText}")



    guess = input("Guess a letter in the word: ").lower()

    if guess not in lettersGuessedList:

        lettersGuessedList.append(guess)
            
        for position in range(wordLength):
            if chosen_word[position] == guess:
                displayList[position] = guess

        if guess not in chosen_word:
            lives -= 1
            print(f"The letter, {guess}, was not in the word!\nYou have {lives} lives left!")

        if lives == 0:
            print(f"You lose! The word was {chosen_word}!")
            break

        displayText = ""

        for letter in displayList:
            displayText += letter 
        print(displayText)

        if displayText == chosen_word:
            print("You win!")
            break

    else:
        print("You already guessed that letter!")

    

# I didn't follow the course verbatim, but rather kept my own interpretations of the challenges.
# The only thing I changed from what I wrote vs what was in the challenge was the 'from position in range'
# because I declared an i variable before the loop to track position, but this method was much better.