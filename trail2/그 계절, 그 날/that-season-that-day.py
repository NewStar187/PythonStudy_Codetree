Y, M, D = map(int, input().split())

def is_special_year(y):
    if y % 100 == 0 and y % 400 != 0:
        return False
    else:
        if y % 4 == 0:
            return True
        else:
            return False

def exist_day(y,m,d):
    if m > 12 or d > 31:
        return False
    else:
        if is_special_year(y):
            if m == 2 and d > 29:
                return False
            else:
                if m < 8:
                    if m % 2 == 1 and d > 31:
                        return False
                    elif m % 2 == 0 and d > 30:
                        return False
                    else:
                        return True
                else:
                    if m % 2 == 0 and d > 31:
                        return False
                    elif m % 2 == 1 and d > 30:
                        return False
                    else:
                        return True
        else:
            if m == 2 and d > 28:
                return False
            else:
                if m < 8:
                    if m % 2 == 1 and d > 31:
                        return False
                    elif m % 2 == 0 and d > 30:
                        return False
                    else:
                        return True
                else:
                    if m % 2 == 0 and d > 31:
                        return False
                    elif m % 2 == 1 and d > 30:
                        return False
                    else:
                        return True


def this_time(y,m,d):
    lst = ["Spring", "Summer", "Fall", "Winter"]

    if exist_day(y,m,d):
        if 3 <= m <= 5:
            return lst[0]
        elif 6 <= m <= 8:
            return lst[1]
        elif 9 <= m <= 11:
            return lst[2]
        else:
            return lst[3]
    else:
        return -1

print(this_time(Y, M, D))