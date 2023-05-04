import re

# Define the regular expression pattern for valid input
#pattern = re.compile(r'^[pr][a-h][1-8]$')
pattern = re.compile(r'^(pawn|rook)\s[a-h][1-8]$')
# Initialize the list of black pieces
black_pieces = []

# Prompt the user to input the white piece
while True:
    white_piece = input('Enter the white piece (pawn or rook) and its coordinates (e.g. "pawn a2"): ')
    print(white_piece)
    if pattern.match(white_piece):
        print(f'White {white_piece} added successfully.')
        break
    else:
        print('Invalid input. Please try again.')

# Prompt the user to input the black pieces
while len(black_pieces) < 16:
    black_piece = input('Enter a black piece and its coordinates, or type "done" to finish: ')
    if black_piece == 'done':
        if not black_pieces:
            print('You must add at least one black piece.')
        else:
            print(f'{len(black_pieces)} black piece(s) added successfully.')
            break
    elif pattern.match(black_piece):
        if black_piece in black_pieces:
            print('You cannot add the same black piece twice.')
        else:
            black_pieces.append(black_piece)
            print(black_pieces)
            print(f'Black {black_piece} added successfully.')
    else:
        print('Invalid input. Please try again.')

# Define a function to determine if the white piece can take a black piece
def can_take(white, black):
    
    
    if white[0:4] == 'pawn':
        # Check if the pawn can take the black piece diagonally
        white_row, white_col = int(white[6]), ord(white[5]) - ord('a')
        print('white-',white_row, white_col)
        print(ord(white[5]),white[5])
        black_row, black_col = int(black[6]), ord(black[5]) - ord('a')
        print('black-',black_row, black_col)
        return (abs(white_row - black_row) == 1 and abs(white_col - black_col) == 1)
    
    elif white[0:4] == 'rook':
        # Check if the rook can take the black piece horizontally or vertically
        
        white_row, white_col = int(white[6]), ord(white[5]) - ord('a')
        black_row, black_col = int(black[6]), ord(black[5]) - ord('a')
        return (white_row == black_row or white_col == black_col)
    else:
        return False

# Find the black pieces that the white piece can take
can_take_list = [black for black in black_pieces if can_take(white_piece, black)]

# Print the result
if can_take_list:
    print(f'The white {white_piece} can take the following black piece(s): {", ".join(can_take_list)}.')
    
else:
    print(f'The white {white_piece} cannot take any black piece.')
    
