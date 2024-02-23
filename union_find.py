# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    # 현재 부모가 자기 자신이 아니라면 루트 노드가 아니라는 의미임
    if parent[x] != x:
        # 루트 노드를 찾기 위해서 자신의 부모에 대한 노드 번호를 넣어서 다시 한번 find_parent 함수를 호출
        # find_parent 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 그 반환 값으로 갱신할 수 있도록 만듦
        # find_parent 함수를 호출할 때 사용했던 노드에 대한 부모의 값이 루트와 동일하도록 경로가 압축되는 것
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    # a와 b의 루트 번호를 찾음
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 루트 번호가 더 큰 쪽이 작은 쪽을 부모로 설정할 수 있도록 함
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화
print(parent)
# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
# 간선의 개수에 따라서 두 원소를 연결하고 있는 각각의 연결 여부를 확인하면 union 연산을 수행
for i in range(e):
    a, b = map(int, input().split())
    # union 연산을 수행할 때는 원소 a와 원소 b가 서로 연결되어 있다는 의미로 union_parent 함수를 호출할 수 있음
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end = '')
for i in range(1, v + 1):
    print(find_parent(parent, i), end = ' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end = '')
for i in range(1, v + 1):
    print(parent[i], end=' ')

# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
# 각 원소가 속한 집합: 1 1 1 1 5 5 
# 부모 테이블: 1 1 1 1 5 5 