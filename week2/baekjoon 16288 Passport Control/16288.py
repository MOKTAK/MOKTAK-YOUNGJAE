import sys
input = sys.stdin.readline

n, k = map(int, input().split())
order = list(map(int, input().split()))

# 심사 창구의 개수만큼의 원소를 가진 리스트를 만들어준다.
# 이 리스트의 원소로는, 해당 창구에 들어온 마지막 사람의 순서를 넣어줄 예정.
gate = [0]*k

for i in range(n):
    # i번째로 나온 사람이 창구에 들어갈 수 있는지 여부를 파악하기 위한 booleean 변수
    check = False
    for j in range(k):
        # 창구에 들어갈 차례가 된 사람이 해당 창구에 들어갈 수 있는지 여부를 파악한다
        # 해당 창구에 먼저 들어간 사람이, 자기보다 순서가 앞인 경우에만 들어갈 수 있다.
        # 가령, 세번째로 들어간 사람 앞에 네번째 사람이 들어가 있는 경우는 없으니까!
        if gate[j] < order[i]:
            # 들어갈 수 있는 창구가 있는 경우엔, 해당 창구에 현재 차례의 순번을 업데이트해주고
            gate[j] = order[i]
            # i번째 사람이 창구에 들어갈 수 있는 상황이니 True로 업데이트하고 for(j)문을 종료한다
            check = True
            break
    # 모든 창구를 검사했는데, 아무런 업데이트가 없는 경우에는
    # i번째 사람이 나올 수 있는 방법이 없다는 의미이기에 for(i)를 종료한다.
    if not check:
        break
# 최종적으로 제 순서에 나올 수 없는 경우가 존재한다면 NO를 출력하고
if not check:
    print("NO")
# 가능하다면 YES를 출력한다.
else:
    print("YES")
