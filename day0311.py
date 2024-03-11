#문자열을 정수로 변환하기
def solution(n_str):
    return int(n_str)


print(solution("250"))


뒤에서 n글자
def solution(my_string, n):
    return my_string[-n:]       #:n, n:


print(solution("Programmers123",5))


#문자열로 변환
def solution(n):
    return str(n)


print(solution(123))


# n번째 원소부터
def solution(num_list, n):
    return num_list[n-1:]


print(solution([5, 2, 1, 7, 5],2))


rny_string
def solution(rny_string):
    return rny_string.replace('m', 'rn')


print(solution('programmers'))


#두 수의 연산값 비교하기
def solution(a,b):
    x = str(a)+str(b)
    y = 2*a*b
    return max(int(x),y)


print(solution(91,2))


#수 조작하기 1
def solution(n,control):
    while True:
        for i in range(len(control)):
            if 'w' == control[i]:
                n += 1
            elif 's' == control[i]:
                n -= 1
            elif 'd' == control[i]:
                n += 10
            else:
                n -= 10
        return n


def solution2(n, control):
    for i in control:
        if i=='w':n+=1
        elif i=='s':n-=1
        elif i=='d':n+=10
        else:n-=10
    return n


def solution3(n,control):
    answer = n
    x = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    for i in control:
        answer += x[i]
    return answer


print(solution3(0, 'wsdawsdassw'))


#정수 찾기
def solution(num_list,n):
    if n in num_list:
        return 1
    return 0


print(solution([1, 2, 3, 4, 5],3))


#홀짝 구분하기
n = int(input())
if n%2 == 0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')


#뒤에서 5등까지
def solution(num_list):
    num_list.sort()
    answer = []
    a = [num_list[0],num_list[1],num_list[2],num_list[3],num_list[4]]
    answer.extend(a)
    return answer

# answer.append(a)
#출력 [[4, 5, 6, 8, 28]]

def solution2(num_list):
    num_list.sort()
    return num_list[:5]


def solution3(num_list):
    return sorted(num_list)[:5]


print(solution([4,6,8,28,5,95,63]))




#알고리즘 문제
#N과 M
N, M = map(int, input().split())
ans = []

def solution():
    # a = [i for i in range(1,N+1)]
    if len(ans) == M:
        # print(f'프린트닷!')
        print(' '.join(map(str,ans)))        #map(func, iterable)
        return

    for j in range(1, N+1):
        if j not in ans:
            # print(f'새로운 선택 전의 >> {ans}')
            ans.append(j)
            # print(f'append함!')
            # print(ans)
            # print(f'이제 함수호출~')
            solution()
            # print(f'재귀 후의 >> {ans}')
            ans.pop()
            # print(f'pop이후 >> {ans}')

solution()


#연산자 끼워넣기
import sys

n = int(input())
arr = list(map(int, input().split()))
pl,mi,mul,div = map(int, input().split())

max_val = -sys.maxsize
min_val = sys.maxsize

def dfs(cum_val, num, pl, mi, mul, div):
    global max_val, min_val
    if num == n:        # == n-1 아님
        max_val = max(max_val, cum_val)
        min_val = min(min_val, cum_val)
        return

    if pl > 0:
        dfs(cum_val+arr[num], num+1, pl-1, mi, mul, div)
    if mi > 0:
        dfs(cum_val - arr[num], num+1, pl, mi-1, mul, div)
    if mul > 0:
        dfs(cum_val * arr[num], num+1, pl, mi, mul-1, div)
    if div > 0:
        dfs(int(cum_val / arr[num]), num+1, pl, mi, mul, div-1)


dfs(arr[0], 1, pl, mi, mul, div)
print(max_val)
print(min_val)

# 입력 예1
# 2
# 5 6
# 0 0 1 0


# 입력 예2
# 6
# 1 2 3 4 5 6
# 2 1 1 1