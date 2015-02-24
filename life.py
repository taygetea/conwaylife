def init(input, *border):
    f = open(input, 'r')
    firstline = f.readline()
    if firstline.startswith("!Name: "):
        name = firstline[7:]
        print "name: " + name

    lines = f.readlines()
    array = []

    longest = sorted([len(line)-1 for line in lines])
    longest = longest[-1]
    for line in lines:
        line = [l for l in line if l in ".O"]
        if len(line) < longest:
            line.extend('.'*(longest - len(line)))
        if line[0] != '!':
            array.append(line)

    return array


def neighbors(x, y, board):
    neighbors = 0
    try:
        if board[x-1][y-1] == 'O':
            neighbors += 1
    except IndexError:
        pass
    try:
        if board[x-1][y] == 'O':
            neighbors += 1
    except IndexError:
        pass
    try:
        if board[x-1][y+1] == 'O':
            neighbors += 1
    except IndexError:
        pass
    try:
        if board[x][y-1] == 'O':
            neighbors += 1
    except IndexError:
        pass
    try:
        if board[x][y+1] == 'O':
            neighbors += 1
    except IndexError:
        pass
    try:
        if board[x+1][y-1] == 'O':
            neighbors += 1
    except IndexError:
        pass
    try:
        if board[x+1][y] == 'O':
            neighbors += 1
    except IndexError:
        pass
    try:
        if board[x+1][y+1] == 'O':
            neighbors += 1
    except IndexError:
        pass
    return neighbors


def update(board):
    output = []

    for i, x in enumerate(board):
        output.append([])
        for j, y in enumerate(x):
            output.append([])
            neighbornum = neighbors(i, j, board)
            if board[i][j] == '.':
                if neighbornum == 3:
                    #print "the space " + str(i) + " " + str(j) + " came alive"
                    output[i].append('O')
                else:
                    output[i].append('.')
            elif board[i][j] == 'O':
                if neighbornum == 3 or neighbornum == 2:
                    #print "the space " + str(i) + " " + str(j) + " survived"
                    output[i].append('O')
                elif neighbornum < 2 or neighbornum > 3:
                    #print "the space " + str(i) + " " + str(j) + " died"
                    output[i].append('.')
    return output


array = init("input.txt")
cycles = 1
for i in range(cycles):
    array = update(array)

array = [''.join(x) for x in array if x != []]
f = open('output.txt', 'w')
for item in array:
    f.write("%s\n" % item)
