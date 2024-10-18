from random import random

def tictactor():
    board = ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]

    name1 = input("Player 1 name?")
    name2 = input("Player 2 name")
    win = False
    numOfTurns = 0
    while win == False:
        print("", board[0][0], "|", board[0][1], "|", board[0][2])
        print("---|---|---")
        print("", board[1][0], "|", board[1][1], "|", board[1][2])
        print("---|---|---")
        print("", board[2][0], "|", board[2][1], "|", board[2][2])
        print("===========================================================")
        
        available = False
        print("Turn:", name1)
        while available == False:
            row = input("What row would you like to place an X in? (1-3)")
            while isnum(row) == False or int(row) > 3 or int(row) < 1:
                print("Please enter a number in range")
                row = input("What row would you like to place an X in? (1-3)")
            column = input("What column would you like to place an X in? (1-3)")
            while isnum(column) == False or int(column) > 3 or int(column) < 1:
                print("Please enter a number in range")
                column = input("What column would you like to place an X in? (1-3)")
            if board[int(row) - 1][int(column) - 1] != "-":
                print("That space is not available!")
            else:
                board[int(row) - 1][int(column) - 1] = "X"
                available = True
        
        for i in range(3):
            if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
                print(name1, "has won!")
                return name1, "has won!"
            if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
                print(name1, "has won!")
                return name1, "has won!"
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            print(name1, "has won!")
            return name1, "has won!"
        if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
            print(name1, "has won!")
            return name1, "has won!"
        
        numOfTurns += 1
        
        if numOfTurns == 9:
            print("", board[0][0], "|", board[0][1], "|", board[0][2])
            print("---|---|---")
            print("", board[1][0], "|", board[1][1], "|", board[1][2])
            print("---|---|---")
            print("", board[2][0], "|", board[2][1], "|", board[2][2])
            print("===========================================================")
            print("Draw")
            break

        print("", board[0][0], "|", board[0][1], "|", board[0][2])
        print("---|---|---")
        print("", board[1][0], "|", board[1][1], "|", board[1][2])
        print("---|---|---")
        print("", board[2][0], "|", board[2][1], "|", board[2][2])
        print("===========================================================")

        available = False
        print("Turn:", name2)
        while available == False:
            row = input("What row would you like to place an O in? (1-3)")
            while isnum(row) == False or int(row) > 3 or int(row) < 1:
                print("Please enter a number in range")
                row = input("What row would you like to place an O in? (1-3)")
            column = input("What column would you like to place an O in? (1-3)")
            while isnum(column) == False or int(column) > 3 or int(column) < 1:
                print("Please enter a number in range")
                column = input("What column would you like to place an O in? (1-3)")
            if board[int(row) - 1][int(column) - 1] != "-":
                print("That space is not available!")
            else:
                board[int(row) - 1][int(column) - 1] = "O"
                available = True

        for i in range(3):
            if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
                print(name2, "has won!")
                return name2, "has won!"
            if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
                print(name2, "has won!")
                return name2, "has won!"
        if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
            print(name2, "has won!")
            return name2, "has won!"
        if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
            print(name2, "has won!")
            return name2, "has won!"
        
        numOfTurns += 1
    return "Draw"

# ----------------------------------------------------------------------------------------------------------


def isnum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    tictactor()