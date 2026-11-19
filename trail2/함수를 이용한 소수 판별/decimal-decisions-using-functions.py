a, b = map(int, input().split())

def sum_prime(a,b):
    lst = []
    lst_not_prime = []

    for i in range(a,b+1):
        lst.append(i)

    for i in lst:
        for j in range(2,i):
            if i % j == 0:
                lst_not_prime.append(i)
                break
    
    return sum(lst)-sum(lst_not_prime)

print(sum_prime(a,b))