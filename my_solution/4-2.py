import sys

input = sys.stdin.readline
n = int(input())
answer = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in f'{i}:{j}:{k}':
                answer += 1 

print(answer)