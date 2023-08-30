# 큰 수의 법칙
# 연속으로 더할 수 있는 횟수는 최대 k번이므로 가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산을 반복
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1]
second = data[n - 2]

# 단순하게 푸는 답안 예시
# result = 0

# while True:
#     for i in range(k): # 가장 큰 수를 K번 더하기
#         if m == 0: # m이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1
#     if m == 0: # m이 0이라면 반복문 탈출
#         break
#     result += second
#     m -= 1

# print(result)

# M을 (K+1)로 나눈 몫이 수열이 반복되는 횟수가 되고 다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 됨
# M이 (K+1)로 나누어 떨어지지 않은 경우, M을 (K+1)로 나눈 나머지만큼 가장 큰 수가 추가로 더해짐
# 가장 큰 수가 더해지는 횟수 계산
count = int(m  / (k+1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)