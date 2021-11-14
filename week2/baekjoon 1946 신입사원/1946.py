import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    count = 1
    person = []

    for i in range(n):
        grade, rank = map(int, input().split())
        person.append([grade, rank])

    #  우선 서류 성적으로 오름차순 정렬 후, 면접 성적만 비교한다
    person.sort()
    min_rank = person[0][1]

    for i in range(n):
        # 하나씩 비교를 해주면서, 면접 순위가 더 높으면
        # count를 1올리고, min_rank를 업데이트 해준다.
        if person[i][1] < min_rank:
            count += 1
            min_rank = person[i][1]

    print(count)
