from collections import deque

def read_maze_from_file(file):
    with open(file, 'r') as f:
        maze = [list(line.strip()) for line in f]
    return maze

def write_maze_to_file(file, maze):
    with open(file, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')