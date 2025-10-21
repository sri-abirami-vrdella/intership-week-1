def solve_maze(maze, x, y, path):
    n = len(maze)
    m = len(maze[0])
    if x == n - 1 and y == m - 1 and maze[x][y] == 1:
        path.append((x, y))
        return True
    if 0 <= x < n and 0 <= y < m and maze[x][y] == 1:
        path.append((x, y))
        maze[x][y] = -1
        if (solve_maze(maze, x + 1, y, path) or
            solve_maze(maze, x, y + 1, path) or
            solve_maze(maze, x - 1, y, path) or
            solve_maze(maze, x, y - 1, path)):
            return True
        path.pop()
        maze[x][y] = 1
    return False


def print_maze_solution(maze):
    path = []
    if solve_maze(maze, 0, 0, path):
        print("Path Found:")
        for step in path:
            print(step, end=" -> ")
        print("End")
    else:
        print("No path found.")


maze = [
    [1, 0, 1, 1],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]

print("\nMAZE SOLVER RESULT")
print_maze_solution(maze)