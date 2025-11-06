import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors:")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer chose: {computer}")

    if user == computer:
        return "Its a tie!"

    # r>s, s>p, p>r
    if is_win(user, computer):
        return 'You won!'
    return 'You lost!'
    
def is_win(player, opponent):
    # return True if player wins
    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return True
print(play())


while True:
    print("\n Rock Paper Scissors Game ")
    print(play())

    again = input("Do you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing! Goodbye!")
        break