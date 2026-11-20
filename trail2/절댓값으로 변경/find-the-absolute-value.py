n = int(input())
arr = list(map(int, input().split()))

def my_abs(n):
    if n >= 0:
        return n
    else:
        return -n

for i in range(len(arr)):
    arr[i] = my_abs(arr[i])

print(*arr)