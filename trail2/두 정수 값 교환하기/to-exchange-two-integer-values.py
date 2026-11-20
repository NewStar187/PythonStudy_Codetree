n, m = map(int, input().split())

def swap(a,b):
    a,b = b,a
    return a,b

print(*list(map(int,swap(n,m))))