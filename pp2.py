# swea 패턴마디의 길이
T = int(input())

for test_case in range(1, T+1):
    string = input()
    length = len(string)  # 마디 최대길이가 안 주어진 경우
    for j in range(1, length+1):
        if string[:j] == string[j:2*j]:
            print(f'#{test_case} {j}')
            break


T = int(input())

for test_case in range(1, T+1):
    string = input()
    for j in range(1, 11):  # 마디 최대길이가 10으로 주어짐
        if string[:j] == string[j:2*j]:
            print(f'#{test_case} {j}')
            break
