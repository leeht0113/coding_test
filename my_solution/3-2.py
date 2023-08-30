# 큰 수의 법칙
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
answer = 0
count = 0
while count <= m:
    for j in range(k):
        if count == m:
            break
        answer += data[0]
        count += 1
    if count == m:
        break
    answer += data[1]
    count += 1
print(answer)
