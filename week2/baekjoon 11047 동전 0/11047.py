n, k = map(int, input().split())
result = 0

coin = []
for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in coin:
    if k == 0:
        break
    result += k//i
    k %= i

print(result)
