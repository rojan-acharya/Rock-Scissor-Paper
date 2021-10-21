import random

def game(comp, user):
    '''This function decides the winner or losser of the game.'''
    if comp == user:
        return None
    elif comp == "s":
        if user == "p":
            return False
        elif user == "r":
            return True
    elif comp == "p":
        if user == "r":
            return False
        elif user == "s":
            return True
    elif comp == "r":
        if user == "s":
            return False
        elif user == "p":
            return True
print("\n")
print("\t******Rock, Paper and Scissor Game******")
print("\n")
print("\tComputer,s Turn:")
random_num = random.randint(1,3)
if random_num == 1:
    comp = 's'
elif random_num == 2:
    comp = "p"
elif random_num == 3:
    comp = "r"
user = input("\tUser's Turn, Please pick any one option\nScissor(s), Paper(p) or Rock(r) : ")

print(f"Computer has choosen -> {comp}")
print(f"User has choosen -> {user}")

result = game(comp, user)
if result == None:
    print("The game is Tie!")
elif result == True:
    print("You win the game.")
else:
    print("You lose the game.")