def isHappy(n: int):
    wow = []
    while (n != 1):
        tmp = 0
        while n:
            tmp += (n % 10) ** 2
            n //= 10
        if tmp in wow: return False
        wow.append(tmp)
        n = tmp
        print(tmp)
    return True

print(isHappy(19))