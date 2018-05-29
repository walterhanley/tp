dashes = ' - - - - '
plus = '+'
pipes = '|         |         |\n'
line = ((plus + dashes) * 2)


def grid():
    print(line + plus)
    print(pipes * 4, end='')
    print(line + plus)
    print(pipes * 4, end='')
    print(line + plus)


def grid_4():
    print(line * 2 + plus)


grid_4()
