import sys
input = sys.stdin.readline
n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input().rstrip()))
dp = [float('inf')] * (m + 1)
dp[0] = 0

for i in money:
    for j in range(i, m + 1):
        dp[j] = min(dp[j], dp[j-i] + 1)
        
answer = dp[m]
if answer != float('inf'):
    print(answer)
else:
    print(-1)



