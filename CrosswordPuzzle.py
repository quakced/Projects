#I couldn't figure out how to open it so I did it the old fashion way
# and the only way I knew how to
board = [
    ['P', 'L', 'V', 'E', 'T', 'Q', 'D', 'S', 'C', 'D', 'F'],
    ['O', 'C', 'L', 'A', 'N', 'G', 'Y', 'P', 'U', 'Q', 'B'],
    ['P', 'W', 'O', 'E', 'K', 'E', 'K', 'C', 'Y', 'V', 'I'],
    ['T', 'B', 'J', 'M', 'H', 'Q', 'K', 'Q', 'Q', 'T', 'N'],
    ['A', 'W', 'Z', 'D', 'P', 'S', 'O', 'Z', 'T', 'X', 'A'],
    ['R', 'E', 'B', 'S', 'B', 'U', 'R', 'T', 'I', 'E', 'R'],
    ['T', 'X', 'C', 'P', 'I', 'K', 'T', 'E', 'S', 'R', 'Y'],
    ['S', 'S', 'E', 'T', 'O', 'E', 'V', 'E', 'W', 'P', 'Y'],
    ['V', 'P', 'N', 'B', 'A', 'N', 'D', 'E', 'R', 'O', 'S'],
    ['T', 'P', 'I', 'L', 'I', 'W', 'P', 'M', 'F', 'U', 'P'],
    ['L', 'A', 'M', 'I', 'C', 'E', 'D', 'A', 'X', 'E', 'H']
]
#printing out the board so it is nice and neat
def print_board():
    for row in board:
        print(' '.join(f"{ch}" for ch in row))
    print()
# variables for the whole code to use
words = ["Binary", "Computer", "Hexadecimal", "Bander", "Powershell", "Apps", "Web Sites", "Duck", "VSC", "Poptarts"]
rows = len(board)
cols = len(board[0])

def searchHorizontally(word):
    #intital variables
    positions = []
    word = word.upper()
    #now checking each row in the row_string for the board contents
    for i in range(rows):
        row_string = ''.join(board[i])
        index = row_string.find(word)
        #while if it doesn't go outside the boundries to find it it will check for the word and append it to the bottom of the terminal
        while index != -1:
            positions.append(((i, index), (i, index + len(word) - 1)))
            index = row_string.find(word, index + 1)
        #checking for the word going right to left instead of left to right
        reversed_word = word[::-1]
        index = row_string.find(reversed_word)
        #while it doesn't go outside the board it will check the opposite of of what the normal horizontal checks for in a different order.
        while index != -1:
            positions.append(((i, index + len(word) - 1), (i, index)))
            index = row_string.find(reversed_word, index + 1)
    return positions
# Search Vertically
def searchVertically(word):
    #intial variables
    positions = []
    word = word.upper()
    #taking the range of the cols and searching from col to the next row
    for col in range(cols):
        col_str = ''.join(board[row][col] for row in range(rows))
        index = col_str.find(word)
        #while it doesn't pass the boundries of the board it will check for the col and the word with each coloumn
        while index != -1:
            #appending the positions to of the index col_str 
            positions.append(((index, col), (index + len(word) - 1, col)))
            index = col_str.find(word, index + 1)
        #checking if the word goes the other way then just up and down
        reversed_word = word[::-1]
        index = col_str.find(reversed_word)
        while index != -1:
            #filping the code to do the opposite than just checking for up and down it is checking down to up from the words bottom to the top
            positions.append(((index + len(word) - 1, col), (index, col)))
            index = col_str.find(reversed_word, index + 1)
    return positions
#Diagonal search
def searchDiagonally(word):
    #inital variables
    positions = []
    word = word.upper()
    word_len = len(word)

    # Diagonals: Top left to bottom right
    for row in range(rows):
        for col in range(cols):
            #trying to stay inside the board boundries
            if row + word_len <= rows and col + word_len <= cols:
                # joining both the rows and the cols together to check both as it goes down
                diagonal = ''.join(board[row + i][col + i] for i in range(word_len))
                if diagonal == word:
                # Once it finds that it is diagonal it will take the row and column it found it in and append the positions
                # As well as it will check if the position is backwords and append it
                    positions.append(((row, col), (row + word_len - 1, col + word_len - 1)))
                elif diagonal[::-1] == word:
                    positions.append(((row + word_len - 1, col + word_len - 1), (row, col)))

    # Diagonals: Bottom left to top right
    for row in range(word_len - 1, rows):
        for col in range(cols - word_len + 1):
            # checking for the diagonal word the other way around from bottom left to top right so we will need to reverse which way we are going
            diagonal = ''.join(board[row - i][col + i] for i in range(word_len))
            #once it finds the word it will append the positon from the row and col
            if diagonal == word:
                positions.append(((row, col), (row - word_len + 1, col + word_len - 1)))
            # checking if it goes in reverse order from right to left
            elif diagonal[::-1] == word:
                positions.append(((row - word_len + 1, col + word_len - 1), (row, col)))
    return positions
#Search for word using all the code togehter
def searchWord(word):
    # returning all the code together so we can get the positions of where the word is from all three
    return (
    searchHorizontally(word) + searchVertically(word) + searchDiagonally(word)
    )
print_board()
# Ask the user for a word and search it
while True:
    #asking input from the user to check what word the user wants from the words list
    word = input(f"What word would you like to find from these words?\n{words}\n").strip()
    # checking if the user had capitalized the letters since the Word Search is captilized
    if word.capitalize() not in words:
        print("That word is not in the list. Please choose from the provided words.")
        continue
    # Once it finds the position of the word by searching through each checker all together it will display the start and end
    # from the positions that the Checkers appended
    found_positions = searchWord(word)
    if found_positions:
        print_board()
        for start, end in found_positions:
            print(f"Found '{word}' from {start} to {end}")
    #if it didn't find it it will tell them it isn't there
    else:
        print(f"'{word}' was not found in the grid.")
