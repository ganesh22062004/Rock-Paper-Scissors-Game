import random

print("🎮 Welcome to Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter Rock, Paper or Scissors: ").lower()

    if user not in choices:
        print("❌ Invalid choice! Please enter Rock, Paper or Scissors.")
        continue

    computer = random.choice(choices)

    print("You chose     :", user)
    print("Computer chose:", computer)

    if user == computer:
        print("🤝 It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You Win!")
    else:
        print("😔 Computer Wins!")

    choice = input("\nDo you want to play again? (y/n): ").lower()
    if choice != "y":
        print("\nThank you for playing! 👋")
        break

