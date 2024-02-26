def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, m = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

answer = []

for _ in range(m):
    calc, a, b = map(int, input().split())
    if calc == 0:
        union_parent(parent, a, b)
    elif calc == 1:
        if (find_parent(parent, a) == find_parent(parent, b)):
           answer.append('YES') 
        else:
            answer.append('NO')

for a in answer:
    print(a)