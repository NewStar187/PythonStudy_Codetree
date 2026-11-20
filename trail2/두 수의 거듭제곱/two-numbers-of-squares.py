a, b = map(int, input().split())

def mult(a,b):
    new_a = 1
    for i in range(b):
        new_a *= a
    return new_a

print(mult(a,b))