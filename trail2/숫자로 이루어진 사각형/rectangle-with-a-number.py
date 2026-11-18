n = int(input())

def print_array(n):
    x = 0
    for i in range(n): # n개의 줄
        for j in range(n): # n개의 숫자
            if x == 9:
                x = 1
                print(x,end = ' ')
            else:
                x += 1
                print(x,end = ' ')
        print()
print_array(n)