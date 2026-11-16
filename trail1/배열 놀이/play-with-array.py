N,Q = map(int, input().split())

lst = list(map(int, input().split()))

for i in range(Q):
    commands = list(map(int, input().split()))

    if len(commands) == 2:
        if commands[0] == 1:
            print(lst[commands[1]-1])
        else:
            if commands[1] in lst:
                print(lst.index(commands[1])+1)
            else:
                print(0)
    else:
        print(*lst[commands[1]-1:commands[2]])