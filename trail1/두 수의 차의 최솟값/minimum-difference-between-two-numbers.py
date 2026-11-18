n = int(input())
lst = list(map(int, input().split()))

result = []

for i in range(n-1):
    for j in range(i+1,n):
        result.append(abs(lst[j]-lst[i]))

print(min(result))