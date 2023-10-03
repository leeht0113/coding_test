import sys
input = sys.stdin.readline
tc = int(input())
answer = []
for t in range(tc):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for _ in range(n):
        dp.append(array[index:index+m])
        index += m
    # 첫번째 열은 그대로 사용함
    for j in range(1, m):
        for i in range(n):
            # 첫번째 행인 경우, 왼쪽 위는 0임 (고려 안함)
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 마지막 행인 경우, 왼쪽 아래는 0임 (고려 안함)
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    answer.append(result)

for i in range(tc):
    print(answer[i])
            
