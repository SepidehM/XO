
import os


def draw_board(board, x, y):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(x):
        print(''.join([char*(x*2+1) for char in '-']))
        s='|'
        for j in range(y):
            s += board[i][j]+"|"
        print(s)
    print(''.join([char*(x*2+1) for char in '-']))

def check_board_free(board, x, y):
    for i in range(x):
        for j in range(y):
            if board[i][j] == ' ':
                return True
    return False


def check_turn(board, x, y, turn):
    for i in range(x):
        for j in range(y):
            if j<y-2 and board[i][j]==str(turn) and board[i][j+1]==str(turn) and board[i][j+2]==str(turn):
                return True
            if i<x-2 and board[i][j]==str(turn) and board[i+1][j]==str(turn) and board[i+2][j]==str(turn):
                return True
            if i<x-2 and j<y-2 and board[i][j]==str(turn) and board[i+1][j+1]==str(turn) and board[i+2][j+2]==str(turn):
                return True
            if i>2 and j>2 and board[i][j]==str(turn) and board[i-1][j-1]==str(turn) and board[i-2][j-2]==str(turn):
                return True
            
    return False


print("enter number of player:")
n = int(input())

print("row and col board:")
x,y = [int(i) for i in input().split(' ')]
print((x,y))
board = []
for i in range(x):
    board.append([])
    for j in range(y):
        board[i].append(' ')


turn = -1

end_game = False

while (not end_game) and check_board_free(board, x, y):
    turn +=1
    turn = turn % n
   
    draw_board(board, x, y)
    valid_input = False
    a = 0
    b = 0
    while not valid_input:
        print("player"+str(turn)+", please select your box:")
        a,b = [int(i) for i in input().split(' ')]
        if a > x or b > y or board[a][b] != ' ' :
            print("invalid input!")
        else:
           valid_input = True

    board[a][b] = str(turn)

    end_game = check_turn(board, x, y, turn)

if end_game:
    print("player number"+str(turn)+" is winner!")
else:
    print("no winner!")







