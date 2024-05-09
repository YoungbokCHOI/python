
# eval() 함수의 기본 사용법
result = eval('3 * 5 + 2')
print(result)  # 출력: 17

# 변수와 함께 eval() 사용하기
x = 10
y = 20
result = eval('x + y')
print(result)  # 출력: 30

# 함수 호출을 포함하는 eval() 사용하기
def multiply(a, b):
    return a * b

result = eval('multiply(2, 3)')
print(result)  # 출력: 6