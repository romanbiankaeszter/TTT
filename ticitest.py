import sys

def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""
    rows = ["A","B","C"]

    columns = ["1","2","3"]

    board = [".",".",".",
             ".",".",".",
             ".",".","."]

    # players
    p1="X"
    p2="O"
    
    current_player = p1

    #win conditions

    row1 = board[0] == board[1] == board[2] !="."
    row2 = board[3] == board[4] == board[5] !="."
    row3 = board[6] == board[7] == board[8] !="."

    
    column1 = board[0] == board[3] == board[6] !="."
    column2 = board[1] == board[4] == board[7] !="."
    column3 = board[2] == board[5] == board[8] !="."

    across1 = board[0] == board[4] == board[8] !="."
    across2 = board[2] == board[4] == board[6] !="."

    game_running=True



    while game_running:


        print("   " + columns[0] + "   " +columns[1]  +"   " + columns[2])
        print(rows[0] + "  " + board[0] + " | " + board[1] + " | "  + board[2]) 
        print("  ---+---+---")
        print(rows[1] + "  " + board[3] + " | " + board[4] + " | "  + board[5])
        print("  ---+---+---")
        print(rows[2] + "  " + board[6] + " | " + board[7] + " | "  + board[8]) 


        coor=input("Give a row and column: ")


        # player changer

        if current_player==p1:
            current_player=p2
        elif current_player ==p2:
            current_player=p1
        
        # Marker

        if coor == "a1" or coor == "1a":
            board[0]=current_player
        
        if coor == "a2" or coor == "2a":
            board[1]=current_player

        
        if coor == "a3" or coor == "3a":
            board[2]=current_player
        
        if coor == "b1" or coor == "1b":
            board[3]=current_player

        
        if coor == "b2" or coor == "2b":
            board[4]=current_player
        
        if coor == "b3" or coor == "3b":
            board[5]=current_player

        
        if coor == "c1" or coor == "1c":
            board[6]=current_player
        
        if coor == "c2" or coor == "2c":
            board[7]=current_player

        if coor == "c3" or coor == "3c":
            board[8]=current_player


        print("   " + columns[0] + "   " +columns[1]  +"   " + columns[2])
        print(rows[0] + "  " + board[0] + " | " + board[1] + " | "  + board[2]) 
        print("  ---+---+---")
        print(rows[1] + "  " + board[3] + " | " + board[4] + " | "  + board[5])
        print("  ---+---+---")
        print(rows[2] + "  " + board[6] + " | " + board[7] + " | "  + board[8]) 



        if row1 or row2 or row3:
            game_running=False

        if column1 or column2 or column3:
            game_running=False

        if board[0]=="X":
            print("thx for playing!")
            sys.exit(0)

    if board[0]=="X":
        sys.exit(0)
        print("thx for playing!")

    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    
    

    
    
    
    row, col = 0, 0
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
   
    
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    
    return False


def is_full(board):
    """Returns True if board is full."""
    
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()


"""
def get_move():
    coor=input("Give a row (a,b or c): ")

    if coor == "1a" or "a1":
        board[0] = "X"
"""