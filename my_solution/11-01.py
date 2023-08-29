# 모험가 길드
import sys

input = sys.stdin.readline
a = int(input())
b = list(map(int, input().split()))
b.sort()
group = 0 # 총 그룹 수
count = 0 # 현재 그룹에 포함된 모함가의 수
for i in b: # i -> 현재 확인하고 있는 공포도
    count += 1
    if count >= i:
        group += 1 # 그룹 결성
        count = 0 # 그룹에 포함된 모험가의 수 초기화

print(group)