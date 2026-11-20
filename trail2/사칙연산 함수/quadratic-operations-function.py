a, o, c = input().split()
a = int(a)
c = int(c)

lst = ['+', '-', '*', '/']

def cal(a, o, c):
    if not o in lst:
        return "False"
    else:
        if o == lst[0]:
            return a+c
        elif o == lst[1]:
            return a-c
        elif o == lst[2]:
            return a*c
        else:
            return a//c

if cal(a,o,c) == "False":
    print("False")
else:
    print(f"{a} {o} {c} =",cal(a,o,c))