# 문자열에서 특정 알파벳이 몇 번 나타나는지 알아봐서 자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있다.
# 특정 문자열 S, 특정 알파벳 a, 문자열의 구간 [l, r]이 주어지면 S의 l번째 문자부터 r번째 문자 사이에 a가 몇번 나타나는지 구하는 프로그램을 작성하라.
# 문자열의 문자는 0부터 세고 l번째와 r번째 문자를 포함해서 생각한다. 통계적으로 크게 무의미한 같은 문자열을 두고 질문을 q번 할것이다.
# 입력 첫번째줄 -> 문자열 S. 입력 두번째줄 -> 질문의 수 q, 입력 세번째줄 ~ q+2번째 줄 -> 알파벳 소문자 ai 와 0 <= l, <= r < |s|를 만족하는 정수 li, ri가 공백으로 구분되어 주어진다.
# 출력 -> 각 질문마다 줄을 구분해 순서대로 답변. i번째 줄에 Sdml li 번째 문자부터 ri번째 문자 사이에 ai가 나타내는 횟수 출력

# 누적합으로 풀어야 시간초과가 나지 않는다. 누적해서 횟수를 쌓아가자
# 가장 먼저 문자열을 입력받고 a-z별로 누적합을 먼저 저장한 후 매 질문이 들어올 때 저장한 누적합의 계산을 통해 바로 답 구현

import sys

input = sys.stdin.readline
s = list(input().rstrip()) #입력받을 문자열
q = int(input().rstrip()) #입력받을 질문의 수

cList = [[0] * len(s) for _ in range(26)] #알파벳 숫자로 표현

for i in range(len(s)): #문자열의 문자 수만큼
    cList[ord(s[i]) - ord('a')][i] += 1 #a는 1 이후로 하나씩 +1

for i in range(26): #알파벳개수 만큼
    for j in range(1, len(s)): #1부터 문자열 수만큼
        cList[i][j] += cList[i][j - 1] #누적합 힛수 저장

for i in range(q): #입력받을 질문의 개수만큼
    a, l, r = input().split() #입력받을 알파벳 소문자와 문자열 구간
    tmp = cList[ord(a) - ord('a')][int(r)] - cList[ord(a) - ord('a')][int(l)] #미리 인덱스로 저장

    if s[int(l)] == a: #입력받은 문자열 문자가 a이면
        tmp += 1 #나온 문자만큼 누적합에 +1

    print(tmp) #누적합 출력