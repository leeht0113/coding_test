import sys
input = sys.stdin.readline
n = int(input())
answer = []
for _ in range(n):
    answer.append(int(input()))
answer.sort(reverse=True)
for a in answer:
    print(a, end = ' ')