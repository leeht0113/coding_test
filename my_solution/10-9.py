from collections import deque
from copy import deepcopy

n = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)

for i in range(1, n + 1):
    lesson = list(map(int, input().split()))
    time[i] += lesson[0]
    for l in lesson[1:]:
        if l != -1:
            graph[l].append(i)
            indegree[i] += 1
    
# print(time)
# print(graph)
# print(indegree)

def topology_sort():
    q = deque()
    result = deepcopy(time)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            if indegree[i] == 0:
                q.append(i)

    for r in result[1:]:
        print(r)

topology_sort()

