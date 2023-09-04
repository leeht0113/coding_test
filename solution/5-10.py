# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    # 결과적으로 True 값 반환
    # 현재 위치에 대해서 처음 dfs가 수행된 것이기 때문에 그 위치에 대해서 result값을 증가시킴
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] == 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        # return 값을 사용하지 않기 때문에 연결된 모든 노드에 대해서 방문처리를 수행하기 위한 목적으로 수행됨
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        # 한번 dfs가 수행되면 해당 노드와 연결된 모든 노드들도 방문 처리할 수 있도록 함
        # 시작점 노드가 방문처리가 되고 처음 방문하는 것이라면 result값을 증가시킴
        if dfs(i, j) == True:
            result += 1

print(result)