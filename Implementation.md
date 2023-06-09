## Implementation, 구현
**구현의 정의**

머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정이다.

<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/c51e5580-b89a-4861-8fc0-427c3aad9fb4" width = "400" />

(구현 관련 설명을 찾다보면 이그림은 무조건 있다)

**구현 유형의 문제?**

-   알고리즘은 간단하나 코드가 길어지는 문제
-   실수 연산을 다르고 특정 소수점 자리까지 출력해야 하는 문제
-   문자열이 입력으로 주어졌을 때 한 문자 단위로 끊어서 리스트에 넣어야 하는 문제
-   2차원 배열(행렬Matrix)에서의 이동, 회전 등 까다로운 문제
-   특정한 라이브러리를 찾아서 사용해야 하는 문제
-   풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제

**완전 탐색 유형**

모든 경우의 수를 주저없이 다 계산하는 해결 방법이다.

**시뮬레이션 유형**

문제에서 제시한 알고리즘들을 한 단계의 차례대로 직접 수행해야 하는 문제이다.

**코딩테스트에서의 구현 문제를 풀 때 알아야 할 것**

-   메모리 사용량 제한보다 더 적은 크기의 메모리를 사용해야한다.
-   탐색해야 할 전체 데이터의 개수가 100만개 이하일 때 완전 탐색을 사용하면 적절하다.
-   좌표평면에서 상하좌우로 이동해야 하는 경우 dx, dy 리스트를 선언해 이동할 방향을 기록한다. 이 외에 상하좌우+대각선 방향으로 이동한다면 →steps = \[(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1,2)\] 로 표현하는 것이 좋다.
-   2차원 리스트를 선언할 때는 리스트 컴프리헨션 문법을 사용하는 것이 효율 적이다. → d = \[\[0\] \* m for \_ in range(n)\]

**완전 탐색 유형의 문제풀이: 시각**

문제: 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성한다.

예를 들어 1을 입력 했을때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다

00시 00분 03초, 00시 13분 30초

반면에 다음은 3이 하나도 포함되어 있지 않기에 세면 안되는 시각이다

00시 02분 55초, 01시 27분 45초

**문제해결 과정:**

가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있다.

하루는 86,400초(24시간 \* 60분 \* 60초 = 총 86400초)이므로, 00시 00분 00초부터 23시 59분 59초까지의 모든 경우는 86,400초이다.

따라서 딘순히 시각을 1씩 증가시키면서 하나라도 포함되어 있는지를 확인하면된다.

→가능한 모든 경우의 수를 검사해보는 완전탐색문제이다.

```
<구현>
n = int(input()) #몇시까지 세야하는지 입력
count = 0 #경우의 수 카운트

for h in range(n + 1): #0 ~ n시까지 체크
		for m in range(60): #0 ~ 59분 
			for s in range(60): #0 ~ 59초
					a = str(h) + str(m) + str(s) #문자열로 합쳐주기
					if '3' in a: #3이 포함되어 있는가
							count += 1 #카운트

print(count) #출력
```

**시뮬레이션 유형의 문제 풀이: 상하좌우**

**문제:** 여행가 A는 N\*N크기의 정사각형 공간 위에 서있다.

1\*1 크기의 정사각형으로 나누어져 있고

가장 왼쪽 위 좌표는 (1, 1)이며 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.

여행가 A는 상하좌우 방향으로 이동이 가능하고 시작 좌표는 항상 (1, 1)이다.

A가 이동할 계획서가 주어지고 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다.

L: 왼쪽으로, R: 오른쪽으로, U: 위로, D: 아래로 →각 방향으로 한칸 이동

여행가 A가 주어진 크기의 정사각형 공간을 벗어나는 움직임은 무시한다.

주어진 계획서에서 A가 최종적으로 도착할 지점의 좌표는?

**문제해결 과정:**

요구사항대로 충실히 구현하는 되는 문제이다.

```
<구현>
#n 입력 받기
n = int(input())
plans = input().split()

#상하좌우에 따른 이동방향
move_types = ['U', 'D', 'L', 'R']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#시작 좌표
x, y = 1, 1

#이동 계획에 따라 움직인다.
for plan in plans:
	#이동방향 확인
	for i in range(len(move_tyoes)):
		if plan == move_types[i]:
			nx = x + dx[i]
			ny = y + dy[i]

		#공간을 벗어나는 경우 무시
		if nx < 1 or ny < 1 or nx > n or ny > n:
			continue
	
		#이동수행
		x, y = nx, ny

print(x,y)
```

---

**\[참조\]**

> [https://velog.io/@jiffydev/이론파이썬-알고리즘-구현Implementation](https://velog.io/@jiffydev/이론파이썬-알고리즘-구현Implementation) #구현 유형  
> [https://velog.io/@kyunghwan1207/그리디-알고리즘Greedy-Algorithm-탐욕법](https://velog.io/@kyunghwan1207/그리디-알고리즘Greedy-Algorithm-탐욕법) #구현 문제 풀이[https://blackon29.tistory.com/62](https://blackon29.tistory.com/62) #파이썬에서 코딩테스트 구현 문제에 접근하는 방법  
> [https://doing7.tistory.com/70](https://doing7.tistory.com/70) #구현 문제 풀이 [https://subinze.tistory.com/12](https://subinze.tistory.com/12) #구현 문제 풀이  
> [https://velog.io/@ryan01/구현-시각](https://velog.io/@ryan01/구현-시각) #구현 문제 풀이
