def init_board():

    rows = ["A","B","C"]

    columns = ["1","2","3"]

    board = [".",".",".",
            ".",".",".",
            ".",".","."]


    print("   " + columns[0] + "   " +columns[1]  +"   " + columns[2])
    print(rows[0] + "  " + board[0] + " | " + board[1] + " | "  + board[2]) 
    print(rows[1] + "  " + board[3] + " | " + board[4] + " | "  + board[5])
    print(rows[2] + "  " + board[6] + " | " + board[7] + " | "  + board[8]) 


def get_move():
    coor=input("Give a row (a,b or c): ")

    if coor == "1a" or "a1":
        board[0] = "X"





init_board()
get_move()