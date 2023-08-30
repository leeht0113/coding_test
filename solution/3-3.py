# 숫자 카드 게임
# 배열에서 가장 작은 수를 찾는 기본 문법을 이용하여 각 행에서 가장 작은 수를 찾은 다음
# 그 수 중에서 가장 큰 수를 찾는 방식으로 문제를 해결
# min() 함수를 이용하는 답안 예시
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄 씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 적은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)