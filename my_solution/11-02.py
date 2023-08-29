import sys
input = sys.stdin.readline
n = input().rstrip()

answer = int(n[0])
for i in range(1, len(n)):
    if int(n[i]) <= 1 or answer <= 1:
        answer += int(n[i])
    elif int(n[i]) > 1:
        answer *= int(n[i])
print(answer)