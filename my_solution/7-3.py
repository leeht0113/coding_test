import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tteok = list(map(int, input().split()))
end = max(tteok)
start = 0
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for t in tteok:
        if (t - mid) > 0:
            total += (t - mid)
    if total >= m: # 적어도 m만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값
        answer = mid
        start = mid + 1
    elif total < m:
        end = mid - 1
print(answer) 
