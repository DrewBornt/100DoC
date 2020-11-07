import random

# I realize the actual 100 days of code series doesn't have loops or functions yet, but I wanted to incorporate whatever I could
# The logic between choices, results, and ascii art could be a bit more refined, but.. this is just an exercise, right?

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = ["ROCK", "PAPER", "SCISSORS"]
asciiArt = [rock, paper, scissors]

def displayASCIIArt(choice):
    if (choice == "ROCK"):
        return asciiArt[0]
    elif (choice == "PAPER"):
        return asciiArt[1]
    elif (choice == "SCISSORS"):
        return asciiArt[2]


def result(pChoice, cChoice):

    if (pChoice == cChoice):
        return "DRAW!"

    elif (pChoice == "ROCK" and cChoice == "PAPER"):
        return "You lose!"

    elif (pChoice == "ROCK" and cChoice == "Scissors"):
        return "You Win!"

    elif (pChoice == "PAPER" and cChoice == "SCISSORS"):
        return "You lose!"

    elif (pChoice == "PAPER" and cChoice == "ROCK"):
        return "You win!"
    
    elif (pChoice == "SCISSORS" and cChoice == "PAPER"):
        return "You win!"

    elif (pChoice == "SCISSORS" and cChoice == "ROCK"):
        return "You lose!"


print("Let's play Rock, Paper, Scissors!")

playing = True

while( playing ):

    verified = False

    while not verified:
        player_choice = str(input("Choose either, ROCK, PAPER, or SCISSORS: "))

        if (player_choice == "ROCK" or player_choice == "PAPER" or player_choice == "SCISSORS"):
            break

        else:
            print("Please choose either ROCK, PAPER, or SCISSORS.")

    
    computer_choice = choices[random.randint(0,2)]

    print(f"Your choice was {player_choice}")
    print(displayASCIIArt(player_choice))

    print(f"The computer chose {computer_choice}")
    print(displayASCIIArt(computer_choice))

    print(result(player_choice, computer_choice))

    replayChoice = input("Play again? NO, otherwise any key to play again? ")

    if (replayChoice == "NO"):
        playing = False

