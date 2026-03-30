import random
import time

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('welcome to rock, paper, scissors! 🗿📃✂️')
def print_dramatic_text(text: str, delay=0.1):
   for char in text:
       print(char, end='', flush=True)
       time.sleep(delay)
   print()
import random
import time


# ðŸŽ® Rock Paper Scissors - Styled Version ðŸŽ®


choices = ["rock", "paper", "scissors"]




def dramatic_text(text, delay=0.02):
   """Print text with a typing effect."""
   for char in text:
       print(char, end="", flush=True)
       time.sleep(delay)
   print()




def countdown():
   """Dramatic countdown like the example."""
   dramatic_text("\nðŸª¨ Rock...")
   time.sleep(0.4)
   dramatic_text("ðŸ“„ Paper...")
   time.sleep(0.4)
   dramatic_text("âœ‚ï¸ Scissors...")
   time.sleep(0.4)
   dramatic_text("ðŸ’¥ SHOOT!\n")
   time.sleep(0.3)




def get_user_choice():
   """Get and validate user input."""
   while True:
       choice = input("ðŸ‘‰ Enter (rock, paper, scissors): ").lower().strip()
       if choice in choices:
           return choice
       else:
           print("âŒ Invalid input. Try again.")




def get_computer_choice():
   """Random computer choice."""
   return random.choice(choices)




def emoji(choice):
   """Return emoji for each choice."""
   if choice == "rock":
       return "ðŸª¨"
   elif choice == "paper":
       return "ðŸ“„"
   else:
       return "âœ‚ï¸"




def decide_winner(user, computer):
   """Determine winner."""
   if user == computer:
       return "tie"
   elif (
       (user == "rock" and computer == "scissors") or
       (user == "paper" and computer == "rock") or
       (user == "scissors" and computer == "paper")
   ):
       return "win"
   else:
       return "lose"




def play_game():
   user_score = 0
   computer_score = 0
   rounds_played = 0


   dramatic_text("ðŸŽ® Welcome to Rock, Paper, Scissors!")
   dramatic_text("ðŸ† First to win 2 out of 3 rounds!\n")


   while user_score < 2 and computer_score < 2:
       rounds_played += 1
       print(f"\nðŸ”¹ Round {rounds_played}")


       user = get_user_choice()
       computer = get_computer_choice()


       countdown()


       print(f"ðŸ™‹ You chose: {emoji(user)} {user}")
       print(f"ðŸ¤– Computer chose: {emoji(computer)} {computer}\n")


       result = decide_winner(user, computer)


       if result == "tie":
           print("âš–ï¸ It's a tie!")
       elif result == "win":
           print("ðŸŽ‰ You win this round!")
           user_score += 1
       else:
           print("ðŸ’» Computer wins this round!")
           computer_score += 1


       print(f"\nðŸ“Š Score: You {user_score} | Computer {computer_score}")


   # Final result
   print("\n" + "=" * 30)
   if user_score > computer_score:
       dramatic_text(f"ðŸ† Congratulations! You won {user_score}/3!")
   else:
       dramatic_text(f"ðŸ’» Game Over! Computer won {computer_score}/3!")
   print("=" * 30)




# Run the game
play_game()