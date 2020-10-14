HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def display_board(board):

    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    print(FAIL)
    for count, row in enumerate(board, 1):
        print(' '.join([str(elem) for elem in row]))
    print (ENDC)
