n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
N_lst = sorted(a,reverse=True)
print(N_lst[0],N_lst[1])