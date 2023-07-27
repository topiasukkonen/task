from collections import deque
import unittest

def readFile(file):
    """
    Function to read a maze from a file.

    Args:
        file (str): Filename of the maze file.

    Returns:
        list: List of lists representing the maze.
    """
    with open(file, 'r') as f:
        maze = [list(line.strip()) for line in f]
    return maze


def writeMaze(file, maze):
    """
    Function to write the maze to a file.

    Args:
        file (str): Filename of the output file.
        maze (list): List of lists representing the maze.
    """
    with open(file, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')


def solveMaze(maze_file, max_moves):
    """
    Function to solve the maze.

    Args:
        maze_file (str): Filename of the maze file.
        max_moves (int): Maximum allowed moves.

    Returns:
        bool: True if a path was found, False otherwise.
    """
    # Read the maze from the file
    maze = readFile(maze_file)
    rows = len(maze)
    cols = len(maze[0])

    # Find the starting point
    start = [(r, c) for r in range(rows) for c in range(cols) if maze[r][c] == '^'][0]
    
    # Initialize the queue with the starting point
    queue = deque([(start[0], start[1], None, 0)])  # (row, col, parent, moves)
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # Possible movements (up, left, down, right)
    visited = set()  # Set to store visited nodes
    came_from = {}  # Dictionary to keep track of path

    while queue:
        r, c, parent, moves = queue.popleft()  
        
        # Skip if the node was already visited or if we've made too many moves
        if (r, c) in visited or moves > max_moves: 
            continue

        visited.add((r, c))
        came_from[(r, c)] = parent

        # Check if we've reached the exit
        if maze[r][c] == 'E':
            path = []
            while (r, c) != start:
                path.append((r, c))
                r, c = came_from[(r, c)]
            path.append(start)  # Add the starting point to the path
            for r, c in path:  # Mark the path on the maze
                maze[r][c] = '*'
            writeMaze('solvedMaze.txt', maze)  # Write the solved maze to a file
            return True

        # Add adjacent nodes to the queue
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if (0 <= new_r < rows and 0 <= new_c < cols and
                    maze[new_r][new_c] not in {'#', '*'}):
                queue.append((new_r, new_c, (r, c), moves + 1))

    writeMaze('unsolvedMaze.txt', maze)  # Write the unsolved maze to a file
    return False


class TestMazeSolver(unittest.TestCase):
    def test_solveMaze(self):
        self.assertEqual(solveMaze('maze-task-first_(1).txt', 20), False)
        self.assertEqual(solveMaze('maze-task-first_(1).txt', 150), True)
        self.assertEqual(solveMaze('maze-task-first_(1).txt', 200), True)

if __name__ == '__main__':
    print(solveMaze('maze-task-first_(1).txt', 20))
    print(solveMaze('maze-task-first_(1).txt', 150)) 
    print(solveMaze('maze-task-first_(1).txt', 200)) 
    unittest.main()