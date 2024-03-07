# def solution(price):
#     answer = 0
#     if price >= 500000:
#         answer = 0.8*price
#     elif price >= 300000:
#         answer = 0.9*price
#     elif price >= 100000:
#         answer = 0.95*price
#     else:               #빠진 조건 넣음 => 정답
#         answer = price
#     return int(answer)
# # #오류=>if elif elif 조건 충돌나지 않게 해줘야 함 + 빠진 조건 없는지!


# def solution(price):
#     if price >= 500000:
#         price = 0.8*price
#     elif price >= 300000:
#         price = 0.9*price
#     elif price >= 100000:
#         price = 0.95*price
#     return int(price)
# # #정답


# print(solution(580000))


def solution(n):
    for i in range(n):
        ans = '#'*n
    print(ans)


solution(n)



pan = 