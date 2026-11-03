
import random

print("===== ROCK PAPER SCISSORS GAME =====")

user_score = 0
computer_score = 0

while True:
    print("\nChoose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1-3): ")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Try again.")
        continue

    options = ["Rock", "Paper", "Scissors"]

    user_choice = options[int(choice) - 1]
    computer_choice = random.choice(options)

    print("\nYour choice:", user_choice)
    print("Computer choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\n===== SCORE =====")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("\nThanks for playing!")
        print("Final Score:", user_score, "-", computer_score)
        break
