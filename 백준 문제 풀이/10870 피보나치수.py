























def fibonacci(n):
    if n <= 1:    # 종료 조건을 설정함
        return n
    return fibonacci(n-1) + fibonacci(n-2)    #피보나치는 전, 전전항의 합이기 때문


import sys
n = int(sys.stdin.readline().strip())
print(fibonacci(n))