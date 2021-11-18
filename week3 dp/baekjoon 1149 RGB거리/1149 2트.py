import sys
input = sys.stdin.readline

n = int(input())
cost = []

for _ in range(n):
    cost.append(list(map(int, input().split())))

'''
두번째 집부터 시작해서, 두번째 집의 빨강, 초록, 파랑색을 선택했을 각각의 경우의 최소값을 찾는다
만약 두번째 집이 빨강인 경우라면, 첫번째 집인 초록 또는 파랑일 경우 중 더 작은 값을 찾고, 지금의 빨강집의 가격을 더해주는식!
이렇게 끝 집까지 최소 cost를 구한 뒤, 그중에서도 가장 합이 작은 수를 찾아 출력한다.
'''
for i in range(1, n):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]


print(min(cost[n-1][0], cost[n-1][1], cost[n-1][2]))
