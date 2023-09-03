import sys
input = sys.stdin.readline
location = input()
row = int(location[1])
column = ord(location[0]) - ord('a') + 1
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

answer = 0
for move in moves:
    next_row = row + move[0]
    next_column = column + move[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        answer += 1

print(answer)

