# 만들 수 없는 금액
import sys
input = sys.stdin.readline

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
for c in coin:
    if target < c:
        break
    target += c
print(target)