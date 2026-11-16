N_1, N_2 = map(int, input().split())

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

result = False

if N_1 > N_2:
    for i in range(N_1 - N_2+1):
        if lst1[i:i+N_2] == lst2:
            print("Yes")
            result = True
            break
else:
    for i in range(N_2 - N_1+1):
        if lst2[i:i+N_1] == lst1:
            print("Yes")
            result = True
            break

if not result:
    print("No")