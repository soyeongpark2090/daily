# 특정 문자 제거
from itertools import combinations  # 라이브러리 import


def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer
# 리스트에서 요소 삭제_remove(삭제할 내용), pop(삭제할 인덱스)


# 아이스 아메리카노
def solution(money):
    answer = divmod(money, 5500)
    return answer


# 피자 나눠 먹기(1)
def solution(n):
    quo = n // 7
    rem = n % 7
    if quo in [0, 2] and rem in [0, 6]:
        pass
    elif rem == 0:  # n이 무슨 수라도 될 수 있게_앞에 quo조건 삭제
        return quo
    return quo+1


print(solution(60))


# 최댓값 만들기(1)


def solution(numbers):
    max_val = 0
    num_com = list(combinations(numbers, 2))
    answer = list(map(lambda num: num[0]*num[1], num_com))
    for i in range(len(answer)):
        if answer[i] > max_val:
            max_val = answer[i]
    return max_val

# 런타임 에러 난 코드_빅오 계산해보기

# 요소끼리 곱하는 함수x_map만 쓰지는 못함. map(lambda)사용
# lambda식의 argument 개수 맞추기(주의!), *num_com
# answer = list(map(lambda x, y: x * y, *num_com))
# => 오류: TypeError: solution.<locals>.<lambda>() takes 2 positional arguments but 10 were given


def solution2(numbers):  # 내림차순 정렬
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]


def solution3(numbers):  # 오름차순(기본)
    numbers.sort()
    return numbers[-1]*numbers[-2]


print(solution([0, 31, 24, 10, 1, 9]))


# 배열 두 배 만들기
def solution(numbers):
    answer = []
    for i in numbers:
        dou = i*2
        answer.append(dou)
    return answer


def solution2(numbers):
    return [i*2 for i in numbers]  # 리스트 컴프리핸션(대괄호 주의!)


print(solution2([1, 2, 3, 4, 5]))


# 피자 나눠 먹기(3)
def solution(slice, n):
    quo = n // slice
    rem = n % slice
    if quo in [0, n] and rem in [0, n-1]:  # 범위수정_아까는 7, 지금은 n
        pass
    elif rem == 0:
        return quo
    return quo+1


def solution2(slice, n):
    quo = n // slice
    if n % slice != 0:
        quo += 1
    return quo


print(solution2(7, 21))


# 짝수 홀수 개수
def solution(num_list):
    a = 0
    b = 0
    answer = []
    for i in num_list:
        if i % 2 == 0:
            a += 1
        else:
            b += 1
    answer.append(a)
    answer.append(b)
    return answer


def solution2(num_list):  # 코드 줄이기
    answer = [0, 0]              # a=, b=로 나열하지 말고.
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1  # 이러면 append 안 써도 됨
        else:
            answer[1] += 1
    return answer


def solution3(num_list):
    answer = list(map(lambda x: x % 2, num_list))
    return [answer.count(0), answer.count(1)]


def solution4(num_list):
    answer = sum(1 for i in num_list if i % 2 == 0)
    return [answer, len(num_list)-answer]


print(solution4([1, 3, 5, 7]))


# 자릿수 더하기
def solution(n):
    to_string = str(n)
    answer = []
    for i in range(len(to_string)):
        to_int = int(to_string[i])
        answer.append(to_int)
    return sum(answer)


def solution2(n):
    return sum(list(map(int, str(n))))


print(solution(1234))

# 배열의 유사도


def solution(s1, s2):
    cnt = 0
    for i in s1:
        for j in s2:
            if i == j:
                cnt += 1
    return cnt


def solution2(s1, s2):
    # map() 함수를 사용하여 s1과 s2를 리스트로 변환하여 각 문자열의 각 문자를 순회하며 유사도를 확인합니다.
    ans = sum(map(lambda x, y: x == y, s1, s2))
    return ans


def solution3(s1, s2):
    # set 자료형을 사용하여 두 문자열의 중복을 제거합니다.
    set1 = set(s1)
    set2 = set(s2)
    # 두 문자열의 교집합을 구하여 유사도를 계산합니다.
    answer = len(set1 & set2)
    return answer


print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))


# 양꼬치
def solution(n, k):
    return n*12000 + (k-(n//10))*2000


print(solution(10, 3))


# 버블정렬_코드
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
for i in range(100):  # 0~99
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


a = set([1, 4, 3, 7, 5])

print(a)

# 출력: {1, 3, 4, 5, 7}
