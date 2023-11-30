import random


class Game:

    
    def __init__(self):
        self.player_score = 0
        self.total_rounds = 0
        self.game_over = False

    def increase_score(self, points):
        if not self.game_over:
            self.player_score += points
            print(f"Score increased by {points}. Total score: {self.player_score}")

    def record_result(self):
        if not self.game_over:
            self.total_rounds += 1

    def end_game(self):
        print(f"Game over. Rounds played: {self.total_rounds}. Total score: {self.player_score}")
        self.game_over = True

def play_game():
    while not game_instance.game_over:
        player_choice = input("Please type rock, paper, or scissors. Type 'exit' to end the game.\n").lower()

        if player_choice == "exit":
            game_instance.end_game()
            break

        options = ["rock", "paper", "scissors"]

        if player_choice not in options:
            print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'exit'.")
            continue

        computer_choice = random.choice(options)

        print(f"You chose: {player_choice}, Computer chose: {computer_choice}.")

        if player_choice == computer_choice:
            print("Tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "scissors" and computer_choice == "paper") or
            (player_choice == "paper" and computer_choice == "rock")
        ):
            game_instance.increase_score(1)
            print("You win!")
        else:
            print("You lose.")

        game_instance.record_result()

game_instance = Game()
play_game()