# swea 거듭제곱
def solution(a, n):
    if n == 1:
        return a
    else:
        return a*solution(a, n-1)


for i in range(1, 11):
    test_case = int(input())
    x, y = map(int, input().split())
    print(f'#{test_case} {solution(x,y)}')


# #문자열 거울상
# T = int(input())

# for test_case in range(1, T + 1):
#     word = input()
#     new = ''
#     for i in word[::-1]:
#         if i == 'b':
#             new.append('d')
#         elif i == 'd':
#             new.append('b')
#         elif i == 'p':
#             new.append('q')
#         else:
#             new.append('p')
#     print(f'#{test_case} {new}')


# 회선1_진원님 코드
# def count_palindromes(test, length):
#     count = 0
#     for i in range(8):
#         for j in range(8 - length + 1):
#             row = test[i][j:j + length]
#             if row == row[::-1]:
#                 count += 1

#             column = ""
#             for k in range(length):
#                 column += test[j + k][i]
#             if column == column[::-1]:
#                 count += 1
#     return count

# result = []
# for _ in range(10):  # 테스트 케이스가 10번 반복
#     length = int(input())
#     test = []
#     for _ in range(8):
#         test.append(input())

#     count = count_palindromes(test, length)
#     result.append(count)

# for i, count in enumerate(result, start=1):
#     print("#{} {}".format(i, count))


# 이중for문 공부중..
for i in range(7):
    for j in range(i + 4):
        print('*', end='')
    print()
