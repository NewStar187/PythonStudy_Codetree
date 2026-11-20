n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def continued_arr(a,b):
    if len(a) == len(b):
        if a == b:
            return True
        else:
            return False

    for i in range(len(a) - len(b)+1): # 시작지점 i
        if a[i:i+len(b)] == b:
            return True
    return False

if continued_arr(a,b):
    print("Yes")
else:
    print("No")