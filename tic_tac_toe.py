print('''
Rules:
Player1 is X
Player2 is O
      
col_0  col_1  col_2
['x',  'y',   'z'] ----> Row 0
['a',  'b',   'c'] ----> Row 1
['d',  'e',   'f'] ----> Row 2

''')

play_board = [["emp","emp","emp"],["emp","emp","emp"],["emp","emp","emp"]]

def show_board():
    global play_board
    for list in play_board:
        print(list)


class Player1:
    choice = "X"
    def __init__(self, name):
        self.name = name
    
    def player1_move(self,c,d):
        global play_board
        play_board[c][d] = Player1.choice
        

class Player2:
    choice = "O"
    def __init__(self, name):
        self.name = name

    def player2_move(self,e,f):
        global play_board
        play_board[e][f] = Player2.choice

a = input("Enter your name, player1 : ")
b = input("Enter your name, player2 : ")

user1 = Player1(a)
user2 = Player2(b)

def winner_checker():
    l = [0,1,2]
    for i in l:
        j = 0
        if play_board[i][j] == play_board[i][j+1] == play_board[i][j+2] == "X" :
            print(f"{user1.name} won !") 
        elif play_board[i][j] == play_board[i][j+1] == play_board[i][j+2] == "O":
            print(f"{user2.name} won !")
        elif play_board[j][i] == play_board[j+1][i] == play_board[j+2][i] == "X" :
            print(f"{user1.name} won !")
        elif play_board[j][i] == play_board[j+1][i] == play_board[j+2][i] == "O" :
            print(f"{user2.name} won !")
        elif play_board[j][j] == play_board[j+1][j+1] == play_board[j+2][j+2] == "X" :
            print(f"{user1.name} won !")
        elif play_board[j][j] == play_board[j+1][j+1] == play_board[j+2][j+2] == "O" :
            print(f"{user2.name} won !")
        elif play_board[0][2] == play_board[1][1] == play_board[2][0] == "X" :
            print(f"{user1.name} won !")
        elif play_board[0][2] == play_board[1][1] == play_board[2][0] == "X" :
            print(f"{user1.name} won !")
        else:
            return 0

count = 0 

def is_filled_checker():
    global count
    for i in range(3):
        for j in range(3):
            if play_board[i][j] != "emp":
                count += 1
        


while True:
    c = int(input(f"Enter the row no. you want to move in, {a} : "))
    d = int(input(f"Enter the column no. you want to move in, {a} : "))
    user1.player1_move(c,d)
    show_board()
    f = winner_checker()

    if f == None:
        break
    
    is_filled_checker()

    if count == 45:
        break

    e = int(input(f"Enter the row no. you want to move in : {b} : "))
    f = int(input(f"Enter the row no. you want to move in : {b} "))
    user2.player2_move(e,f)
    show_board()
    g = winner_checker()

    if g == None:
        break

    is_filled_checker()

    if count == 45:
        break

if f == 0 and g == 0:
    print("It was a draw !")







        



