import curses
import random

WIDTH, HEIGHT = 10, 15
rand_possition_goal = (random.randint(1, HEIGHT), random.randint(1, WIDTH))

def set_up_board():
    temp = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
    ## Define goal possitions
    temp[rand_possition_goal[0]][rand_possition_goal[1]] = " # "
    return temp

## Define Board
board = set_up_board()
## Running script state
running_state = True

## Draw a board
def draw():
    output = ""
    for i in range(HEIGHT):
        output += "|"
        for y in range(WIDTH):
            output += " # " if board[i][y] else " . "
        output += "|"
        output += "\n"
    return output

## Update board while pressing arrow keys
def draw_update(stdscr, y_axis, x_axis):
    global board
    board = set_up_board()
    stdscr.clear()
    if y_axis < 0:
        y_axis = 0
    if y_axis > HEIGHT - 1:
        y_axis = HEIGHT -1
    if x_axis < 0:
        x_axis = 0
    if x_axis > WIDTH - 1:
        x_axis = WIDTH - 1
    if board[y_axis][x_axis] != " # ":
        board[y_axis][x_axis] = " # "
    if y_axis == rand_possition_goal[0] and x_axis == rand_possition_goal[1]:
        stdscr.clear()
        print("GAME OVER!")
        global running_state
        running_state = False
    stdscr.addstr(draw())

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)
    stdscr.keypad(True)
    
    board[0][0] = " # "
    stdscr.addstr(draw())
    y_axis, x_axis = 0,0

    while running_state:
        key = stdscr.getch()
        if key == curses.KEY_UP or key == ord('w'):
            y_axis -= 1
            draw_update(stdscr, y_axis, x_axis)
        elif key == curses.KEY_DOWN or key == ord('s'):
            y_axis += 1
            draw_update(stdscr, y_axis, x_axis)
        elif key == curses.KEY_LEFT or key == ord('a'):
            x_axis -= 1
            draw_update(stdscr, y_axis, x_axis)
        elif key == curses.KEY_RIGHT or key == ord('d'):
            x_axis += 1
            draw_update(stdscr, y_axis, x_axis)
        elif key == ord('q'):
            break

curses.wrapper(main)