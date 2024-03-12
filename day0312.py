# n의 배수 고르기
def solution2(n, num_list):
    for i in num_list:
        if i % n != 0:
            num_list.remove(i)
    return num_list
# 리스트를 수정하는 동시에 for문을 돌고 있어서 원하는 값 출력이 안됨


def solution(n, num_list):
    a = num_list[:]
    for i in num_list:
        if i % n != 0:
            a.remove(i)
    return a
# [:]는 복사본을 만드는 만드는 표기임


print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))
