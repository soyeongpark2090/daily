# T = int(input())

# for test_case in range(1, T+1):
#     string = list(input())

#     for i in range(len(string)):
#         for j in range(1, 11):
#             if string[0][0:j+1] == string[0][j+1:2*j+3]:
#                 print(f'#{test_case} {j+1}')


# T = int(input())

# for test_case in range(1, T+1):
#     string = input()
#     length = len(string)
#     for j in range(1, length+1):
#         if string[:j] == string[j:2*j]:
#             print(f'#{test_case} {j}')
#             break


T = int(input())

for test_case in range(1, T+1):
    string = input()
    for j in range(1, 11):
        if string[:j] == string[j:2*j]:
            print(f'#{test_case} {j}')
            break
