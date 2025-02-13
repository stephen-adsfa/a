def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_prime_factors(n):
    original_n = n
    factors = []
    factor = 2
    while n > 1:
        if n % factor == 0:
            factors.append(str(factor))
            n //= factor
        else:
            factor += 1
    print(f"{original_n} = {' * '.join(factors)}")
