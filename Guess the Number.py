'''
ICT - 104

Members:
- Camus, Mark Dave
- Dizon, Vince
- Dungo, Jann Carl
- Gurango, Francoise
- Lacson, Rhein
- Tienzo, Krisean 
- Parungao, Clarence Lane
- Quiambao, Adan Josh
'''

#import necessary modules
try:
    from players import Player
    import random
    
#print game introduction
    print("In this program, you’re going to make a Guess the Number game.")
    print("The computer will think of a secret number from 1 to 100 and ask the user to guess it.")
    print("After each guess, the computer will tell the user whether the number is too high or too low.")
    print("The user wins if they can guess the number. Good luck!")
    print(" ")

    
#functions for playing a one-player game
    def play_one_player_game(player):
        quit_game = False
        while not quit_game:
            random_number = random.randint(1, 100)#Generate a random number for the game
            print("\nNew game")

            play = True
            while play:# Let the player enter a guess and check if they want to continue playing
                play = player.enter_guess(random_number, play)
                
# Display the player's score after the game
            print(f"\nScore: {player.name} {player.score}")
            
 # Ask if the player wants to play again
            keep_playing = input("\nDo you want to play again? (y/n): ")
            if keep_playing.lower() == 'n':
                print("Thank you for playing!")
                quit_game = True
            elif keep_playing.lower() != 'y':
                quit_game = True
                print("Invalid input!")
                
# Function for playing a two-player game
    def play_two_player_game(player1, player2):
        quit_game = False
        while not quit_game:
            random_number = random.randint(1, 100) # Generate a random number for the game
            print("\nNew game")

             # Randomly select the first player for each round
            first_player = random.choice([player1, player2])
            second_player = player1 if first_player == player2 else player2

            play = True
            while play:# Let both players enter their guesses and check if they want to continue playing
                play = first_player.enter_guess(random_number, play)
                play = second_player.enter_guess(random_number, play)
                
# Display the scores of both players after the game
            print(f"\nScore: {first_player.name} {first_player.score} | {second_player.name} {second_player.score}")
            
# Ask if the players want to play again
            keep_playing = input("\nDo you want to play again? (y/n): ")
            if keep_playing.lower() == 'n':
                print("Thank you for playing!")
                quit_game = True
            elif keep_playing.lower() != 'y':
                quit_game = True
                print("Invalid input!")
                
# Main entry point of the program
    if __name__ == "__main__":
        print("In this program, you're going to make a Guess the Number game.")
         # Prompt the user to choose a game mode
        choice = int(input("Choose a game mode: [1] One Player or [2] Two Players: "))

        if choice == 1: # For one player, create a player object and start the game
            player1 = Player(input("Enter your name: "))
            play_one_player_game(player1)
        elif choice == 2:# For two player, create two player object and start the game
            player1 = Player(input("Player 1, enter your name: "))
            player2 = Player(input("Player 2, enter your name: "))
            play_two_player_game(player1, player2)
        else:
            print("Invalid choice. Please choose either 1 or 2.")

except ValueError:
    print("Wrong Value!")



'''
https://drive.google.com/file/d/1rJPkBvW4I7V5ndId8ELP6OS0wokyYUM8/view?fbclid=IwAR2WqWGx6LkT5yzPYC8d885ndMEouvN0LZB7drG_mbSmF50SPtOqEpGYnvA
'''

