# 숫자 카드 게임
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

card_game = []
for _ in range(n):
    card_game.append(list(map(int, input().split())))

numbers = []
for c in card_game:
    numbers.append(min(c))

print(max(numbers))