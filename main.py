import curses
import random

WIDTH, HEIGHT, START_POSSITIONS = 10, 15, (0, 0)
EMPTY_CELL, FILLED_CELL = " . ", " # "
game_running_state = True
target_position  = (
    random.randint(0, HEIGHT -1),
    random.randint(0, WIDTH -1)
)
obsticle_possitions = [(4,4),(4,5),(5,4),(5,5)]

def board_creation():
    temp = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    temp[target_position [0]][target_position [1]] = FILLED_CELL

    for item in obsticle_possitions:
        temp[item[0]][item[1]] = FILLED_CELL
    return temp

board = board_creation()

def update_game_running_state():
    global game_running_state
    game_running_state = False

def draw_board():
    output = ""
    for i in range(HEIGHT):
        output += "|"
        for y in range(WIDTH):
            output += FILLED_CELL if board[i][y] else EMPTY_CELL
        output += "|"
        output += "\n"
    return output

def draw_updated_board(stdscr, y_axis, x_axis):
    global board, game_running_state
    board = board_creation()
    stdscr.clear()
    for item in obsticle_possitions:
        if (y_axis, x_axis) == item:
            stdscr.clear()
            print("GAME OVER!")
            game_running_state = False
    if board[y_axis][x_axis] != FILLED_CELL:
        board[y_axis][x_axis] = FILLED_CELL
    if (y_axis, x_axis) == target_position:
        stdscr.clear()
        print("You did it!")
        game_running_state = False
    stdscr.addstr(draw_board())

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)
    stdscr.keypad(True)
    
    y_axis, x_axis = START_POSSITIONS
    board[y_axis][x_axis] = FILLED_CELL
    stdscr.addstr(draw_board())

    while game_running_state:
        key = stdscr.getch()
        if key == curses.KEY_UP or key == ord('w'):
            if y_axis in range(1, HEIGHT):
                y_axis -= 1
                draw_updated_board(stdscr, y_axis, x_axis)
        elif key == curses.KEY_DOWN or key == ord('s'):
            if y_axis in range(HEIGHT - 1):
                y_axis += 1
                draw_updated_board(stdscr, y_axis, x_axis)
        elif key == curses.KEY_LEFT or key == ord('a'):
            if x_axis in range(1, WIDTH):
                x_axis -= 1
                draw_updated_board(stdscr, y_axis, x_axis)
        elif key == curses.KEY_RIGHT or key == ord('d'):
            if x_axis in range(WIDTH - 1):
                x_axis += 1
                draw_updated_board(stdscr, y_axis, x_axis)
        elif key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
