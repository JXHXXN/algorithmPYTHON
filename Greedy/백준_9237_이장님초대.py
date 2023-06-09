# 구입한 n개의 나무 묘묙, 묘목 하나를 심는데 걸리는 시간은 1일, 상근이는 각 묘목이 다 자라는데 며칠이 걸리는지 정확하게 안다.
# 마지막 나무가 다 자란 다음날 이장님을 초대하려고 한다. 초대할 수 있는 최대 빠른 날짜는?
# 입력 첫째줄 -> 묘목의 수 n, 입력 둘째줄 -> 각 나무가 다 자라는데 걸리는 날 ti
# 입력 둘째줄 -> 며칠에 이장님을 초대할 수 있는가? 묘목을 구입한 날은 1이고 답이 여러가지인 경우에는 가장 작은 값 출력

# 오래걸리는 나무부터 심어야 최대한 빨리 나무들을 모두 기를 수 있기에 나무들의 일수를 내림차순으로 정렬한다.
# 마지막에 자라는 나무를 찾고 나무를 심는데 걸리는 일수의 최댓값을 저장해주며 바꿔주는 과정을 반복한다.
# 조건문을 이용해 최종적으로 자라나는 나무를 탐색한 후 max값을 갱신한다.
# 처음 심는 1일과 나무가 다 자라고 다음날 이장님을 초대하기에 총 2일을 더해준다.

n = int(input()) #입력 받을 묘목의 수
days = list(map(int, input().split())) #입력 받을 각 나무가 자라는데 걸리는 날

days.sort(reverse= True) #나무가 자라는 속도 역정렬

max = days[0] #최댓값 저장

if n == 1: #묘목이 한그루면
    print(n + 2) #2일 더해서 출력
else:
    for i in range(1, n): #모든 묘목 자랄 때 까지
        if max < (i + days[i]): #최대일수 값
            max = i + days[i] #갱신

    result = max + 2 #최댓값에 앞1일 뒤1일 추가
    print(result)