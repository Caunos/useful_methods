import math

def sieve(n):
    isPrimeList = [True] * (n+1)
    isPrimeList[0] = False
    isPrimeList[1] = False

    for i in range(2, int(math.sqrt(n))):
        if isPrimeList[i]:
            for j in range(i*2, n, i):
                isPrimeList[j] = False

    return isPrimeList


