import sys
rows = ["A","B","C"]
columns = ["1","2","3"]
player_chars=[".","X","O"]
current_player=1
def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""

    return [[0,0,0],
            [0,0,0],
            [0,0,0]]



def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    error_message="Wrong input, try again!"
    row, col = 0, 0
    is_valid=False
    while is_valid==False:
        coordinates=input("Player "+ str(player) +" Give a row and column: ")
        if coordinates=="quit":
            row, col = -1, -1
            break
        if len(coordinates)!=2:
            print(error_message)
            continue
        a=coordinates[0].upper()
        b=coordinates[1]
        if not a.isalpha() or not b.isdigit():
            print(error_message)
            continue
        if  a not in rows or b not in columns:
            print(error_message)
            continue
        row=rows.index(a)
        col=columns.index(b)
        if board[row][col]!=0:
            print(error_message)
            continue
        is_valid=True   
    
    return row, col


def get_ai_move():
    """Returns the coordinates of a valid move for player on board."""
    print("itt még nincs semmi")
    
    
    """row, col = 0, 0
    return row, col"""


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col]=player
    
    pass


def has_won(board):
    """Returns True if player has won the game."""
  
    row1 = board[0][0] == board[0][1] == board[0][2] == current_player 
    row2 = board[1][0] == board[1][1] == board[1][2] == current_player
    row3 = board[2][0] == board[2][1] == board[2][2] == current_player
   
    column1 = board[0][0] == board[1][0] == board[2][0] == current_player
    column2 = board[0][1] == board[1][1] == board[2][1] == current_player
    column3 = board[0][2] == board[1][2] == board[2][2] == current_player

    across1 = board[0][0] == board[1][1] == board[2][2] == current_player
    across2 = board[0][2] == board[1][1] == board[2][0] == current_player
    
    if row1 or row2 or row3:
        return True
        
    elif column1 or column2 or column3:
        return True

    elif across1 or across2:
        return True

    return False


def is_full(board):
    """Returns True if board is full."""
    for list_item in board:
        if 0 in list_item:
            return False
    return True


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""

    print("   " + columns[0] + "   " +columns[1]  +"   " + columns[2])
    board_elements=""
    for i in range(len(board)):
        board_elements=board_elements+rows[i] + "  "
        for j in range(len(board[i])):
            board_elements=board_elements +player_chars[board[i][j]]
            if j!=len(board[i]) - 1:
                board_elements=board_elements+ " | "
        print(board_elements) 
        if i!=len(board)-1:
            print("  ---+---+---")
        board_elements=""
        i+=1
    



def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner==0:
        print("It's a tie")
    else:
        print(player_chars[winner]+" WON!")
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    global current_player
    current_player=1


    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    while True:
        print_board(board)
        row, col = get_move(board, current_player)
        if row==-1 and col==-1:
            return
        mark(board, current_player, row, col)
        if has_won(board):
            winner=current_player
            break
        if is_full(board):
            winner = 0
            break
        if current_player==1:
            current_player=2
        else:
            current_player=1

    print_board(board)
    print_result(winner)

def main_menu():
    mode=input("Choose number: 1- two-player mode or 2- AI mode ")
    if mode=="1":
        tictactoe_game('HUMAN-HUMAN')
    elif mode=="2":
       get_ai_move() 


if __name__ == '__main__':
    main_menu()