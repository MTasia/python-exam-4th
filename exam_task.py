from collections import deque


def possible_neighbours(i, j, maze, visited):
    neighbours = []
    if i + 1 < len(maze):
        if maze[i + 1][j] == 0 and not visited[i + 1][j]:
            neighbours.append((i + 1, j))
    if j + 1 < len(maze):
        if maze[i][j + 1] == 0 and not visited[i][j + 1]:
            neighbours.append((i, j + 1))
    if i - 1 > -1:
        if maze[i - 1][j] == 0 and not visited[i - 1][j]:
            neighbours.append((i - 1, j))
    if j - 1 > - 1:
        if maze[i][j - 1] == 0 and not visited[i][j - 1]:
            neighbours.append((i, j - 1))
    return neighbours


def count_steps(maze, start, end, n):
    j = start[0]
    i = start[1]
    visited = [[False for j in range(n)] for i in range(n)]
    # dist = [[0 for j in range(len(maze))] for i in range(len(maze))]
    queue = deque()
    queue.append((i, j))
    mass1 = []
    while queue:
        curr = queue.popleft()
        mass1.append(curr)
        print("curr", curr)
        curr_x, curr_y = curr[0], curr[1]
        visited[curr_x][curr_y] = True
        neighbours = possible_neighbours(curr_x, curr_y, maze, visited)
        print(neighbours)
        print()
        for nb in neighbours:
            queue.append(nb)
            if nb == end:
                return 0
    print("for end")
    j = end[0]
    i = end[1]
    # visited = [[False for j in range(n)] for i in range(n)]
    # dist = [[0 for j in range(len(maze))] for i in range(len(maze))]
    queue = deque()
    queue.append((i, j))
    mass2 = []
    while queue:
        curr = queue.popleft()
        mass2.append(curr)
        print("curr", curr)
        curr_x, curr_y = curr[0], curr[1]
        visited[curr_x][curr_y] = True
        neighbours = possible_neighbours(curr_x, curr_y, maze, visited)
        print(neighbours)
        print()
        for nb in neighbours:
            queue.append(nb)
            if nb == end:
                return 0

    for i in visited:
        print(*i)
    print(mass1)
    print(mass2)

    # Search min path
    min_path = (mass1[0][0] - mass2[0][0]) ** 2 + (mass1[0][1] - mass2[0][1]) ** 2
    for pair1 in mass1:
        xs, ys = pair1[0], pair1[1]
        for pair2 in mass2:
            xt, yt = pair2[0], pair2[1]
            min_path = min(min_path, (xs - xt) ** 2 + (ys - yt) ** 2)
    return min_path


def main():
    n = 5
    x1, y1 = 1, 1
    x2, y2 = 5, 5
    mass = [[0, 0, 0, 0, 1], [1, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0]]

    start = (x1 - 1, y1 - 1)
    end = (x2 - 1, y2 - 1)
    print(count_steps(mass, start, end, n))


if __name__ == '__main__':
    main()
