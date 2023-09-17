import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
search_array = list(map(int, map(int, input().split())))

# 반복문
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = start - 1
        else:
            start = mid + 1
    return 'no'

# 재귀함수
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return 'yes'
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)
    
for i in range(m):
    if binary_search(array, search_array[i], 0, n - 1) == 'yes':
        print('yes', end=' ')
    else:
        print('no', end=' ')


    