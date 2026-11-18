n = int(input())
price = list(map(int, input().split()))

result = []
if n > 1:
    for i in range(n-1):
        for j in range(i,n):
            result.append(price[j]-price[i])
    if max(result) > 0:
        print(max(result))
    else:
        print(0)
else:
    print(0)