import random
print("Welcome to the Rock, Paper, Scissors game:")
rules=input("Press Enter to continue or type (Help) for the rules help.\n ").capitalize()
if rules=="Help":
  print("""
                ********* Rules *********
                1) You choose and the computer chosses
                2) Rock smaches Scissors -> Rock wins
                3) Scissors cut Paper -> Scissos win
                4) Paper covers Rock -> Paper win \n \n \n """)
choices=["Rock","Paper","Scissors"]
choice=input("Enter your choise (Rock, Paper, Scissors):\n \n\n ").capitalize()
if choice in choices:
  if choice=="Paper":
    print("""
        _______ 
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)         
    """)
  elif choice=="Scissors":
    print("""
        _______ 
    ---'   ____)____
              ______)
              _______)
          (____)
    ---.__(___)
    """)
  else:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.______)
    """)
  computer_choice=random.choice(choices)
  print(" The computer choise is: \n ")
  if computer_choice=="Paper":
    print("""
        _______ 
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)      
    """)
  elif computer_choice=="Scissors":
    print("""
        _______ 
    ---'   ____)____
              ______)
              _______)
          (____)
    ---.__(___)
    """)
  else:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.______)
    """)
  if computer_choice=="Rock" and choice=="Scissors":
    result=("computer win")
    cause=("The Rock smached the Scissors")
  elif computer_choice=="Rock" and choice=="Paper":
    result=("computer lose")
    cause=("The Paper covers the Rock")
  elif computer_choice=="Paper" and choice=="Scissors":
    result=("computer lose")
    cause=("The Scissors beats the Paper")
  elif computer_choice=="Paper" and choice=="Rock":
    result=("computer win")
    cause=("The Paper covers the Rock")
  elif computer_choice=="Scissors" and choice=="Rock":
    result=("computer lose")
    cause=("The Rock breaks the Scissors")
  elif computer_choice=="Scissors"and choice=="Paper":
    result=("computer win")
    cause=("The Scissors cut the Paper")
  else:
    result=("Draw")
    cause=(f"The computer choise is {computer_choice} and Your choice is {choice}")
  if result=="computer win":
    print("You lose! ",cause)
  elif result=="computer lose":
    print("You win. ",cause)
  else:
    print("You drew against the computer.",cause)
else:
  print("\n Invalid choice. Please run the program again and choose Rock, Paper, Scissors.")