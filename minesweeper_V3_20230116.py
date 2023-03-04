
#**************************************************************************************************
#---START PSEUDOCODE
'''
- first construct the array - 2D-grid with mines in.
- indexes/positions on the edge of the grid have different numbers
- look to PDF for method to iterate through the array
- look to the internet for an algorithm to calculate numerical value of each index
- check out online PDF books for information on common games such as minesweeper
- the hint given is to be careful of going 'out of bounds' at the edge of the grid

- look-up the meaning of 'out of bounds'/python

- the essential problem is to count the number of #-symbols neighbouring/touching a grid-space
- the maximum number of # must be 8, the minimum must be 0, for the example grid, see Task pdf
- the edge of the grid-spaces have a lower potential value since they have fewer neighbours
- a hint was provided in the form of a grid, I have not understood the meaning of this hint ???

- it was suggested to use enumerate(), not a counter. Why ??? What is the point of teaching a hint and not...
    ...explaining the advantage of enumerate() over using a counter ???
- research how to read a grid to perform calculations on it, I assume a typed-out grid (not a formula) is provided...
    ...after re-reading, the grid provided is just to test the code. The code must work with any size of grid

- PLAN
-------
- Create a 2D grid which copies the grid provided in the task
- Create a function which is a 2D loop that goes through this grid by traversing each square that touches...
    ...the starting point, so 8-grid points, if a mine is detected then the value for the starting point...
    is increased by 1-point
- Out-of-bounds in this context, just means, counting grid-points which do not exist, a logic-error...
    ...I don't see how this could effect the result, if the grid does not exist then there is no mine...
    ...to detect there, but it might create an error message
- The method for traversing the grids is a nested 2D list, going down the rows, and along the columns
- I do not know how to implement this plan, I can research enumerate() but I do not see the advantage of using it...
    ...since no advantage was suggested in the pdf Task File
'''
#-- END PSEUDOCODE
#**************************************************************************************************

#   CLEAR EXPLAINATION AND LOGIC FOR THIS CODE CAME FROM : https://www.youtube.com/watch?v=ptMMa-SDSeE

def game_minesweeper(bombs, row_num, col_num) :
    '''this function takes in a 2D-list (grid of mines), & calculates number of mines adjacent to each grid-point.'''

    # grid_of_mines =[['-'] * col_num for _ in range(row_num)]      #<== HYP_DEV GAVE THIS LINE IN ITS pdf FOR THIS TASK 
    grid_of_mines =[[0 for i in range(col_num)] for j in range(row_num)]
    # print("This is the grid of the mines : ",grid_of_mines)       #<== A TEST BUTTON, IF YOU WISH TO SEE THE START-GRID?

    for bomb_location in bombs :                #<== THIS CALLS THE bombs ARGUMENT FROM def PARAMETER... 
        (bomb_row, bomb_col) = bomb_location    #<== ...TO SET BOMB-LOCATION HERE, IN  <for loop>, ONE AT A TIME
        grid_of_mines[bomb_row][bomb_col] = ('#')

        row_range = range(bomb_row - 1, bomb_row + 2)       #<== SEARCHES ADJACENT CELLS - ROWS
        col_range = range(bomb_col - 1, bomb_col + 2)       #<== SEARCHES ADJACENT CELLS - COLUMNS

        for i in row_range :
            for j in col_range :
                 if (0 <= i < row_num and 0 <= j < col_num and grid_of_mines[i][j] != ('#')) :   #<== EVALUATES: OUT-OF-BOUND/'MINE'
                    (grid_of_mines[i][j]) += 1      #<== PROGRESSES THE SEARCH 1-CELL AT A TIME
    return grid_of_mines

# BELOW, THIS CALLS THE FUNCTION & PRINTS THE FUNCTION return() VALUE
# + I HAVE ASSUMED THAT THIS TASK DOES NOT REQUIRE A USER input() TO TAKE DIFFERENT BOMB LOCATIONS, AT THIS TIME
#print(game_minesweeper(([[0,3],[0,4],[1,1],[2,2],[3,1],[3,2]]), 5, 5))  #<== BOMB CO-ORDINATES FROM TASK pdf


# work in progress, this a way to read in the mines input..............................
def input_mines() :
    while True :
        choice = input("""
Select an option below:-
1. Input the co-ordinates of mines?
2. Read the mines from a file?
3. To QUIT (type: 3)
____ Type in 1 or 2 _________ :   
""")
        if choice != 1 or 2 or 3 :
            print("Input not understood, please try again")
            continue
        elif choice == 1 :
            columns = input("Please type in the number of Columns in your grid : ")
            rows = input("Please type in the number of Rows in your grid : ")
            bombsites = []
            while True :
                bomb_positions = input("""
Please type in all the positions of the bombs :
Type in each co-ordinate inside square brackets and seperate each bracket by a comma :
""")     
        elif choice == 2 :
            filename = input("Please type in the name of your file : "
        else :
            return quit()
    
