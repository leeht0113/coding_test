import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs 함수
def dfs(x, y):
    # 범위 벗어나면 false 반환
    if x <= -1 or x >=n or y <= -1 or y >= n:
        return False
    # 방문 여부 확인
    if graph[x][y] == 0:
        # 방문하지 않았으면 방문처리
        graph[x][y] = 1
        # 상하좌우로 dfs 탐색
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x. y+1)
        # dfs 탐색이 이뤄지면 true 반환
        return True
    # 이미 방문된 노드여서 dfs 탐색이 이뤄지지 않으면 False 반환
    return False

result = 0
for i in range(n):
    for j in range(m):
        # 해당 위치 dfs 수행, 수행되면 아이스크림 개수 추가
        if dfs(i, j) == True:
            result += 1

print(result)