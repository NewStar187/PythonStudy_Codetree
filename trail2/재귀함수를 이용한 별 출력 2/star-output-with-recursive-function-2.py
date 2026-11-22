n = int(input())

def my_star(n):
    if n == 0:
        return
        
    print("* " * n)
    my_star(n-1)
    print("* " * n)
    # my_star(n-1)

my_star(n)