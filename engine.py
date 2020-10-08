def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''

    game_board = []
    border_lines = 2
    border_characters = 2
 
    first_row = []
    first_row.append(" ")
    for _ in range(width):
        first_row.append("_")
    game_board.append(first_row)
 
    for _ in range(height-border_lines):
        middle_row = []
        middle_row.append("| ")
        for _ in range(width-border_characters):
            middle_row.append(" ")
        middle_row.append(" |")
        game_board.append(middle_row)
 
    last_row = []
    last_row.append("|")
    for _ in range(width):
        last_row.append("_")
    last_row.append("|")
    game_board.append(last_row)
 
    return game_board



def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
 
    x = player['x']
    y = player['y']
    board[y][x] = player['avatar']

