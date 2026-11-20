a, b = map(int, input().split())

def cal(a,b):
    if a > b:
        a = a + 25
        b *= 2
    else:
        b = b + 25
        a *= 2
    return (a,b)

print(*cal(a,b))