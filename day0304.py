# range(len())_2가지 경우
a_list = [1, 2, 3, 5, 6, 7, 4, 7]
for i in range(len(a_list)):  # 리스트 a_list의 길이를 범위로 설정하여 반복
    print(f'index: {i} , value: {a_list[i]}')


b = 'watermelon'
for i in range(len(b)):  # 문자열 watermelon의 길이를 범위로 설정하여 반복
    print(i, b[i])
# index와 value 혼동하지 말 것.


# 짝수의 합_ 여러가지 방법
def solution(n):
    return sum([x for x in range(2, n+1, 2)])


def solutions2(n):
    return sum(range(2, n+1, 2))


def solutions3(n):
    return sum(filter(lambda x: x % 2 == 0, range(n+1)))


def solutions4(n):
    cnt = 0
    for i in range(2, n+1, 2):
        cnt += i
    return cnt


# print(solutions2(10))
# print(solutions3(10))
# print(solutions4(10))


# 오늘 작성한 코드 (문제1~문제10)
def solution(num1, num2):       # 두 수의 차
    answer = num1-num2
    return answer


def solution(num1, num2): return num1*num2     # 두 수의 곱


def solution(num1, num2):       # 숫자 비교하기
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer


def solution(num1, num2):           # 숫자 비교하기 _여러가지 방법
    return 1 if num1 == num2 else -1


def solution(num1, num2):       # 나머지 구하기_ anwer=-1이 있어야 예외처리(num2가 0인 경우)
    return num1 % num2


def solution(num1, num2):
    answer = -1
    answer = num1 % num2
    return answer


def solution(num1, num2):       # 몫 구하기 _ 몫도 answer=-1이 있어야 예외처리(num2가 0인 경우)
    answer = divmod(num1, num2)
    return answer[0]


def solution(num1, num2):
    answer = -1
    answer = num1 // num2
    return answer


def solution(age):              # 나이 출력
    result = 2022 - (age-1)
    return result


solution = (lambda num1, num2: num1+num2)      # 두 수의 합


def solution(num1, num2):               # 두 수의 나눗셈
    answer = int((num1 / num2)*1000)
    return answer


def solution(angle):        # 각도기
    if 0 < angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90 < angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4
    return answer


def solution(n):        # 짝수의 합
    cnt = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            cnt += i
            continue
    return cnt
