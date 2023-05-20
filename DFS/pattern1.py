# https://atcoder.jp/contests/atc001/tasks/dfs_a
from collections import deque

def dfs(s1, s2):
    stack = deque([[s1, s2]])
    while stack:
        x, y = stack.pop()
        if maze[x][y] == "g":
            return True
        else:
            maze[x][y] = "#"
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= x+dx < H and 0 <= y+dy < W and maze[x+dx][y+dy] != "#":
                stack.append([x+dx, y+dy])
    return False

'''    if x < 0 or x >= H or y < 0 or y >= W:
        return False
    if maze[x][y] == "#":
        return False
    if maze[x][y] == "g":
        return True
    maze[x][y] = "#"
    if dfs(x+1, y):
        return True
    if dfs(x-1, y):
        return True
    if dfs(x, y+1):
        return True
    if dfs(x, y-1):
        return True
    return False 
'''

if __name__ == "__main__":
    H, W = map(int, input().split())
    maze = []
    start = []
    for i in range(H):
        maze.append(list(input()))
        if "s" in maze[-1]:
            start = [i, maze[-1].index("s")]
    if dfs(start[0], start[1]):
        print("Yes")
    else:
        print("No")