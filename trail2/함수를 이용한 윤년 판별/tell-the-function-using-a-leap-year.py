y = int(input())

def is_special_year(y):
    if y % 100 == 0 and y % 400 != 0:
        return "false"
    else:
        if y % 4 == 0:
            return 'true'
        else:
            return 'false'

print(is_special_year(y))