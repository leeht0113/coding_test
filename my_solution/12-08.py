import sys
input = sys.stdin.readline
a = input()
alpha = ''.join(sorted(list(filter(str.isalpha, a))))
num = str(sum(list(map(int, filter(str.isdigit, a)))))
print(''.join(alpha + num))
