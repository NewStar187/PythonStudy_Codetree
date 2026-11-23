N = int(input())

def cal(n):
    
    if n == 0:
        return 0
    
    return cal(n//10) + (n%10)**2

print(cal(N))