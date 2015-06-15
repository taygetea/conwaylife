import curses
import time


def load(input="input.txt"):
    out = []
    for line in open(input, 'r'):
        out.append(list(line))

    return out


def cleanboard(grid):
    width = sorted([len(line) for line in grid])[-1]
    for line in grid:
        if len(line) < width:
            line.extend('.'*(width - len(line)))
def rebuild(grid):
    boardOut = []
    ylen = len(grid)
    xlen = len(grid[0])
    for i, item in enumerate(grid):
        lineOut = []
        for j, cell in enumerate(grid[i]):
            neighbors = (grid[i][(j-1) % xlen] +
                         grid[i][(j+1) % xlen] +
                         grid[(i-1) % ylen][j] +
                         grid[(i+1) % ylen][j] +
                         grid[(i-1) % ylen][(j-1) % xlen] +
                         grid[(i-1) % ylen][(j+1) % xlen] +
                         grid[(i+1) % ylen][(j-1) % xlen] +
                         grid[(i+1) % ylen][(j+1) % xlen])
            liveneighbors = len(filter(lambda x: x == 'O', neighbors))
            if cell == 'O':
                if liveneighbors < 2:
                    lineOut.append(".")
                elif liveneighbors > 3:
                    lineOut.append(".")
                else:
                    lineOut.append("O")
            else:
                if liveneighbors == 3:
                    lineOut.append("O")
                else:
                    lineOut.append(".")
        boardOut.append(lineOut)
    return boardOut


def main(stdscr, delay=0.033):
    grid = load()
    while True:
        grid = rebuild(grid)
        for index, elem in enumerate(grid):
            stdscr.addstr(index, 0, ''.join(elem))
        time.sleep(delay)
        stdscr.refresh()
curses.wrapper(main)
