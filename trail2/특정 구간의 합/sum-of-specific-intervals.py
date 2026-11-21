n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

def calcul():
    global queries
    global arr

    mysum = []

    for i in range(len(queries)):
        mysum.append(sum(arr[queries[i][0]-1:queries[i][1]]))

    return mysum

for i in calcul():
    print(i)