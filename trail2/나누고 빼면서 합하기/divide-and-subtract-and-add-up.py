n, m = map(int, input().split())
A = list(map(int, input().split()))

def calcul(m):
    sum = 0

    while True:
        sum += A[m-1]
        if m % 2 == 0:
            m = m // 2
        elif m == 1:
            break
        else:
            m -= 1

    return sum

print(calcul(m))