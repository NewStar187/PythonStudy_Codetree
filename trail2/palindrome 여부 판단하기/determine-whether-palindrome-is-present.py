A = input()

def is_palindrome(s):
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")

is_palindrome(A)