a, b = map(int, input().split())

def is_snum(a,b):
    result = []
    
    for i in range(a,b+1):
        if not (i % 2 == 0) and not(i % 10 == 5) and not( (i % 3 == 0) and not (i % 9 == 0)):
            result.append(i)
    
    return len(result)

print(is_snum(a,b))