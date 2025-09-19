import random

def roll_dice():
    """Simulates rolling a standard six-sided die."""
    return random.randint(1, 6)

def play_game():
    """
    Main function to run the Snakes and Ladders game.
    The game board is a dictionary where keys are snake/ladder heads and values are their tails.
    """
    board = {
        # Snakes
        16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78,
        # Ladders
        1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100
    }
    
    players = {"Player 1": 0, "Player 2": 0}
    player_names = list(players.keys())
    game_over = False

    while not game_over:
        for player in player_names:
            input(f"\n{player}, press Enter to roll the dice...")
            roll = roll_dice()
            print(f"You rolled a {roll}.")
            
            new_position = players[player] + roll
            
            if new_position > 100:
                print("Can't move, you need to roll exactly to win!")
            else:
                if new_position in board:
                    final_position = board[new_position]
                    if final_position > new_position:
                        print(f"🤩 You landed on a ladder! Move up from {new_position} to {final_position}.")
                    else:
                        print(f"🐍 Oh no, you landed on a snake! Slide down from {new_position} to {final_position}.")
                    players[player] = final_position
                else:
                    players[player] = new_position
                
                print(f"Your new position is {players[player]}.")
            
            if players[player] == 100:
                print(f"\n🎉 Congratulations, {player} wins the game!")
                game_over = True
                break

if __name__ == "__main__":
    play_game()