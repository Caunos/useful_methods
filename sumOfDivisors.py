def sumOfDivisors(n):
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n == i*i:
                sum += i
            else:
                sum += i + n//i
    return sum
