from collections import deque
import heapq


# #쇠막대기

# 바이러스
# N = int(input())
# M = int(input())
#
# graph = [[] for _ in range(N)]
# visited = [0 for _ in range(N)]
#
#
# for _ in range(M):  #i: 0,1,2,3,4,5,6
#     a,b = map(int,input().split())
#
#     graph[a-1].append(b)
#     graph[b-1].append(a)
#
#     # print(arr)
#     # [[2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
#
# def dfs(cur):
#     print(f'{visited=}')
#     print(f'{graph=}')
#     visited[cur-1] = 1      #어차피 접근의 인덱스가 0부터임
#
#     for nxt in graph[cur-1]:
#         # print(nxt)
#         if visited[nxt-1] == 0:   #False
#             dfs(nxt)
#
#
# dfs(1)
# print(visited)
# print(sum(visited)-1)   #1번(=시작노드) 노드의 방문표시를 빼줌
# 이렇게 인덱스를 주면 헷갈림_그냥 0부터 시작해야..아래코드!


N = int(input())
M = int(input())

# N=7  #a-1,b-1아니고 a,b로 하려면 N+1이어야 함 #graph[7]까지 접근 가능하려면.
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):  # 0,1,2,3,4,5   #N=6 (아래 표시해야 하는 양방향 수가 6개=M개)
    a, b = map(int, input().split())

    graph[a].append(b)  # input 자체가 1~7_1번 컴퓨터~
    graph[b].append(a)
    print(graph)
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]


def dfs(cur):
    # print(f'{visited=}')
    # print(f'{graph=}')
    visited[cur] = 1

    for nxt in graph[cur]:
        # print(nxt)
        if visited[nxt] == 0:  # False
            dfs(nxt)


dfs(1)
print(visited)
print(sum(visited)-1)  # 1번(=시작노드) 노드의 방문표시를 빼줌


# 카드2
N = int(input())


def last_card(N):
    queue = deque(range(1, N+1))  # queue에 1~N-1까지 push한다..
    print(queue)

    while len(queue) > 1:  # 1234
        queue.popleft()  # 234
        queue.append(queue.popleft())  # 342  #변수에 담아도 되고, 이렇게 한번에 해도 됨
    return queue[0]


print(last_card(N))


# 프린트 큐
N = int(input())

for _ in range(N):
    # 처음 입력받을 때의 idx와 중요도값   #target의 idx값을 추적해야 하므로, 묶어서 표시   #for문 안에 있어야_이전 큐가 초기화됨
    queue = deque()
    cnt = 1

    a, b = map(int, input().split())  # 문서의 수, 궁금한 문서의 인덱스
    arr = list(map(int, input().split()))  # 중요도

    for i in range(len(arr)):
        queue.append((arr[i], i))

    while queue:
        val, idx = queue.popleft()
        # 전체 튜플을 val과 비교하는 게 아니라, 튜플의 0번째 인덱스와 비교
        if queue and val < max(queue, key=lambda x: x[0])[0]:
            queue.append((val, idx))  # 이때는 인쇄한게 아니므로 cnt값은 변화가 없음
        else:
            if idx == b:
                print(cnt)  # 얘 때문에 cnt 초기화를 1로 해야함
                break
            cnt += 1


# 카드 합체 놀이
N, T = map(int, input().split())  # 숫자의 개수, 합체 횟수

arr = list(map(int, input().split()))
heapq.heapify(arr)  # 최소힙(디폴트 인 파이썬)
# print(f'{arr} 최소힙 되다!')

for _ in range(T):
    if arr:  # 큐 문제에서는 붙여주는 게 좋음_이 문제에서는 없어도 가능하긴 함(arr에 수가 2개 미만인 경우 없음)
        a = heapq.heappop(arr)  # 그리디의 일종_작은 값 두개를 뽑아야.
        b = heapq.heappop(arr)
        # print(f'{a=}, {b=}')
        # print(f'{arr} 힙팝 이후!')

        heapq.heappush(arr, a+b)
        # print(f'arr1 >> {arr}')     #자식들 간 대소관계는 고려x => a,b 무관하게 붙임_자동 조절
        heapq.heappush(arr, a+b)
        # print(f'arr2 >> {arr}')


print(sum(arr))
