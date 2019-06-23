def betterExp(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        if n % 2 == 0:
            x = betterExp(a, n // 2)
            return x * x
        else:
            x = betterExp(a, (n - 1) // 2)
            return x * x * a