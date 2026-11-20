A = input()

def alpha_num(arr):
    n_set = set(arr)
    if len(n_set) > 1:
        print("Yes")
    else:
        print("No")

alpha_num(A)