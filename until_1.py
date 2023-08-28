import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))

answer = 0

while n > 1:
    if n % k == 0:
        n /= k
        answer += 1
    else:
        n -= 1
    if n == 1:
        break

print(answer)