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


# 배열의 평균값
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer = sum(numbers[:i+1])/(i+1)
    return answer


def solution2(numbers):
    answer = sum(numbers)/len(numbers)  # sum은 iterable한 각각을 더함. 배열도 iterable함.
    return answer


# 머쓱이보다 키 큰 사람
def solution(array, height):
    cnt = 0
    for i in range(len(array)):
        if array[i] > height:
            cnt += 1
    return cnt


# 배열 원소의 길이
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer
# answer = answer.append(len(i))와 같은 형태는 오류 발생.
# 왜냐하면, append는 return이 없는 함수. 그 자체만 바꿀 뿐.


# 배열 뒤집기
def solution(num_list):
    num_list.reverse()
    return num_list


# 중복된 숫자 갯수
def solution(array, n):
    cnt = 0
    for i in range(len(array)):
        if n == array[i]:
            cnt += 1
    return cnt


# 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1: num2+1]


# 문자열 뒤집기
def solution(my_string):
    answer = my_string[::-1]
    return answer


# 편지
def solution(message):
    answer = 0
    for i in range(len(message)):
        length = len(message[i])*2
        answer += length
    return answer


# 점의 위치 구하기
def solution(dot):
    return 1 if dot[0] > 0 and dot[1] > 0 else\
        2 if dot[0] < 0 and dot[1] > 0 else\
        3 if dot[0] < 0 and dot[1] < 0 else\
        4 if dot[0] > 0 and dot[1] < 0 else None
# 백슬래쉬(\)와 None


# 문자열 안의 문자열
def solution(num1, num2):
    return 1 if num2 in num1 else 2
