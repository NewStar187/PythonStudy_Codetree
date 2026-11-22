N = int(input())

def my_print(N):
    if N == 0:
        return

    print(N,end=' ')
    my_print(N-1)
    print(N,end=' ')

my_print(N)