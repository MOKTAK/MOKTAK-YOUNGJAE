import sys
input = sys.stdin.readline

'''
1. 친구들이 받을 사탕의 수를 입력받고, 내림차순으로 정렬한다.
2. 분노의 합을 최소화 하려면, 사탕을 골고루 나누어줘야한다.
    -> 받지 못하는 사탕의 개수가 고르게 분포되도록 한다.(이걸 놓쳤음)
3. 골고루 나누어줄때 친구들이 받을 사탕을 수를 고려한다.
   ex) 친구들이 받을 사탕의 수는 1개인데 2개를 주는 일이 없도록
'''

m, n = map(int, input().split())

friend = []
for _ in range(n):
    friend.append(int(input()))
friend.sort()

print(friend)
# 나누어 주지 못하는 사탕의 개수를 구한다
sum_candy = sum(friend)
left_candy = sum_candy-m

rage_power = 0
for i in range(n):
    '''
    나누어 주지 못한 사탕을 골고루 분배한다.
    친구가 받아야할 사탕의 수가 분배되어야 할 받지 못한 사탕의 수보다 작은 경우가 있을 수 있기 때문에
    이를 고려해서 사탕의 수를 체크한다

    candy = min(friend[i], left_candy//(n-i))

    여기서 candy는 해당 순서의 사람이 못받는 사탕의 개수
    friend[i]는 그 사람이 받고싶어하는 사탕의 개수
    left_candy//(n-i)는 사탕을 나누어주어여할 남은 사람의 수(n-i)를 , 부족한 사탕의 수로 나누어준 값

    위에서 friend를 sort 해주었기 때문에, 사탕을 많이 받길 원하는 사람에게는 더 많은 사탕을 줄 수 있게 된다.

    '''
    candy = min(friend[i], left_candy//(n-i))
    rage_power += candy * candy
    left_candy -= candy

print(rage_power % (pow(2, 64)))
