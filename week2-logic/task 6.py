"""tic tac toe"""

won=0
ttt=[["","",""],["","",""],["","",""]]
player=" x "
def giveboard():
    global ttt
    for i in range(3):
        print("-------------------")
        for k in range(3):
            if ttt[i][k] == "":
                print("|", f"{i},{k}",end=" " )
            else:
                print("|",ttt[i][k],end=" ")
        print("|")
    print("-------------------")

def play():
    #a,b=0,0
    global won,player
    global ttt
    if won==0 and "" in ttt[0] or "" in ttt[1] or "" in ttt[2]:
        if player == " x ":
            a,b=map(int,input("Player 1 turn\n enter cell coordinates: ").split())
            ttt[a][b]=" x "
            if checkwin(a,b):
                print("\n Game over !....Player 1 wins!")
                won=1
                return False
            else:
                player=" o "
                return True
        else:
            a, b = map(int, input("Player 2 turn\n enter cell coordinates: ").split())
            ttt[a][b]=" o "
            if checkwin(a,b):
                print("\n Game over !....Player 2 wins!")
                won=1
                return False
            else:
                player=" x "
                return True

def checkwin(a,b):
    global player
    winning_combinations = [
        ([0,0], [0,1], [0,2]), ([1,0], [1,1], [1,2]), ([2,0], [2,1], [2,2]),  # Rows
        ([0,0], [1,0], [2,0]), ([0,1], [1,1], [2,1]), ([0,2], [1,2], [2,2]),  # Columns
        ([0,0], [1,1], [2,2]), ([0,2], [1,1], [2,0])  # Diagonals
    ]
    for combo in winning_combinations:
        if all(ttt[i][j] == player for i,j in combo):
            return True
    return False

a=True
while(a):
    try:
        giveboard()
        a=play()
    except:
        print("\nsomething went wrong!!!!! \n")
giveboard()


