lst = list(map(int, input().split()))
lst.remove(lst[-1])
print(max(lst),min(lst))