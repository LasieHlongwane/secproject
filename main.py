print("Hello welcome to Rock - Paper - Scissors")


def playerOne():
    print("Player 1 WINS!")


def playerTwo():
    print("Player 2 WINS!")


def Draw():
    print("Draw")


player1 = int(input("""Player one, your turn:
1. Rock
2. Paper
3. Scissors
Pick an option (enter a number)
"""))

player2 = int(input("""Player two, your turn:
1. Rock
2. Paper
3. Scissors
Pick an option (enter a number)
"""))

if player1 == 1 and player2 == 3:
    playerOne()
elif player2 == 1 and player1 == 3:
    playerTwo()
elif player1 == 1 and player2 == 1:
    Draw()
elif player1 == 3 and player2 == 2:
    playerOne()
elif player2 == 3 and player1 == 2:
    playerTwo()
elif player1 == 2 and player2 == 2:
    Draw()
elif player1 == 2 and player2 == 1:
    playerOne()
elif player2 == 2 and player1 == 1:
    playerTwo()
elif player1 == 3 and player2 == 3:
    Draw()
else:
    quit()
    