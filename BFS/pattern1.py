# https://atcoder.jp/contests/atc002/tasks/abc007_3
from collections import deque

def bfs(s1, s2, g1, g2):
    queue = deque([[s1, s2, 0]])
    while queue:
        x, y, cost = queue.popleft()
        if x == g1 and y == g2:
            return cost
        elif maze[x][y] == "#":
            continue
        else:
            maze[x][y] = "#"
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= x+dx < H and 0 <= y+dy < W and maze[x+dx][y+dy] != "#":
                queue.append([x+dx, y+dy, cost+1])

if __name__ == "__main__":
    H, W = map(int, input().split())
    s1, s2 = map(int, input().split())
    g1, g2 = map(int, input().split())
    maze = []
    for i in range(H):
        maze.append(list(input()))
    print(bfs(s1-1, s2-1, g1-1, g2-1))