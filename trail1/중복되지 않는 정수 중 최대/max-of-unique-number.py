n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
N_nums = list(set(nums))
mx = max(N_nums)

while True:
    if nums.count(mx) == 1:
        print(mx)
        break
    else:
        N_nums.remove(mx)
        if len(N_nums) == 0:
            print(-1)
            break
        else:
            mx = max(N_nums)