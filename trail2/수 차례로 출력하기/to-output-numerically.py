n = int(input())

def my_print(n):
    if n == 0:
        return
    
    my_print(n-1)
    print(n,end=' ')

def my_reverse_print(n):
    if n == 0:
        return

    print(n,end=' ')
    my_reverse_print(n-1)

my_print(n)
print()
my_reverse_print(n)