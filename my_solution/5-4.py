from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 상, 하, 좌, 우
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(len(move)):
            nx = x + move[i][0]
            ny = y + move[i][1]
            # 범위 벗어나면 건너 띔
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물인 경우 bfs 수행 안함
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 그래프의 맨 마지막 칸 반환
    return graph[-1][-1]
    
print(bfs(0, 0))
