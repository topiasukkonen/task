from collections import deque

def readFile(file):
    with open(file, 'r') as f:
        maze = [list(line.strip()) for line in f]
    return maze

def writeMaze(file, maze):
    with open(file, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')
            
def solveMaze(maze_file, max_moves):
    maze = readFile(maze_file)
    rows = len(maze)
    cols = len(maze[0])

    start = [(r, c) for r in range(rows) for c in range(cols) if maze[r][c] == '^'][0]
    queue = deque([(start[0], start[1], None, 0)])
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)] 
    visited = set()
    came_from = {}

    while queue:
        r, c, parent, moves = queue.popleft() 
        if (r, c) in visited or moves > max_moves: 
            continue
        visited.add((r, c))
        came_from[(r, c)] = parent

        if maze[r][c] == 'E':
            path = []
            while (r, c) != start:
                path.append((r, c))
                r, c = came_from[(r, c)]
            path.append(start) 
            for r, c in path:
                maze[r][c] = '*'
            writeMaze('solvedMaze.txt', maze)
            return True

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if (0 <= new_r < rows and 0 <= new_c < cols and
                    maze[new_r][new_c] not in {'#', '*'}):
                queue.append((new_r, new_c, (r, c), moves + 1))

    writeMaze('unsolvedMaze.txt', maze)
    return False


print(solveMaze('maze-task-second_(1).txt', 20))
print(solveMaze('maze-task-second_(1).txt', 150)) 
print(solveMaze('maze-task-second_(1).txt', 200)) 
