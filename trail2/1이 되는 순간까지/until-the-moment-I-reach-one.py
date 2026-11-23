N = int(input())

result = 0

def f(n):
    global result

    if n == 1:
        return result

    if n % 2 == 0:
        result += 1
        return f(n//2)
    else:
        result += 1
        return f(n//3)

print(f(N))