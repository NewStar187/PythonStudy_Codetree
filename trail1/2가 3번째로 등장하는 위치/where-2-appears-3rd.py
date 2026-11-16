N = int(input())
lst = list(map(int, input().split()))

cnt = 0
idx = 0

for i in lst:
    idx += 1
    if i == 2:
        cnt += 1

    if cnt == 3:
        print(idx)
        break