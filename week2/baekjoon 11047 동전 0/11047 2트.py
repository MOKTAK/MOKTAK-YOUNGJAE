import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []

for _ in range(n):
    coin.append(int(input()))

count = 0
for i in range(n-1, -1, -1):
    if k == 0:
        break
    count += k//coin[i]
    k %= coin[i]

print(count)
