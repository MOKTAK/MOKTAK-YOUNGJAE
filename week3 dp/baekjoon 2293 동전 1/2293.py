import sys
input = sys.stdin.readline

coin = []
n, k = map(int, input().split())
dp = [0] * (k+1)

for _ in range(n):
    coin.append(int(input()))

# 동전을 한개만 쓸 때의 경우의 수를 고려하기 위해 dp[0]을 1로 선언한다
dp[0] = 1

for i in coin:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])
