import sys
input = sys.stdin.readline
n = int(input())
score = []
for _ in range(n):
    n, m = input().split()
    score.append((n, int(m)))
score.sort(key=lambda x: x[1])
for s in score:
    print(s[0], end=' ')