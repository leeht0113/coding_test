import sys
input = sys.stdin.readline
n = int(input())
plan = input().split()
# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
plan_type = ['L','R','U','D']
# 현재 위치
x, y = 1, 1
for p in plan:
    move = plan_type.index(p)
    nx = x + dx[move]
    ny = y + dy[move]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny
print(x, y)
