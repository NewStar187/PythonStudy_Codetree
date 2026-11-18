lst = list(map(int, input().split()))

under_lst = []
upper_lst = []

for i in lst:
    if i < 500:
        under_lst.append(i)
    else:
        upper_lst.append(i)

print(max(under_lst),min(upper_lst))