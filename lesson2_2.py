def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    s = str(x)
    semi_len = len(s) >> 1
    for i in range(semi_len):
        if s[i] != s[-(i + 1)]:
            return False
    return True

print(isPalindrome(12321))