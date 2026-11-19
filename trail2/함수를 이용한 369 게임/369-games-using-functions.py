a, b = map(int, input().split())

def is_magic_num(n):
    lst = list(str(n))
    for i in range(len(lst)):
        lst[i] = int(lst[i])

    if 3 in lst or 6 in lst or 9 in lst or n % 3 == 0:
        return True
    else:
        return False

def my_count(a,b):
    sum = 0
    for i in range(a,b+1):
        if is_magic_num(i):
            sum += 1
    return sum

print(my_count(a,b))