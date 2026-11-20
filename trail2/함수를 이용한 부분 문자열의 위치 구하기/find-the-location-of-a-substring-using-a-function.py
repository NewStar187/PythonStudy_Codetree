text = input()
pattern = input()

def pattern_test(t):
    for i in range(len(t)-len(pattern)+1):
        if t[i:i+len(pattern)] == pattern:
            return i
    return -1

print(pattern_test(text))