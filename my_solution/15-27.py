import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, x = map(int, input().split())
array = list(map(int, input().split()))

start = bisect_left(array, x)
end = bisect_right(array, x)

answer = end - start
if answer != 0:
    print(answer)
else:
    print(-1)
