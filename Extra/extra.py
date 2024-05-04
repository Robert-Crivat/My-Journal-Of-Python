import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

restart = True
while restart == True :
    restart = False
    print("Welcome to ")
    moves = [rock, paper, scissors]
    pc = moves[random.randint(0,2)]

    user = input("What do you choose?\nType 0 for Rock, 1 for Paper, 2 for Scissors\n")
    print(moves[int(user)])

    if (moves[int(user)] == pc):
        print(f"computer choose : {pc} \n this is tie")
    elif (moves[int(user)] == moves[0] and pc == moves[2]):
        print(f"computer choose : {pc} \n you winn")
    elif (moves[int(user)] == moves[1] and pc == moves[0]):
        print(f"computer choose : {pc} \n you winn")
    elif (moves[int(user)] == moves[2] and pc == moves[1]):
        print(f"computer choose : {pc} \n you winn")
    else:
        print(f"computer choose : {pc} \n you lose")
    if (input("insert Y for restart the game : ") == "Y"):
        restart = True