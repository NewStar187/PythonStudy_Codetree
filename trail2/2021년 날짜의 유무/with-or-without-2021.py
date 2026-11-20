M, D = map(int, input().split())

def exist_day(m,d):
    if m > 12 or d > 31:
        return "No"
    else:
        if m == 2 and d > 28:
            return "No"
        else:
            if m < 8:
                if m % 2 == 1 and d > 31:
                    return "No"
                elif m % 2 == 0 and d > 30:
                    return "No"
                else:
                    return "Yes"
            else:
                if m % 2 == 0 and d > 31:
                    return "No"
                elif m % 2 == 1 and d > 30:
                    return "No"
                else:
                    return "Yes"


print(exist_day(M,D))