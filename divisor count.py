def divisorCount(n, x):
    total = 1
    for i in range(n+1):
        if x[i]:
            count = 0
            if n % i == 0:
                while n % i == 0:
                    count += 1
                    n = n // i
                total = total * (count+1)
    return total