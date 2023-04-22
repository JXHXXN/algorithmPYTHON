# 스티커 2n개를 구매했고 2행 n열로 배치되어 있다. 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어낸다.
# 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합은?
# 규칙) 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없다 -> 뗀 스티커의 상하좌우 스티커 사용불가.
# 힌트) 점수가 50 50 100 60 스티커를 고르면, 점수는 260되고 최대점수이다. 가장 높은 점수를 가지는 두 스티커 100 70은 변을 공유하기에 동시에 뗄 수 없다.
# 입력 첫째줄 -> 테스트 케이스의 개수 T, 입력 둘째줄 -> n, 입력 셋째, 넷째줄 -> n개의 정수(각 점수는 그 위치에 해당하는 스티커의 점수)
# 연속하는 두 정수 사이에 빈 칸이 하나 있음. 점수는 0보다 크거나 같고, 100보다 작거나 같다.
# 출력 첫째줄 -> 각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력

# 스티커 떼면 상하좌우까지 뗴어지기에 스티커 선택에 따라 다음 순서가 다름

t = int(input()) #테스트 케이스 개수 입력받기

for i in range(t): #테스트 케이스 개수만큼 반복
    sticker = int(input()) #스티 점수 입력받기
    graph = [] #스티커 정수 정렬하기
    for j in range(2): #2행
        graph.append(list(map(int, input().split()))) #입력받은 스티커 점수

    if sticker == 1:#입력받은게 1이라면
        print(max(graph[0][0], graph[1][0])) #출력값으로
        continue

    graph[0][1] += graph[1][0] #대각선
    graph[1][1] += graph[0][0]

    for k in range(2, sticker): #2부터 입력받은 값 까지
        graph[0][k] += max(graph[1][k - 1], graph[1][k - 2])
        graph[1][k] += max(graph[0][k - 1], graph[0][k - 2])

    print(max(graph[0][sticker - 1], graph[1][sticker - 1])) #누적된 값 중 최댓값 선택해 출력