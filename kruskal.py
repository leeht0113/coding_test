# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        # 경로 압축 기법 사용
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속합 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블을 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    # 파이썬에서는 기본적으로 튜플에 원소가 여러개일 때는 첫번째 원소를 기준으로해서 정렬을 수행함
    edges.append((cost, a, b))

# 간선을 비용순으로 설정
edges.sort()

# 비용이 낮은 순서대로 간선을 하니씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    # 해당 간선에 포함되어 있는 두 원소 a와 b에 대해서 이미 같은 집합에 포함되어 있지 않다면 합치기 연산을 수행하고 해당 간선을 최소 신장 트리에 포함시킬 수 있도록 함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        # 합치기 연산을 수행할 때마다 해당 간선의 비용 값을 result 변수에 더해줄 수 있도록 하여 최종적으로 result값을 출력하도록 만듦
        result += cost
# 최소 신장 트리의 포함되어 있는 모든 간선의 비용의 합이 출력됨
print(result)