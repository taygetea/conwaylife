import curses
import time
import sys


def load(input="input.txt"):
    out = []
    for line in open(input, 'r'):
        out.append(list(line))

    return out


def cleanboard(board):
    width = max([len(line) for line in board])
    for line in board:
        for index, elem in enumerate(line):
            if elem not in ".O":
                line[index] = "."
        line.extend(['.' for i in range(width - len(line))])
    return board


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
    grid = cleanboard(load(sys.argv[1]))
    for l in grid:
        print ''.join(l)
    while True:
        grid = rebuild(grid)
        for index, elem in enumerate(grid):
            stdscr.addstr(index, 0, ''.join(elem))
        time.sleep(delay)
        stdscr.refresh()
if __name__ == "__main__":
    curses.wrapper(main)
