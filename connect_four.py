########################################################################################################
# THE CODE BELOW IS PROVIDED TO YOU. MAKE SURE YOU UNDERSTAND IT!
########################################################################################################
import random

def make_diagonal(grid, line, column, direction):
    """
    This function takes a list of lists as input (the grid).
    It also takes:
    - a line number and a column number (defining the "starting point")
    - a direction = either upright or downleft (the direction of the diagonal)

    It returns a list made of the elements located in the relevant diagonal.
    """
    diagonal = []

    # Use a boolean to stop the loop if going outside of the grid
    in_grid = True
    while in_grid:
        # Add the element located at (line, column)
        diagonal.append(grid[line][column])

        # Move to the next "cell" depending on the direction
        if direction == "upright":
            # Going right
            column = column + 1
            # Going up = line index goes down
            line = line - 1
        elif direction == "downright":
            # Going right
            column = column + 1
            # Going down
            line = line + 1

        # Check that we are still inside the grid - if not, stop the loop
        if not 0 <= column <= len(grid[0]) - 1:
            in_grid = False
        if not 0 <= line <= len(grid) - 1:
            in_grid = False

    return diagonal


def check_connect4_win(grid):
    """
    This function takes a list of lists as argument (the grid).
    It assumes that the grid contains either:
    - two distinct symbols for player 1 and player 2
    - empty cells are represented with "", " ", or "-"

    It returns the winning symbol on the grid, or False if there is no winner.
    """

    EMPTY = ["", " ", "-"]

    # Horizontal lines
    for line in grid:
        result = check_connect4_line(line)
        if result:
            return result

    # Columns
    for col_number in range(len(grid[0])):
        column = make_column(grid, col_number)

        result = check_connect4_line(column)
        if result:
            return result

    # Diagonals
    for line_number, line in enumerate(grid):
        for column_number, element in enumerate(line):
            # If the element is an empty cell, continue to next loop
            if element in EMPTY:
                continue

            # Create the diagonals starting from that point
            diagonal1 = make_diagonal(grid, line_number, column_number, "upright")
            diagonal2 = make_diagonal(grid, line_number, column_number, "downright")

            # Check each of them
            for diagonal in (diagonal1, diagonal2):
                result = check_connect4_line(diagonal)
                if result:
                    return result

    return False


def make_grid(lines, columns, empty="-"):
    """Returns a list of lists with 'lines' lines and 'columns' columns, filled the the 'empty' character"""
    grid = []
    for line in range(lines):
        elements = []
        for column in range(columns):
            elements.append(empty)
        grid.append(elements)
    return grid 


########################################################################################################
# YOU MUST WRITE / CHANGE THE CODE BELOW!
########################################################################################################


def check_connect4_line(line):
    """
    This function takes a list of characters (or a string) as argument = a line of discs.
    If the line contains 4 identical elements, return this element (= winning disc).
    Otherwise, return False.
    """
    start = 0
    end = 0
    while end < len(line):
        end = start + 4
        windowCheck = line[start:end]
        disc = windowCheck[0]
        if disc != "-" and windowCheck.count(disc) == 4:
            return disc
        start += 1
    return False

def make_column(grid, column_number):
    """
    This function takes a list of lists as input (the grid).
    It returns a list made of the elements located in the column column_number.
    """
    column_list = []
    for i in range(len(grid)):
        column_list.append(grid[i][column_number])
    return column_list


def check_column(grid, column):
    """Returns True if the column index provided belongs to the grid"""
    return int(column) < len(grid[0])


def add_symbol_to_grid(grid, symbol, column):
    """
    Change the grid: play the symbol at the column index provided.
    Make sure the symbol "falls down" to the bottom of the column / the last empty cell.
    """
    for i in range(len(grid)):
        if grid[len(grid)-1 - i][int(column)] == "-":
            grid[len(grid)-1 - i][int(column)] = symbol
            break

def print_grid(grid):
    for line in grid:
        print(" ".join(line))

def main(lines, columns):
    """
    The main function:
    - creates an empty grid
    - sets up a loop to play the game
    """
    grid = make_grid(lines, columns)

    # 2-player game or against the computer?
    computer_plays = True
    incorrect_value = True
    while incorrect_value:
        value = input("Press 1 to play against the computer or 2 for a 2-player game.")
        if value in ("1", "2"):
            incorrect_value = False
            computer_plays = value == "1"
    
    # Main loop
    play = True
    current_player = "Player 1"
    current_symbol = "X"
    while play:
        # Input loop
        incorrect_value = True
        column = -1
        while incorrect_value:
            if computer_plays and current_player == "Player 2":
                column = random.randint(0,len(grid[0]) - 1)
                print("The computer has made its move! Placing it in column " + str(column + 1))
            else:
                column = input("Current turn: " + current_player + ". Enter column? ")
            if check_column(grid, column):
                incorrect_value = False
            else:
                print("You cannot play this column!")
        add_symbol_to_grid(grid, current_symbol, column)
        print_grid(grid)
        winner = check_connect4_win(grid)
        if winner:
            print(current_player + " has won! The new connect 4 champion!")
            play = False
        if current_player == "Player 1":
            current_player = "Player 2"
            current_symbol = "O"
        else:
            current_player = "Player 1"
            current_symbol = "X"

if __name__ == "__main__":
    main(6,7)