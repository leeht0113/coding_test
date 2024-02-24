from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 (그래프) 초기화
# 1번부터 v번 까지의 각 노드에 대한 인접한 노드 정보를 담을 수 있도록 하기 위해서 2차원 리스트를 만듦
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 정점 A에서 B로 이동이 가능하다는 것은 B에 대해서 들어오는 간선이 존재한다는 의미임
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 큐에 들어간 순서가 전체 위상 정렬이 수행한 결과와 동일하기 때문에 큐에서 원소를 꺼낼 때마다 결과 리스트에 담을 수 있도록 함
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        # 나가는 간선을 제거할 수 있도록 함
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end = ' ')

topology_sort()

# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
# 1 2 5 3 6 4 7