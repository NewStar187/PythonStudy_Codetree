a, b = map(int, input().split())

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def sum_even(n):
    n_lst = list(str(n))
    for i in range(len(n_lst)):
        n_lst[i] = int(n_lst[i])
    
    if sum(n_lst) % 2 == 0:
        return True
    else:
        return False

def count_of_magic_num(a,b):
    result = []

    for i in range(a,b+1):
        if is_prime(i) and sum_even(i):
            result.append(i)

    return len(result)

print(count_of_magic_num(a,b))