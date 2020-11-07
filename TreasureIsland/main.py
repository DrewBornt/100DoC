print("Welcome to Treasure Island.")
print("Can you navigate to find the treasure?")
print("Careful, the wrong path is deadly.")

playing = True
while(playing):

    print("You have beached on the island.")
    first_direction = input("You can go either LEFT or RIGHT:\n")

    if( first_direction == "RIGHT"):
        
        print("You fell into a trap hole.")
        print("GAME OVER")

    else:

        print("Your path has brought you to a river.")
        second_direction = input("Do you SWIM across or WAIT?\n")

        if( second_direction == "SWIM"):

            print("The current is too strong and you drown in the river.")
            print("GAME OVER.")
        
        else:
            print("An abandoned boat drifts down the river and allows you to cross.")
            print("Your path comes to a building with 3 doors.")
            third_choice = input("What color door do you take? RED, YELLOW, or BLUE?\n")

            if( third_choice == "BLUE"):
                print("You enter through the door, and it locks behind you. The walls begin to close in on you.")
                print("GAME OVER")
            elif( third_choice == "RED"):
                print("You enter through the door, and it locks behind you. The ceiling begins to come down on you.")
                print("GAME OVER")
            else:
                print("You enter through the door. There is a chamber with a single ray of light shining down onto a large pile of gold.")
                print("Congratulations! You found the treasure!")
                playing = False
    
    keepPlaying = input("Do you want to try again? YES or NO?\n")
    if( keepPlaying == "NO"):
        playing = False
        


