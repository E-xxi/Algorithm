n= int(input()) # 앞의 글자는 n, 뒤의 글자는 m으로 할당됨.
change = []

for _ in range(n): # m번 loop을 돌면서 input을 arr에 append
	change.append(list(map(int, input().split())))

ball_pos = 1

#안의 숫자를 기준으로 바꿔야함. 
for row in change:
    if row[0] == ball_pos:
        ball_pos = row[1]
    elif row[1] == ball_pos:
        ball_pos = row[0]
        

#가장 첫번째 컵 숫자 반환
print(ball_pos) 
