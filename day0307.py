def solution(price):
    answer = 0
    if price >= 500000:
        answer = 0.8*price
    elif price >= 300000:
        answer = 0.9*price
    elif price >= 100000:
        answer = 0.95*price
    else:  # 빠진 조건 넣음 => 정답
        answer = price
    return int(answer)
# 오류=>if elif elif 조건 충돌나지 않게 해줘야 함 + 빠진 조건 없는지!
# price 자체는 값을 가지므로 answer로 변수 준 경우와는 필요 없음


def solution(price):
    if price >= 500000:
        price = 0.8*price
    elif price >= 300000:
        price = 0.9*price
    elif price >= 100000:
        price = 0.95*price
    return int(price)
# 정답


print(solution(580000))

# 세균증식


def solution(n, t):
    return (2**t)*n


# 삼각형의 완성조건
def solution(sides):
    if max(sides) < sum(sides)-max(sides):
        return 1
    return 2


# 중앙값 구하기
def solution(array):
    array.sort()
    for i in range(len(array)):
        if i == len(array)//2:
            return array[i]


# 짝수는 싫어요
def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 != 0:
            answer.append(i)
    return answer


# 순서쌍의 개수
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append((i, n//i))
    return len(answer)
