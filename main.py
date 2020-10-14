import util
import engine
import ui
import inventory
import time
import os
import numpy

def main():
    PLAYER_ICON = '@'
    ENEMY = '&'
    PLAYER_START_X = 3
    PLAYER_START_Y = 3
    player = create_player(PLAYER_ICON,PLAYER_START_X, PLAYER_START_Y)
    board = engine.create_board(100, 30)
    util.clear_screen()
    is_running = True
    lvl = 0
    gold = 0
    inventory_1 = {"Healt potion": 1, "Knife": 1, "Gold coin": 2}
    engine.create_enemies(board, ENEMY, 5)
    while is_running and lvl < 4:
        x = player['x']
        y = player['y']
        engine.put_player_on_board(board, player)
        if gold < 1:
            engine.put_gold_on_board(board)
            gold = 1
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        if key == 'i':
            os.system("cls || clear")
            inventory.print_table(inventory_1)
            time.sleep(4.0)
        if key == "d":
            if board[y][x+1] == " " and board[y][x+1] != "#":
                board[y][x] = " "
                player['x'] = player ["x"] + 1
            if board[y][x+1] == "#":
                lvl = lvl +1
                main()
            if board[y][x+1] == "G":
                board[y][x+1] = " "
                inventory.add_gold(inventory_1)
        if key == "a":
            if board[y][x-1] == " ":
                board[y][x] = " "
                player['x'] = player ['x'] - 1
            if board[y][x-1] == "G":
                board[y][x-1] = " "
                inventory.add_gold(inventory_1)
        if key == "w":
            if board[y-1][x] == " ":
                board[y][x] = " "
                player['y'] = player ['y'] - 1
            if board[y-1][x] == "G":
                board[y-1][x] = " "
                inventory.add_gold(inventory_1)
        if key == "s":
            if board[y+1][x] == " ":
                board[y][x] = " "
                player ['y'] = player ['y'] + 1
            if board[y+1][x] == "G":
                board[y+1][x] = " "
                inventory.add_gold(inventory_1)
        engine.move_enemies(board, ENEMY)
        util.clear_screen()

def create_player(PLAYER_ICON,PLAYER_START_X, PLAYER_START_Y):
    player = {"avatar":PLAYER_ICON ,
    "x":PLAYER_START_X,
    "y": PLAYER_START_Y}
    return player


if __name__ == '__main__':
    main()
