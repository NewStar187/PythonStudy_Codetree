n = int(input())

def my_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum//10

print(my_sum(n))