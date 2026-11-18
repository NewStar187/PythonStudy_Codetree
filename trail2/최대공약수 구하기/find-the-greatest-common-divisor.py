n, m = map(int, input().split())

def my_gcd(n,m):
    result = []
    for i in range(1,n+1):
        if n % i == m % i == 0:
            result.append(i)
    print(max(result))

my_gcd(n,m)