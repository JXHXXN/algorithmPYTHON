# 해빈이는 한번 입었던 옷들의 조합을 절대 다시 입지 않는다.
# 예를 들어 오늘 안경, 콭, 상의, 신발이라면 다음날은 바지를 추가로 입거나 안경대신 렌즈 착용하거나 해야함.
# 의상들이 주어졌을 때 며칠동안 돌아다닐 수 있나
# 입력 첫쨰줄 -> 각 테스트 케이스 수, 입력 둘째줄 -> 해빈이가 가진 의상의 수, 입력 셋쨰줄 ~~ 의상의 수 -> 의상이름, 종류 (같은 종류의 의상은 하나만 입을 수 있). 다음 입력 -> 새로운 케이스의 의상수 ~~ 의상 종류 및 이름
# 출력 첫째줄 -> 각 케이스에 대해 입을 수 있는 의상 경우의 수

# 같은 종류의 의상은 하나씩만, 꼭 1종류 이상의 의상은 착용해야한다. 0종류만 아니면 된다.
# (a 종류수 + 1) * (b 종류수 + 1) * (c 종류수 + 1) ... -1
# 종류수에 + 1 을 해 준 이유는 그 종류의 의상을 착용해도 되고 안해도 된다.
# 마지막에 - 1 을 해 준 이유는 모든 의상을 착용하지 않은 경우를 제외시켜줘야 한다.

from collections import Counter #Counter모듈 불러오기

t = int(input()) #테스트 케이스 개수 입력받기

for i in range(t): #케이스 수 만큼 반복
    n = int(input()) #혜빈이가 가진 의상의 수
    wear = [] #옷 종류
    for j in range(n): #가진 옷 종류 수 만큼 반복
        a, b = input().split() # 옷이름 입력받기
        wear.append(b) #옷종류에 b추가

    wear_Counter = Counter(wear) #카운터를 이용해 자동으로 세준다
    count = 1 #각 종류마다 항목의 개수

    for key in wear_Counter: #입을 수 있는 옷 카운팅 하기
        count *= wear_Counter[key] + 1 #입을 수 있는 경우의 수는 = (경우의 수[의상]+1임) * count

    print(count - 1) #아무것도 안입은 경우 제외