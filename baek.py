# 모의고사
def solution(answers):
    answer = []
    val = [0, 0, 0]

    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if person1[i % len(person1)] == answers[i]:  # 나머지 이용
            val[0] += 1

        if person2[i % len(person2)] == answers[i]:  # elif가 아니라 if(중복허용이니까)
            val[1] += 1

        if person3[i % len(person3)] == answers[i]:  # elif가 아니라 if(중복허용이니까)
            val[2] += 1

    for j in range(len(val)):
        if val[j] == max(val):
            answer.append(j+1)
    # 인덱스에 접근해야 하므로, for i in val: 아님
    # 인덱스가 0부터 시작하므로, 1부터 시작하는 실제번호 맞춰주기
    return answer


# 출력 [3]
a = solution((3, 1, 2, 4, 2, 5, 4, 3, 5, 2))
print(a)


# 버블정렬
numbers = [7, 5, 2, 6, 1, 8, 9, 4]


def bubble_sort(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(i):  # 이미 정렬 완 된 가장 뒷 수는 제외하고 반복
            if numbers[j] > numbers[j + 1]:
                print(f'{i=}, {j=}')
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


print(bubble_sort(numbers))


# 백준_최댓값
max_num = 0
row = 1  # 프린트해주려면 맨 바깥에 선언되어 있어야. 보기 쉽게 초기화는 1
col = 1

for i in range(1, 10):
    n = list(map(int, input().split()))

    for index, val in enumerate(n, 1):
        if val > max_num:
            max_num = val
            row = i
            col = index

print(max_num)
print(row, col)


# 백준_수 찾기
a = int(input())
n = sorted(map(int, input().split()))
b = int(input())
m = sorted(map(int, input().split()))


def binary_search(array, target):
    left = 0
    right = len(array)-1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid-1
        elif array[mid] < target:
            left = mid+1
        else:
            return 1
    return 0


for i in m:
    result = binary_search(n, i)
    print(result)


# 백준_색종이
paper = [[0 for i in range(100)] for j in range(100)]  # 0으로 초기화된 2차원 종이 선언

N = int(input())
# 한줄씩 입력되므로. 다시 안 쓸 거면 데이터 입력받을 때는 (변수 선언 말고) _써도 됨    #오류의 원인: N번 받아야.
for _ in range(N):
    x, y = map(int, input().split())  # x는 종이와 가로거리, y는 종이와 세로거리

    for i in range(1, 11):  # for 가독성:1~10
        for j in range(1, 11):
            paper[x+i][y+j] = 1  # 오류의 원인: paper[i][j]로 했었음.

ans = 0
for i in range(100):
    for j in range(100):
        ans += paper[i][j]

print(ans)


# 백준_랜선 자르기
K, N = map(int, input().split())  # k는 있는 랜선 개수, n은 만들어야 하는 랜선 개수

arr = []
for i in range(K):
    arr.append(int(input()))

arr.sort()  # arr은 정렬됨, print(arr)로 확인 가능, 이분 탐색은 정렬 꼭 필요!!

start = 1
end = max(arr)  # 이 2줄을 start, end = 1, max(arr)로 해도 가능
ans = 0

while start <= end:
    mid = (start + end) // 2

    lan_cnt = 0
    for i in range(K):
        lan_cnt += arr[i]//mid

    if lan_cnt >= N:  # 문제조건
        start = mid+1
        ans = mid  # lan_cnt줄여야=>mid늘려야=>현 mid보다 작은 값은 이제 제외=>start값 재조정
    elif lan_cnt < N:
        end = mid-1

print(ans)
