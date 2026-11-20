a, b = map(int, input().split())

def cal(a,b):
    a_temp = a
    b_temp = b
    if a > b:
        a_temp *= 2
        b_temp += 10
    else:
        a_temp += 10
        b_temp *= 2

    return (a_temp,b_temp)

print(*cal(a,b))