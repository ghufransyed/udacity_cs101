# 06_is_palindrome


def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return True and is_palindrome(s[1:-1])
        else:
            return False


print is_palindrome('abba')
