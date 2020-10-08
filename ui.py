
def display_board(board):

    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for count, row in enumerate(board, 1):
        print(''.join([str(elem) for elem in row]))

    pass
