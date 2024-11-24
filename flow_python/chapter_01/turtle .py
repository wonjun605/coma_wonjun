import turtle

# 터틀 객체 생성
t = turtle.Turtle()
t.shape("turtle")

# 밑변과 높이의 길이
base = 100
height = 100

# 직각 이등변 삼각형 그리기
t.left(90)  # 왼쪽으로 90도 회전
t.forward(base)  # 밑변 그리기
t.right(135)  # 오른쪽으로 135도 회전
t.forward(height * (2 ** 0.5))  # 높이에 해당하는 대각선 길이만큼 이동
t.right(135)  # 오른쪽으로 135도 회전
t.forward(base)  # 나머지 밑변 그리기
t.left(90)

# 그래픽 창 유지
turtle.done()
